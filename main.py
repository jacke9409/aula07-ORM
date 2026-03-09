# Biblioteca sqlalchemy para criar a conexão com o banco de dados
# criar um ambiente virtual python
from sqlalchemy import create_engine
#importar tipos de dados e estrutura das colunas
from sqlalchemy import Column, Integer, String, Float, Boolean

# Importar a classe base para criar as classes de modelo
from sqlalchemy.orm import declarative_base
# Importa a ferramenta para criar sessões de banco de dados
from sqlalchemy.orm import sessionmaker
