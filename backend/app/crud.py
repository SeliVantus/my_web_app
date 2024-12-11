
from sqlalchemy.orm import Session
from datetime import date
from . import models

def get_info_about_me(db: Session):
	try:
		result = db.query(models.I).filter(models.I.id_me==1).first()
		if result  is None:
			print("Zapis' with id_me = 1 not found")
		return result
	except Exception as e:
		print(f"Error with request data: {e}")
		return None

def get_me_films(db: Session):
	try:
		result = db.query(models.Film).filter(models.Film.id_me==1).all()
		if result  is None:
			print("Zapis' with id_me = 1 not found")
		return result
	except Exception as e:
		print(f"Error with request data: {e}")
		return None

def add_film(db: Session, title: str, release_date: date, thematics: str = None):
	film = models.Film(
		id_me = 1, 
		title = title, 
		release_date = release_date, 
		thematics = thematics
	)
	try:
		db.add(film)
		db.commit()
		db.refresh(film)

	except Exception as e:
		db.rollback()
		raise e
	return film

def delete_film(db: Session, id_films: int):
	film = db.query(model.Film).filter(model.Film.id_films == id_films).first()
	if film:
		try:
			db.delete(film)
			db.commit
		except Exception as e:
			db.rollback()
			raise e
	else:
		raise ValueError(f"Film with id_films = {id_films} dos not exist")
	return film

def get_me_books(db: Session):
	try:
		result = db.query(models.Book).filter(models.Book.id_me==1).all()
		if result  is None:
			print("Zapis' with id_me = 1 not found")
		return result
	except Exception as e:
		print(f"Error with request data: {e}")
		return None

def add_book(db: Session, title: str, author: str, thematics: str, release_date: str):
	book = models.Book(
		id_me = 1, 
		title = title, 
		author = author, 
		thematics = thematics, 
		release_date = release_date
	)
	try:
		db.add(book)
		db.commit()
		db.refresh(book)

	except Exception as e:
		db.rollback()
		raise e
	return book

def delete_book(db: Session, id_books: int):
	book = db.query(model.Book).filter(model.Book.id_books == id_books).first()
	if book:
		try:
			db.delete(book)
			db.commit
		except Exception as e:
			db.rollback()
			raise e
	else:
		raise ValueError(f"Film with id_books = {id_books} dos not exist")
	return book

def get_me_people(db: Session):
	try:
		result = db.query(models.People).filter(models.People.id_me==1).all()
		if result  is None:
			print("Zapis' with id_me = 1 not found")
		return result
	except Exception as e:
		print(f"Error with request data: {e}")
		return None

def add_people(db: Session, first_name: str, birth_date: date, phone_number: str):
	people = models.People(
		id_me = 1,
		first_name = first_name,
		birth_date = birth_date,
		phone_number = phone_number
	)
	try:
		db.add(people)
		db.commit()
		db.refresh(people)
	except Exception as e:
		db.rollback()
		raise e
	return people

def get_me_prize_for_people(id_people: int, db: Session):
	try:
		result = db.query(models.Prize).filter(models.Prize.id_people==id_people).all()
		if result  is None:
			print("Zapis' with id_me = 1 not found")
		return result
	except Exception as e:
		print(f"Error with request data: {e}")
		return None

def get_me_things(db: Session):
	try:
		result = db.query(models.Thing).filter(models.Thing.id_me==1).all()
		if result is None:
			print("Zapis' with id_me = 1 not found")
		return result
	except Exception as e:
		print(f"Error with request data: {e}")
		return None

def add_thing(db: Session, title: str, price: int):
	thing = model.Thing(
		id_me = 1,
		title = title,
		price = price
	)
	try:
		db.add(thing)
		db.commit()
		db.refresh(thing)
	except Exception as e:
		db.rollback()
		raise e
	return thing

def get_me_targets(db: Session):
	try:
		result = db.query(models.Target).filter(models.Target.id_me==1).all()
		if result is None:
			print("Zapis' with id_me = 1 not found")
		return result
	except Exception as e:
		print(f"Error with request data: {e}")
		return None

def add_target(db: Session, deadline: date, importance: int):
	target = model.Target(
		id_me = 1,
		deadline = deadline,
		importance = importance
	)
	try:
		db.add(target)
		db.commit()
		db.refresh(target)
	except Exception as e:
		db.rollback()
		raise e
	return target

