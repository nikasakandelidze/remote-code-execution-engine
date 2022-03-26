from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from storage.sessionManager import Base

# class User(Base):
#     __tablename__ = "user"
#
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
#


class Code(Base):
    __tablename__ : str= "code"

    id: Column = Column(Integer, primary_key=True, index=True)
    code_input: Column = Column(String)
    language_id: Column = Column(Integer, ForeignKey('language.id'))

    language = relationship("Language", uselist=False, back_populates="codes")


class Language(Base):
    __tablename__ : str = "language"

    id: Column = Column(Integer, primary_key=True, index=True)
    name: Column = Column(String)
    version: Column = Column(Integer, default=1)

    codes = relationship("Code", back_populates="language")

