from src.models.db.settings.connection import database_connection
from .pets_repository import PetsRepository

database_connection.connect_to_db()


def test_list_pets():
    repo = PetsRepository(database_connection)
    response = repo.list_pets()
    print(response)