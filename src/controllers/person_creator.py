from src.models.db.repositories.people_repository import PeopleRepository
import re

class PersonCreatorController:
    def __init__(self, people_repository: PeopleRepository):
        self.__people_repository = people_repository

    def create(self, body: dict) -> dict:
        first_name = body['first_name']
        last_name = body['last_name']
        age = body['age']
        pet_id = body['pet_id']

        self.__validate_names(first_name, last_name)
        self.__insert_person_in_db(first_name, last_name, age, pet_id)

        return body

    def __validate_names(self, first_name: str, last_name: str):
        non_valid_name = re.compile(r'[^a-zA-z]')

        if non_valid_name.search(first_name) or non_valid_name.search(last_name):
            raise Exception('Invalid name!')
        
    def __insert_person_in_db(self, first_name: str, last_name: str, age: int, pet_id: str):
        self.__people_repository.insert_person(first_name, last_name, age, pet_id)