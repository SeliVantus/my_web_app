from  sqlalchemy import  Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base

class I(Base):
	__tablename__ = "me"
	
	id_me = Column(Integer, primary_key=True, index=True)
	first_name = Column(String(50), index=True, nullable=False)
	information = Column(String(100), nullable=False)
	birth_date = Column(Date, nullable=False)

	films = relationship("Film", back_populates="user")
	books = relationship("Book", back_populates="user")
	targets = relationship("Target", back_populates="user")
	things = relationship("Thing", back_populates="user")
	people = relationship("People", back_populates="user")

class People(Base):
	__tablename__ = "people"

	id_people = Column(Integer, primary_key = True, index = True)
	id_me = Column(Integer, ForeignKey("me.id_me"), nullable=False)
	first_name = Column(String(20), nullable = False)
	birth_date = Column(Date, nullable = False)
	phone_number = Column(String(11), nullable = False)

	user = relationship("I",back_populates="people")
	prizes = relationship("Prize", back_populates="man")

class Film(Base):
	__tablename__ = "films"

	id_films = Column(Integer, primary_key = True, index = True)
	id_me = Column(Integer, ForeignKey("me.id_me"), nullable=False)
	title = Column(String(50), nullable=False)
	release_date = Column(Date)
	thematics = Column(String(50))

	user = relationship("I", back_populates="films")

class Book(Base):
	__tablename__ = "books"

	id_books = Column(Integer, primary_key = True, index = True)
	id_me = Column(Integer, ForeignKey("me.id_me"), nullable = False)
	title = Column(String(50), nullable = False)
	author = Column(String(50), nullable = False)
	thematics = Column(String(50), nullable = False)
	release_date = Column(String(5), nullable = False)

	user = relationship("I", back_populates="books")

class Target(Base):
	__tablename__ = "targets"
	
	id_targets = Column(Integer, primary_key = True, index = True)
	id_me = Column(Integer, ForeignKey("me.id_me"), nullable = False)
	deadline = Column(Date, nullable = False)
	importance = Column(Integer, nullable = False)
	
	user = relationship("I", back_populates="targets")

class Thing(Base):
	__tablename__ = "things"

	id_things = Column(Integer, primary_key = True, index = True)
	id_me = Column(Integer, ForeignKey("me.id_me"), nullable = False)
	title = Column(String(50), nullable = False)
	price = Column(Integer, nullable = False)

	user = relationship("I", back_populates="things")

class Prize(Base):
	__tablename__ = "prizes"

	id_prizes = Column(Integer, primary_key = True, index = True)
	id_people = Column(Integer, ForeignKey("people.id_people"), nullable = False)
	title = Column(String(50), nullable = False)

	man = relationship("People", back_populates="prizes")
