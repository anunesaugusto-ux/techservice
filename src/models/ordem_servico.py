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
        id_cliente=None,  
        data_abertura=None,
        status_registo=1,
        id_ordem=None,
    ):
        self.id_ordem = id_ordem
        self.id_equipamento = id_equipamento
        self.id_cliente = id_cliente
        self.data_abertura = data_abertura if data_abertura else datetime.now()
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

    def inserir_ordem(self, repo):
        return repo.inserir(self)

    def atualizar_ordem(self, repo):
        return repo.atualizar(self)

    def excluir_ordem(self, repo):
        return repo.excluir(self.id_ordem)

    def pesquisar_ordem(self, repo, id_ordem):
        return repo.pesquisar(id_ordem)