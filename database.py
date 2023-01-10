import sqlalchemy
from dataclasses import dataclass

@dataclass
class Database:
    DB_HOST: str = None
    DB_PORT: str = None
    DB_USERNAME: str = None
    DB_PASSWORD: str = None
    DB_TYPE: str = None

    def get_engine(self):
        from sqlalchemy import create_engine

        if not self.DB_TYPE:
            self.DB_TYPE = "postgres"
        
        if self.DB_TYPE == "postgres":
            conn_str: str = f'postgresql+psycopg2://{self.DB_HOST}:{self.DB_PASSWORD}@{self.DB_HOST}/{self.DB_PORT}'
            engine = create_engine(conn_str)
            return engine