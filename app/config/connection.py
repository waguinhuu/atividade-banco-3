from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Parâmetros para conexão com banco de dados MySQL.
db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_ban