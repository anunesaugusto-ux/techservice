class Equipamento:

    def __init__(
        self,
        id_cliente,
        tipo,
        marca,
        modelo,
        numero_serie,
        data_compra=None,
        status=1,
        id_equipamento=None,
    ):
        self.id_equipamento = id_equipamento
        self.id_cliente = id_cliente
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.data_compra = data_compra
        self.status = status

    def criar_equipamento(self, repo):
        return repo.criar(self)

    def editar_equipamento(self, repo):
        return repo.atualizar(self)