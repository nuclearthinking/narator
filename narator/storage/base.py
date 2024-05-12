import datetime

import sqlalchemy as sa
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import relationship, selectinload, sessionmaker, scoped_session, declarative_base

engine = create_engine('sqlite:///narator.db')

db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Books(Base):
    __tablename__ = 'books'
    id = Column(sa.Integer, primary_key=True, autoincrement=False)
    language = Column(sa.Enum('en', 'ru'), nullable=False)
    title = Column(String(100), nullable=False)
    chapters = relationship('Chapter', backref='books')


class Chapter(Base):
    __tablename__ = 'chapters'
    id = Column(sa.Integer, primary_key=True)
    chapter_number = Column(sa.Integer, nullable=False)
    text = Column(sa.Text, nullable=False)
    title = Column(String(255), nullable=False)
    book_id = Column(sa.Integer, sa.ForeignKey('books.id'))
    audio = relationship('Audio', backref='chapters', uselist=False, cascade='all, delete-orphan')
    locked_until = Column(sa.DateTime, nullable=True)


class Audio(Base):
    __tablename__ = 'audio'
    id = Column(sa.Integer, primary_key=True)
    chapter_id = Column(sa.Integer, sa.ForeignKey('chapters.id'))
    book_id = Column(sa.Integer, sa.ForeignKey('books.id'))
    data = Column(sa.LargeBinary, nullable=False)
    __table_args__ = (sa.UniqueConstraint('chapter_id', 'book_id', name='audio_chapter_id_book_id_uindex'),)


def initialize_db():
    Base.metadata.create_all(bind=engine, checkfirst=True)


def add_book_if_not_exist(book_id, title, language: str):
    query = sa.select(Books).where(Books.id == book_id)
    book = db_session.execute(query).scalar_one_or_none()
    if not book:
        book = Books(id=book_id, title=title, language=language)
        db_session.add(book)
        db_session.commit()


def get_book(book_id):
    query = sa.select(Books).where(Books.id == book_id)
    return db_session.execute(query).scalar_one_or_none()


def add_chapter(chapter_number: int, text: str, title: str, book_id: int):
    query = sa.select(Chapter).where(Chapter.chapter_number == chapter_number, Chapter.book_id == book_id)
    chapter = db_session.execute(query).scalar_one_or_none()
    if chapter:
        return

    chapter = Chapter(chapter_number=chapter_number, text=text, title=title, book_id=book_id)
    db_session.add(chapter)
    db_session.commit()


def get_chapter(chapter_number, book_id) -> Chapter | None:
    query = sa.select(Chapter).where(Chapter.chapter_number == chapter_number, Chapter.book_id == book_id)
    return db_session.execute(query).scalar_one_or_none()


def get_chapters(book_id, chapter_number, limit=10) -> list[Chapter]:
    query = (
        sa.select(Chapter)
        .where(Chapter.book_id == book_id, Chapter.chapter_number > chapter_number)
        .order_by(Chapter.chapter_number)
        .limit(limit)
    )
    return list(db_session.execute(query).scalars().all())


def get_next_chapter(book_id: int, chapter_from: int) -> Chapter | None:
    query = (
        sa.select(Chapter)
        .options(selectinload(Chapter.audio))
        .where(
            Chapter.book_id == book_id,  # noqa
            Chapter.chapter_number > chapter_from,  # noqa
            Chapter.audio == None,  # noqa
            sa.or_(Chapter.locked_until <= datetime.datetime.utcnow(), Chapter.locked_until.is_(None)),  # noqa
        )
        .order_by(Chapter.chapter_number)
        .limit(1)
    )
    result = db_session.execute(query).scalar_one_or_none()
    if result:
        result.locked_until = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        db_session.commit()
    return result


def save_narrated_chapter(chapter_id: int, book_id: int, data: bytes) -> None:
    audio = Audio(chapter_id=chapter_id, data=data, book_id=book_id)
    db_session.add(audio)
    db_session.commit()
