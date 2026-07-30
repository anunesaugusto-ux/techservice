class Cliente:

    def __init__(
        self,
        nome,
        email,
        telefone=None,
        nif=None,
        morada=None,
        id_cliente=None,
        status=1,
    ):
        self.id_cliente = id_cliente
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nif = nif
        self.morada = morada
        self.status = status

    def inserir_cliente(self, repo):
        return repo.inserir(self)

    def editar_cliente(self, repo):
        return repo.atualizar(self)

    def excluir_cliente(self, repo):
        return repo.excluir(self.id_cliente)

    def pesquisar_cliente(self, repo, id_cliente):
        return repo.pesquisar(id_cliente)