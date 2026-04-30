from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

class DatabaseManager:
    engine: Engine

    def __init__(self):
        self.engine = create_engine("sqlite:///termini.db")

database_manager = DatabaseManager()
