from typing import List
from src.models.db.entities.pets import PetsTable
from sqlalchemy.orm.exc import NoResultFound

class PetsRepository:
    def __init__(self, db) -> None:
        self.__db = db

    def list_pets(self) -> List[PetsTable]:
        with self.__db as database:
            try:
                pets = database.session.query(PetsTable).all()

                return pets
            except NoResultFound:
                return []
            
    def delete_pets(self, name: str) -> None:
        with self.__db as database:
            try:
                (
                    database
                        .session
                        .query(PetsTable)
                        .filter(PetsTable.name == name)
                        .delete()
                )

                database.session.commit()
            except Exception:
                database.session.rollback()
                raise Exception