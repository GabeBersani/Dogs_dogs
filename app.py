from urllib import request
from flask import Flask, render_template, redirect, url_for, flash, request
from sqlalchemy import select

from models import Produto, Venda, Categoria, Cliente, db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gabriele123'


@app.route('/')
def redirecionar():
    return redirect(url_for('base'))


@app.route('/base')
def base():
    return render_template('home.html')


@app.route('/produto')
def produto():
    sql_produto = select(Produto)
    resultado_produto = db_session.execute(sql_produto).scalars()
    print(resultado_produto)
    produto = []
    for n in resultado_produto:
        produto.append(n.serialize_produto())
        print(produto[-1])

    return render_template("produto.html",
                           produto=produto)


@app.route('/novo_produto', methods=['GET', 'POST'])
def novo_produto():
    if request.method == 'POST':
        if not request.form["nome_produto"]:
            flash("preencher todos os campos", "erro")
            if not request.form["PRECO"]:
                flash("preencher todos os campos", "erro")
                if not request.form["cat_produtos"]:
                    flash("preencher todos os campos", "erro")

                    return redirect(url_for('produto'))

        else:
            form_evento = Produto(nome_produto=request.form["nome_produto"], PRECO=request.form["PRECO"],
                                  cat_produtos=str(request.form["cat_produtos"]))

            print(form_evento)
            form_evento.save()
            db_session.close()
            flash("Cadastro realizado com sucesso", "success")
            return redirect(url_for('novo_produto'))

    return render_template('novo_produto.html')


@app.route('/venda')
def venda():
    sql_venda = select(Venda)
    resultado_venda = db_session.execute(sql_venda).scalars().all()
    print(resultado_venda)
    venda = []
    for n in resultado_venda:
        venda.append(n.serialize_venda())
        print(venda[-1])

    return render_template("venda.html", venda=venda)


@app.route('/nova_venda', methods=['GET', 'POST'])
def nova_venda():
    if request.method == 'POST':
        if not request.form["data2"]:
            flash("preencher todos os campos", "erro")
            if not request.form["id_produto2"]:
                flash("preencher todos os campos", "erro")
                if not request.form["id_cliente2"]:
                    flash("preencher todos os campos", "erro")
                    if not request.form["qtd2"]:
                        flash("preencher todos os campos", "erro")

                    return redirect(url_for('venda'))

        else:
            form_evento = Venda(data2=request.form["data2"],
                                id_produto2=request.form["id_produto2"],
                                id_cliente2=request.form["id_cliente2"],
                                qtd2=request.form["qtd2"]
                                )

            print(form_evento)
            form_evento.save()
            db_session.close()
            flash("Cadastro realizado com sucesso", "success")
            return redirect(url_for('nova_venda'))

    return render_template('nova_venda.html')


@app.route('/categoria')
def categoria():
    sql_categoria = select(Categoria)
    resultado_categoria = db_session.execute(sql_categoria).scalars()
    print(resultado_categoria)
    categoria = []
    for n in resultado_categoria:
        categoria.append(n.serialize_categoria())
        print(categoria[-1])

    return render_template("categoria.html",
                           categoria=categoria)


@app.route('/nova_categoria', methods=['GET', 'POST'])
def nova_categoria():
    if request.method == 'POST':
        if not request.form["nome_categoria"]:
            flash("preencher todos os campos", "erro")

            return redirect(url_for('categoria'))

        else:
            form_evento = Categoria(nome_categoria=request.form["nome_categoria"])

            print(form_evento)
            form_evento.save()
            db_session.close()
            flash("Cadastro realizado com sucesso", "success")
            return redirect(url_for('nova_categoria'))

    return render_template('nova_categoria.html')


@app.route('/cliente')
def cliente():
    sql_cliente = select(Cliente)
    resultado_cliente = db_session.execute(sql_cliente).scalars()
    print(resultado_cliente)
    cliente = []
    for n in resultado_cliente:
        cliente.append(n.serialize_cliente())
        print(cliente[-1])

    return render_template("cliente.html",
                           cliente=cliente)


@app.route('/novo_cliente', methods=['GET', 'POST'])
def novo_cliente():
    if request.method == 'POST':
        if not request.form["CPF"]:
            flash("preencher todos os campos", "erro")
            if not request.form["Nome2"]:
                flash("preencher todos os campos", "erro")
                if not request.form["telefone"]:
                    flash("preencher todos os campos", "erro")
                    if not request.form["Profissao2"]:
                        flash("preencher todos os campos", "erro")
                        if not request.form["Area2"]:
                            flash("preencher todos os campos", "erro")

                    return redirect(url_for('cliente'))

        else:
            form_evento = Cliente(CPF=request.form["CPF"],
                                  Nome2=request.form["Nome2"], telefone=request.form["telefone"],
                                  Profissao2=request.form["Profissao2"], Area2=request.form["Area2"])

            print(form_evento)
            form_evento.save()
            db_session.close()
            flash("Cadastro realizado com sucesso", "success")
            return redirect(url_for('novo_cliente'))

    return render_template('novo_cliente.html')


if __name__ == '__main__':
    app.run(debug=True)
