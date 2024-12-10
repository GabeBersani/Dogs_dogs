# importar biblioteca
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, relationship

# fala onde esta o banco (colocar um nome, ex: engine)
engine = create_engine('sqlite:///base_vet_analise_5.sqlite3')

# gerenciar sessoes com banco de dados
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Produto(Base):
    __tablename__ = 'TAB_PRODUTO'
    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome_produto = Column(String(40), index=True, nullable=False)
    PRECO = Column(String(1000), index=True)
    cat_produtos = Column(ForeignKey('TAB_CATEGORIA.nome_categoria'), nullable=False)

    def __repr__(self):
        return '< ID Produto: {} Produto: {}  Preço: {} Categoria {} >'.format(self.id_produto, self.nome_produto, self.PRECO, self.cat_produtos)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


    def serialize_produto(self):
        dados_produto = {
            'id_produto': self.id_produto,
            'nome_produto': self.nome_produto,
            'PRECO': self.PRECO,
            'cat_produtos': self.cat_produtos

        }
        return dados_produto


class Venda(Base):
    __tablename__ = 'TAB_VENDA'
    id_venda2 = Column(Integer, primary_key=True, autoincrement=True)
    data2 = Column(String, index=True, nullable=False)
    id_produto2 = Column(Integer, ForeignKey('TAB_PRODUTO.id_produto'), nullable=False)
    id_cliente2 = Column(Integer, ForeignKey('TAB_CLIENTE.id_cliente'), nullable=False)
    qtd2 = Column(Integer, index=True, nullable=False)


    def __repr__(self):
        return '<ID Venda: {}  Data: {} ID Produto {} ID Cliente {} Quantidade: {}>'.format(self.id_venda2, self.data2,
                                                                self.id_produto2, self.id_cliente2, self.qtd2)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_venda(self):
        dados_venda = {
            'id_venda2': self.id_venda2,
            'data2': self.data2,
            'id_produto2': self.id_produto2,
            'id_cliente2': self.id_cliente2,
            'qtd2': self.qtd2
        }
        return dados_venda



class Categoria(Base):
    __tablename__ = 'TAB_CATEGORIA'
    id_categoria = Column(Integer, primary_key=True, autoincrement=True)
    nome_categoria = Column(String(100), index=True, nullable=False)


    def __repr__(self):
        return '<ID Categoria: {}  Nome categoria: {} >'.format(self.id_categoria, self.nome_categoria
                                                                )


    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


    def serialize_categoria(self):
        dados_categoria = {
            'id_categoria': self.id_categoria,
            'nome_categoria': self.nome_categoria
        }
        return dados_categoria


class Cliente(Base):
    __tablename__ = 'TAB_CLIENTE'
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    CPF = Column(String(100), index=True, nullable=False, unique=True)
    Nome2 = Column(String(100), index=True, nullable=False)
    telefone = Column(String(20), index=True, nullable=False)
    Profissao2 = Column(String(100), index=True, nullable=False)
    Area2 = Column(String(100), index=True, nullable=False)


    def __repr__(self):
        return '<ID Cliente: {} CPF:{}  Nome: {} Telefone {} ID Profissão {} Área: {}>'.format(self.id_cliente, self.CPF,
                                                                                        self.Nome2,  self.telefone,
                                                                                        self.Profissao2, self.Area2)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


    def serialize_cliente(self):
        dados_venda = {
            'id_cliente': self.id_cliente,
            'CPF': self.CPF,
            'Nome2': self.Nome2,
            'telefone': self.telefone,
            'Profissao2': self.Profissao2,
            'Area2': self.Area2
        }
        return dados_venda




def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()