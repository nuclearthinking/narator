from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base, relationship
import sqlalchemy as sa

engine = create_engine('sqlite:///narator.db')

db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Books(Base):
    __tablename__ = 'books'
    id = Column(sa.Integer, primary_key=True, autoincrement=False)
    title = Column(String(100), nullable=False)
    chapters = relationship('Chapters', backref='books')


class Chapters(Base):
    __tablename__ = 'chapters'
    id = Column(sa.Integer, primary_key=True)
    chapter_number = Column(sa.Integer, nullable=False)
    text = Column(sa.Text, nullable=False)
    title = Column(String(255), nullable=False)
    book_id = Column(sa.Integer, sa.ForeignKey('books.id'))


Base.metadata.create_all(bind=engine, checkfirst=True)


def add_book_if_not_exist(book_id, title):
    book = Books.query.filter_by(id=book_id).first()
    if not book:
        book = Books(id=book_id, title=title)
        db_session.add(book)
        db_session.commit()


def add_chapter(chapter_number, text, title, book_id):
    chapter = Chapters.query.filter_by(chapter_number=chapter_number, book_id=book_id).first()
    if chapter:
        return

    chapter = Chapters(chapter_number=chapter_number, text=text, title=title, book_id=book_id)
    db_session.add(chapter)
    db_session.commit()


def get_chapter(chapter_number, book_id) -> Chapters | None:
    chapter = Chapters.query.filter_by(chapter_number=chapter_number, book_id=book_id).first()
    return chapter
