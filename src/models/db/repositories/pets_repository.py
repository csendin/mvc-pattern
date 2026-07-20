from typing import List
from src.models.db.entities.pets import PetsTable
from sqlalchemy.orm.exc import NoResultFound

class PetsRepository:
    def __init__(self, db):
        self.__db = db

    def list_pets(self) -> List:
        with self.__db as database:
            try:
                pets = database.session.query(PetsTable).all()

                return pets
            except NoResultFound:
                return []