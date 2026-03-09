# Biblioteca sqlalchemy para criar a conexão com o banco de dados
# criar um ambiente virtual python
from sqlalchemy import create_engine
#importar tipos de dados e estrutura das colunas
from sqlalchemy import Column, Integer, String, Float, Boolean

# Importar a classe base para criar as classes de modelo
from sqlalchemy.orm import declarative_base
# Importa a ferramenta para criar sessões de banco de dados
from sqlalchemy.orm import sessionmaker

# classe base para ORM (Object-Relational Mapping)
Base = declarative_base()

# classes = tabelas do banco de dados
# objeto de cada classe é uma linha da tabela
# atributos= colunas da tabela

# classe produto representa a tabela 'produtos' no banco de dados
class Produto(Base):
    # nome da tabela no banco de dados
    __tablename__ = "produtos"
    # coluna de id
    # Interger > números inteiros
    # primary_key=True > define a coluna como chave primária
    id = Column(Integer, primary_key=True)
    # coluna de nome do produto
    # string > texto
    nome = Column(String(100),)
    # coluna de preço do produto
    # Float > números decimais
    preco = Column(Float)
    # metodo construtor
    def __init__(self, nome, preco, estoque, ativo):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.ativo = ativo
    # quantidade em estoque
    estoque = Column(Integer)
    # Produto disponível para venda
    ativo = Column(Boolean)

    # Representação do objeto para imprimir
    def __repr__(self):
        return f"Produto(id={self.id}, nome={self.nome}, preco={self.preco}, estoque={self.estoque}, ativo={self.ativo})"

# criar a conexão com o banco de dados
# echo=True > log do sql
engine = create_engine("sqlite:///estoque.db", echo=True)

# criar as tabelas no banco de dados (se não existirem)
Base.metadata.create_all(engine)
# criar uma fabrica de sessões para interagir com o banco de dados
Session = sessionmaker(bind=engine)
# criar uma sessão
# carrinho de compras para adicionar, consultar, atualizar e deletar produtos
session = Session()

# criar um novo produto
produto1 = Produto("notebook",  5500, 6, True)
produto2 = Produto("teclado",  250, 10, True)
produto3 = Produto("mouse",  150, 55, True)
# Adicionar os produtos à sessão e salvar no banco de dados
session.add(produto1)
session.add(produto2)
session.add(produto3)
# confirmar a inserção dos produtos no banco de dados
# Salvar as alterações no banco de dados
session.commit()

# listar/ Consultar todos os produtos
produtos = session.query(Produto).all()
for produto in produtos:
    print(produto)
for p in produtos:
    print(f"ID: {p.id}, Nome: {p.nome}, Preço: {p.preco}, Estoque: {p.estoque}, Ativo: {p.ativo}")
# coisas para não esquecer:
# importar os valores padroes do sqlalchemy
# cada classe vira uma tabela no banco de dados
# cada objeto vai representar uma linha da tabela
# os atributos da classe são as colunas da tabela (banco de dados)