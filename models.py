from database import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey,Boolean,DateTime,Enum
from sqlalchemy.orm import relationship




class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), unique=True, index=True)
    email = Column(String(250), unique=True, index=True)
    password = Column(Text)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f'<User(username={self.username}, email={self.email})>'


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    published_date = Column(DateTime)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship("Author", back_populates="books")
    reviews = relationship("Review", back_populates="book")


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    rating = Column(Integer)
    book_id = Column(Integer, ForeignKey('books.id'))

    book = relationship("Book", back_populates="reviews")





