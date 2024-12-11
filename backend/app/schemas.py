from pydantic import BaseModel
from typing import Optional
from datetime import date

class FilmCreate(BaseModel):
	title: str
	release_date: Optional[date]
	thematics: Optional[str]

class BookCreate(BaseModel):
	title: str
	author: str
	thematics: str
	release_date: str

class PeopleCreate(BaseModel):
	first_name: str
	birth_date: date
	phone_number: str

class ThingCreate(BaseModel):
	title: str
	price: int

class TargetCreate(BaseModel):
	deadline: date
	importance: int
