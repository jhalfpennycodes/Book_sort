from app import app, db
from app.forms import LoginForm, RegisterForm, Add_book
from app.models import User, Book
from flask import Flask, flash, redirect, url_for, request, abort, render_template
from flask_login import login_user, logout_user, login_required
from flask_user import current_user
from werkzeug.security import check_password_hash, generate_password_hash


@app.route('/')
def home_page():
    if current_user.is_authenticated:
        return redirect(url_for('member_home'))
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            username = form.username.data
            password = form.password.data
            remember = True if request.form.get('remember') else False

            user = User.query.filter_by(username=username).first()

            if user and check_password_hash(user.password, password):
                login_user(user, remember=remember)
                return redirect(url_for('library'))
            else:
                flash('Username or password is incorrect, please try again.\n')
                return redirect(url_for('login'))
        except Exception as e:
            flash('Username or password is incorrect, please try again.\n')
            return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        name = form.name.data

        user = User.query.filter_by(username=username).first()

        if user:
            flash('Username already exists.')
            return redirect(url_for('register'))

        new_user = User(username=username, name=name, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash('Successfully created account')

    return render_template('register.html', form=form)



#---------------------------------- APP ROUTES ---------------------------------- :


@app.route('/member')
@login_required
def member_home():
    return render_template('member.html')


@app.route('/library', methods = ['GET'])
@login_required
def library():
    books = Book.query.all()
    return render_template('library.html', books=books)


@app.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    form = Add_book()
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data, description=form.description.data, rating=form.rating.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('library'))
    return render_template('add_book.html', form=form)


@app.route('/delete_book/<id>', methods=['GET', 'POST'])
@login_required
def delete_book(id):
    book = Book.query.filter_by(id=int(id)).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('library'))


@app.route('/edit_book/<id>', methods=['GET', 'POST'])
@login_required
def edit_book(id):
    book = Book.query.filter_by(id=int(id)).first()
    form = Add_book()
    if form.validate_on_submit():
        try:
            book.title = form.title.data
            book.author = form.author.data
            book.rating = form.rating.data
            db.session.commit()
            flash("Your reading has been edited.")
            return redirect(url_for('edit_book'))
        except Exception as e:
            flash('Failed to update reading\n' + str(e), 'error')
            return redirect(url_for('edit_book'))
    return render_template('edit_reading.html', form=form, book=book)


@app.route('/readings', methods=['GET'])
@login_required
def readings():
    user = current_user
    read = User.query.filter_by().first()
    return render_template('readings.html', user=user, read=read)


@app.route('/add_to_readings/<id>', methods=['GET', 'POST'])
@login_required
def add_to_readings(id):
    user = current_user
    reading = Book.query.filter_by(id=int(id)).first()
    user.reading.append(reading)
    db.session.commit()
    return redirect(url_for('readings'))


@app.route('/complete_reading/<id>', methods=['GET', 'POST'])
@login_required
def complete_reading(id):
    curr_reading = Book.query.filter_by(id=int(id)).first()
    user = current_user
    user.reading.remove(curr_reading)
    db.session.commit()
    return redirect(url_for('readings'))

