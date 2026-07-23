from src.models.db.repositories.pets_repository import PetsRepository
from src.models.db.entities.pets import PetsTable

class PetListerController:
    def __init__(self, pets_repository: PetsRepository):
        self.__pets_repository = pets_repository

    def list(self) -> dict:
        pets = self.__get_pets_in_db()

        response = self.__format_response(pets)

        return response

    def __get_pets_in_db(self) -> list[PetsTable]:
        pets = self.__pets_repository.list_pets()

        return pets
        
    def __format_response(self, pets: list[PetsTable]) -> dict:
        pets = []

        for pet in pets:
            pets.append({ 'name': pet.name, 'type': pet.type })

        return { pets }