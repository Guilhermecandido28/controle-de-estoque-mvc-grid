from infra_db.configs.base import Base
from sqlalchemy import Column, String, Integer, Numeric, BLOB, Date, REAL

class Estoque(Base):
    __tablename__ = "estoque"

    id = Column(Integer,  primary_key=True)
    descricao = Column(String)
    categoria = Column(String)
    marca = Column(String)
    estoque_minimo = Column(Integer)
    quantidade = Column(Integer)
    observacoes = Column(String)
    tamanho = Column(String)
    fornecedor = Column(String)
    cor = Column(String)
    custo = Column(String)
    venda = Column(String)
    imagem = Column(BLOB)

    def __repr__(self):
        return f'Estoque -> Código de Barras = {self.id}, Descrição = {self.descricao}'
    
class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    imagem = Column(BLOB)
    nome = Column(String, nullable=False)
    sobrenome = Column(String, nullable=False)
    celular = Column(String)
    cpf = Column(String)
    instagram = Column(String)
    OBS = Column(String)
    CEP = Column(String)
    rua = Column(String)
    numero = Column(String)
    bairro = Column(String)
    cidade = Column(String)
    estado = Column(String)
    valor_gasto = Column(Numeric)

    def __repr__(self):
        return f'Cliente -> Nome = {self.nome + " " + self.sobrenome}, Contato = {self.celular}'
    
class Compras(Base):
    __tablename__ = "compras"

    id = Column(Integer, primary_key=True)
    data_compra = Column(Date)
    data_entrega = Column(Date)
    codigo_de_barras = Column(String)
    produto = Column(String)
    fornecedor = Column(String)
    forma_de_pagamento = Column(String)
    parcelamento = Column(String)
    vencimento = Column(String)
    qtd_parcial = Column(String)
    quantidade = Column(Integer)
    frete = Column(REAL)
    status = Column(String)
    total = Column(REAL)
    

    def __repr__(self):
        return f'Compra -> Nome = {self.produto}, Parcelado = {self.parcelamento}'
    
class Fornecedor(Base):
    __tablename__ = "fornecedor"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    cnpj = Column(String)
    email = Column(String)
    telefone = Column(String)
    OBS = Column(String)
    CEP = Column(String)
    rua = Column(String)
    numero = Column(String)
    bairro = Column(String)
    cidade = Column(String)
    estado = Column(String)
    lista_produtos = Column(String)
    imagem = Column(BLOB)

    def __repr__(self):
        return f'Fornecedor -> Nome = {self.nome}, Contato = {self.telefone}'
    
class Venda(Base):
    __tablename__ = "venda"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date)
    produtos = Column(String)
    cliente = Column(String)
    desconto = Column(String)
    total = Column(String)
    forma_pagamento = Column(String)


    def __repr__(self):
        return f'Cliente -> Nome = {self.produtos}, Total = {self.total}'