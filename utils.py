from sqlalchemy import select

from models import Produto, Venda, Categoria, Cliente, db_session


def inserir_produto():
    produto = Produto(nome_produto=str(input('Nome: ')),
                      PRECO=str(input('Preço: ')),
                      cat_produtos=str(input('Categoria: ')),
                      )
    print(produto)
    produto.save()


def consultar_produto():
    var_produto = select(Produto)
    var_produto = db_session.execute(var_produto).all()
    print(var_produto)


def atualizar_produto():
    var_produto = select(Produto).where(Produto.nome_produto == str(input('Nome: ')))
    var_produto = db_session.execute(var_produto).scalar()
    print(var_produto)
    var_produto.nome_produto = str(input('Nome: '))
    var_produto.save()


def deletar_produto():
    produto = Produto.query.filter_by(nome_produto=str(input('Nome:'))).first()
    print(produto)
    produto.delete()


def inserir_venda():
    venda = Venda(data2=str(input('Data da venda: ')),
                  id_produto2=int(input('ID do produto:  ')),
                  id_cliente2=(input('ID do cliente: ')),
                  qtd2=int(input('Quantidade de vendas: '))
                  )
    print(venda)
    venda.save()


def consultar_venda():
    var_venda = select(Venda)
    var_venda = db_session.execute(var_venda).all()
    print(var_venda)


def atualizar_venda():
    var_venda = select(Venda).where(Venda.id_produto2 == str(input('Nome ID Produto: ')))
    var_venda = db_session.execute(var_venda).scalar()
    print(var_venda)
    var_venda.id_produto2 = str(input('Novo ID da venda: '))
    var_venda.save()


def deletar_venda():
    venda = Venda.query.filter_by(id_venda2=str(input('Nome do ID da venda:'))).first()
    print(venda)
    venda.delete()


def inserir_categoria():
    categoria = Categoria(nome_categoria=str(input('Nome da Categoria: ')),
                          )
    print(categoria)
    categoria.save()


def consultar_categoria():
    var_categoria = select(Categoria)
    var_categoria = db_session.execute(var_categoria).all()
    print(var_categoria)


def atualizar_categoria():
    var_categoria = select(Categoria).where(Categoria.nome_categoria == str(input('Nome Categoria: ')))
    var_categoria = db_session.execute(var_categoria).scalar()
    print(var_categoria)
    var_categoria.nome_categoria = str(input('Novo Nome Categoria: '))
    var_categoria.save()


def deletar_categoria():
    categoria = Categoria.query.filter_by(nome_categoria=str(input('Nome Categoria:'))).first()
    print(categoria)
    categoria.delete()


def inserir_cliente():
    cliente = Cliente(Nome2=str(input('Nome: ')),
                      CPF=str(input('CPF: ')),
                      telefone=str(input('Telefone: ')),
                      Profissao2=str(input('Profissão: ')),
                      Area2=str(input('Área: ')),

                      )
    print(cliente)
    cliente.save()


def consultar_cliente():
    var_cliente = select(Cliente)
    var_cliente = db_session.execute(var_cliente).all()
    print(var_cliente)


def atualizar_cliente():
    var_cliente = select(Cliente).where(Cliente.Nome2 == str(input('Nome Cliente: ')))
    var_cliente = db_session.execute(var_cliente).scalar()
    print(var_cliente)
    var_cliente.Nome2 = str(input('Novo Nome Cliente: '))
    var_cliente.save()


def deletar_cliente():
    cliente = Cliente.query.filter_by(Nome2=str(input('Nome Cliente:'))).first()
    print(cliente)
    cliente.delete()


if __name__ == '__main__':
    consultar_produto()

    while True:
        print('Menu')
        print('[1] Inserir produto')
        print('[2] Consultar produto')
        print('[3] Atualizar produto')
        print('[4] Deletar produto')
        print('')
        print('[5] Inserir venda')
        print('[6] Consultar venda')
        print('[7] Atualizar venda')
        print('[8] Deletar venda')
        print('')
        print('[9] Inserir categoria')
        print('[10] Consultar categoria')
        print('[11] Atualizar categoria')
        print('[12] Deletar categoria')
        print('')
        print('[13] Inserir cliente')
        print('[14] Consultar cliente')
        print('[15] Atualizar cliente')
        print('[16] Deletar cliente')
        print('')
        print('[17] Sair')

        escolha = int(input('Escolha: '))
        if escolha == 1:
            inserir_produto()
        elif escolha == 2:
            consultar_produto()
        elif escolha == 3:
            atualizar_produto()
        elif escolha == 4:
            deletar_produto()

        elif escolha == 5:
            inserir_venda()
        elif escolha == 6:
            consultar_venda()
        elif escolha == 7:
            atualizar_venda()
        elif escolha == 8:
            deletar_venda()


        elif escolha == 9:
            inserir_categoria()
        elif escolha == 10:
            consultar_categoria()
        elif escolha == 11:
            atualizar_categoria()
        elif escolha == 12:
            deletar_categoria()

        elif escolha == 13:
            inserir_cliente()
        elif escolha == 14:
            consultar_cliente()
        elif escolha == 15:
            atualizar_cliente()
        elif escolha == 16:
            deletar_cliente()
        elif escolha == 17:
            break
