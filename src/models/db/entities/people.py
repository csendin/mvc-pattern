import uuid
from sqlalchemy import Column, Text, UUID, Integer, ForeignKey
from src.models.db.settings.base import Base

class PeopleTable(Base):
    __tablename__ = 'people'

    id = Column(UUID, primary_key=True, default=uuid.uuid7)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    age = Column(Integer, nullable=False)
    pet_id = Column(UUID, ForeignKey('pets.id'))