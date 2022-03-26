from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db/"
Base = declarative_base()


class SessionManager:
    def __init__(self, initialize_schema = True):
        self.engine = create_engine(
            SQLALCHEMY_DATABASE_URL
        )
        self.session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        if initialize_schema:
            Base.metadata.drop_all(bind=self.engine)
            Base.metadata.create_all(bind=self.engine)

    def get_new_session(self):
        return self.session_local()