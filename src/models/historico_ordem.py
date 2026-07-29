from datetime import datetime


class HistoricoOrdem:

    def __init__(
        self,
        id_ordem,
        status_novo,
        status_anterior=None,
        observacao=None,
        usuario="Sistema",
        id_historico=None,
    ):
        self.id_historico = id_historico
        self.id_ordem = id_ordem
        self.status_anterior = status_anterior
        self.status_novo = status_novo
        self.observacao = observacao
        self.data_alteracao = datetime.now()
        self.usuario = usuario

    def consultar_historico_ordem(self, repo, id_ordem):
        return repo.listar_por_ordem(id_ordem)