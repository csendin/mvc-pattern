import pytest
from sqlalchemy.engine import Engine
from .connection import database_connection

@pytest.mark.skip(reason='database interaction')
def test_connect_to_database():
    assert database_connection.get_engine() is None

    database_connection.connect_to_database()
    database_engine = database_connection.get_engine()

    assert database_engine is not None
    assert isinstance(database_engine, Engine)