from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Parâmetros para conexão com BD MySQL:
db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

# Endereço para conexão com BD MySQL:
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Conectando ao banco de dados:
db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session()

# Gerenciando sessão:
@contextmanager
def get_db():
    db = Session
    try:
        yield db
        db.commit() # Se caso der certo, faz o commit
    except Exception as erro:
        db.rollback() # Se caso der erro, desfaz a operação
        raise erro # Lança a exceção, informando o erro
    finally:
        db.close() # Garante o fechamento da sessão