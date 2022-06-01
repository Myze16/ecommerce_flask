class Produto():
    def __init__(self):
        self._id = None
        self._nome = None
        self._preco = None
        self._quantidade = None
        self._foto = None

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, new_nome):
        self._nome = new_nome

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, new_preco):
        self._preco = new_preco

    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, new_quantidade):
        self._quantidade = new_quantidade

    @property
    def foto(self):
        return self._foto
    
    @foto.setter
    def foto(self, new_foto):
        self._foto = new_foto
