from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.connection import db

Base = declarative_base()

class Usuario():
    # Definindo caracteristicas da tabela.
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(250))
    email = Column(String(250), unique=True)
    senha = Column(String(250))