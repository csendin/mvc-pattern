from src.models.db.repositories.people_repository import PeopleRepository

class PersonFinderController:
    def __init__(self, people_repository: PeopleRepository):
        self.__people_repository = people_repository

    def find(self, person_id: str) -> dict:
        person = self.__find_person_in_db(person_id)

        return person

    def __find_person_in_db(self, person_id: str):
        person = self.__people_repository.get_person(person_id)

        if not person:
            raise Exception('Person not found')
        
        return person