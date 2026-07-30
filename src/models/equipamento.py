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

    def inserir_equipamento(self, repo):
        return repo.inserir(self)

    def atualizar_equipamento(self, repo):
        return repo.atualizar(self)

    def excluir_equipamento(self, repo):
        return repo.excluir(self.id_equipamento)

    def pesquisar_equipamento(self, repo, id_equipamento):
        return repo.pesquisar(id_equipamento)