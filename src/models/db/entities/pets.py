import uuid
from sqlalchemy import Column, Text, UUID
from src.models.db.settings.base import Base

class PetsTable(Base):
    __tablename__ = 'pets'

    id = Column(UUID, primary_key=True, default=uuid.uuid7)
    name = Column(Text, nullable=False)
    type = Column(Text, nullable=False)