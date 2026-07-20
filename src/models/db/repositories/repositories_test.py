import pytest
from src.models.db.settings.connection import database_connection
from .pets_repository import PetsRepository

database_connection.connect_to_db()

repo = PetsRepository(database_connection)

@pytest.mark.skip(reason='database interaction')
def test_list_pets():
    response = repo.list_pets()
    print(response)

@pytest.mark.skip(reason='database interaction')
def test_delete_pet():
    name = 'belinha'

    repo.delete_pets(name)