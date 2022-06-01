from application.model.entity.produto import Produto
from database import lista_produtos_object


class ProdutoDAO():
    def listar_produtos(self):
        lista_produtos = lista_produtos_object
        return lista_produtos

    def cadastrar_produto(self, produto):
        lista_produtos_object.append(produto)