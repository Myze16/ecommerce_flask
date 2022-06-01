from crypt import methods
from application import app
from flask import render_template, request
from application.model.dao.produto import ProdutoDAO
from application.model.entity.produto import Produto


@app.route("/")
def inicio():
    lista_produtos = ProdutoDAO().listar_produtos()
    return render_template("index.html", lista=lista_produtos)


@app.route("/cadastro",methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        produto = Produto()
        produto.nome = request.form.get('nome', None)
        produto.preco = request.form.get('preco', None)
        produto.quantidade = request.form.get('quantidade', None)
        produto.foto = request.form.get('foto', None)
        ProdutoDAO().cadastrar_produto(produto)
    return render_template("cadastro.html")
