from datetime import datetime


class OrdemServico:

    def __init__(
        self,
        id_equipamento,
        defeito_relatado,
        prioridade="MEDIA",
        status="ABERTA",
        diagnostico=None,
        solucao=None,
        valor_servico=0.00,
        valor_pecas=0.00,
        desconto=0.00,
        valor_total=0.00,
        observacoes=None,
        status_registo=1,
        id_ordem=None,
    ):
        self.id_ordem = id_ordem
        self.id_equipamento = id_equipamento
        self.data_abertura = datetime.now()
        self.status = status
        self.prioridade = prioridade
        self.defeito_relatado = defeito_relatado
        self.diagnostico = diagnostico
        self.solucao = solucao
        self.valor_servico = valor_servico
        self.valor_pecas = valor_pecas
        self.desconto = desconto
        self.valor_total = valor_total
        self.observacoes = observacoes
        self.status_registo = status_registo

    def abrir_ordem_servico(self, repo):
        return repo.criar(self)

    def alterar_estado_ordem(self, repo, novo_status):
        self.status = novo_status
        return repo.atualizar_status(self.id_ordem, novo_status)

    def listar_ordens_servico(self, repo):
        return repo.listar()