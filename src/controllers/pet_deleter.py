from src.models.db.repositories.pets_repository import PetsRepository

class PetDeleterController:
    def __init__(self, pets_repository: PetsRepository):
        self.__pets_repository = pets_repository

    def delete(self, name: str) -> None:
        self.__pets_repository.delete_pets(name)