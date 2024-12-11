from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from . import models, crud, database
from .schemas import FilmCreate, BookCreate, PeopleCreate, ThingCreate, TargetCreate

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.get("/me")
def read_root_slide(db: Session = Depends(database.get_db)):
	info_about_me = crud.get_info_about_me(db)
	print("Result request:", info_about_me)
	if info_about_me is None:
		return {"error: No data found for id_me = 1"}
	return {"me": info_about_me}

@app.get("/me/films")
def read_me_films(db: Session = Depends(database.get_db)):
	film = crud.get_me_films(db)
	return {"films": film}

@app.post("/me/films")
def create_film(
	film: FilmCreate, 
	db: Session = Depends(database.get_db)
):

	film = crud.add_film(
		db, 
		title=film.title, 
		release_date=film.release_date, 
		thematics=film.thematics
	)
	return {"film": film}

@app.delete("/me/films")
def delete_film(id_films: int, db: Session = Depends(database.get_db)):
	try:
		film = crud.delete_film(db, id_films=id_films)
		return {"mesage": f"Film with id {id_films} has been deleted", "film": film}
	except ValueError as e:
		raise HTTPException(status_code=404, detail=str(e))
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Error deleting film: {e}")

@app.get("/me/books")
def read_me_books(db: Session = Depends(database.get_db)):
	book = crud.get_me_books(db)
	return {"books": book}

@app.post("/me/books")
def create_book(
	book: BookCreate,
	db: Session = Depends(database.get_db)
):

	book = crud.add_book(
		db,
		title=book.title,
		author=book.author,
		thematics=book.thematics,
		release_date=book.release_date
	)
	return {"book": book}

@app.delete("/me/books")
def delete_book(id_books: int, db: Session = Depends(database.get_db)):
	try:
		book = crud.delete_book(db, id_books=id_books)
		return {"mesage": f"Book with id {id_books} has been deleted", "book": book}
	except ValueError as e:
		raise HTTPException(status_code=404, detail=str(e))
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Error deleting books: {e}")


@app.get("/me/people")
def get_me_people(db: Session = Depends(database.get_db)):
	people = crud.get_me_people(db)
	return {"people": people}

@app.post("/me/people")
def add_people(
	people: PeopleCreate,
	db: Session = Depends(database.get_db)
):

	people = crud.add_people(
		db,
		first_name = people.first_name,
		birth_date = people.birth_date,
		phone_number = people.phone_number
	)
	return {"people": people}

@app.get("/me/people/{id_people}/prize")
def get_me_prize_for_people(id_people: int, db: Session = Depends(database.get_db)):
	prizes = crud.get_me_prize_for_people(id_people, db)
	return {"prize": prizes}

@app.get("/me/things")
def get_me_things(db: Session = Depends(database.get_db)):
	things = crud.get_me_things(db)
	return {"things": things}

@app.post("/me/things")
def add_thing(
	thing: ThingCreate,
	db: Session = Depends(database.get_db)
):

	things = crud.add_thing(
		db,
		title = thing.title,
		price = thing.price
	)
	return {"thing": thing}

@app.get("/me/targets")
def get_me_targets(db: Session = Depends(database.get_db)):
        targets = crud.get_me_targets(db)
        return {"targets": targets}

@app.post("/me/targets")
def add_target(
        target: TargetCreate,
        db: Session = Depends(database.get_db)
):

        target = crud.add_target(
                db,
                deadline = target.deadline,
                importance = target.importance
        )
        return {"target": target}
