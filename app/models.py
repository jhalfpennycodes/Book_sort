from app import db
from flask_user import UserMixin


user_book = db.Table('reading',
                db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                db.Column('book_id', db.Integer, db.ForeignKey('books.id'))
            )


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100, collation='NOCASE'), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    name = db.Column(db.String(100), nullable=True, unique=False)

    reading = db.relationship('Book', secondary=user_book, backref='readers')


class Book(db.Model, UserMixin):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=True)
    rating = db.Column(db.Integer)