from src.database.conexao import conectar


def inserir(ordem_servico):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO ordem_de_servico (
            id_equipamento, status, prioridade, defeito_relatado,
            diagnostico, solucao, valor_servico, valor_pecas,
            desconto, valor_total, observacoes
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (
        ordem_servico.id_equipamento,
        ordem_servico.status,
        ordem_servico.prioridade,
        ordem_servico.defeito_relatado,
        ordem_servico.diagnostico,
        ordem_servico.solucao,
        ordem_servico.valor_servico,
        ordem_servico.valor_pecas,
        ordem_servico.desconto,
        ordem_servico.valor_total,
        ordem_servico.observacoes,
    )

    cursor.execute(sql, valores)
    conexao.commit()
    ordem_servico.id_ordem = cursor.lastrowid

    cursor.close()
    conexao.close()
    return ordem_servico


def listar():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT os.id_ordem, os.id_equipamento, eq.id_cliente, os.data_abertura,
               os.status, os.prioridade, os.defeito_relatado, os.diagnostico,
               os.solucao, os.valor_servico, os.valor_pecas, os.desconto,
               os.valor_total, os.observacoes, os.status_registo,
               os.created_at, os.updated_at, os.deleted_at
        FROM ordem_de_servico os
        JOIN equipamento eq ON os.id_equipamento = eq.id_equipamento
        WHERE os.status_registo = 1
        ORDER BY os.id_ordem
    """

    cursor.execute(sql)
    ordens = cursor.fetchall()

    cursor.close()
    conexao.close()
    return ordens


def pesquisar(id_ordem):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT os.id_ordem, os.id_equipamento, eq.id_cliente, os.data_abertura,
               os.status, os.prioridade, os.defeito_relatado, os.diagnostico,
               os.solucao, os.valor_servico, os.valor_pecas, os.desconto,
               os.valor_total, os.observacoes, os.status_registo,
               os.created_at, os.updated_at, os.deleted_at
        FROM ordem_de_servico os
        JOIN equipamento eq ON os.id_equipamento = eq.id_equipamento
        WHERE os.id_ordem = %s
          AND os.status_registo = 1
    """

    cursor.execute(sql, (id_ordem,))
    ordem = cursor.fetchone()

    cursor.close()
    conexao.close()
    return ordem


def atualizar(ordem_servico):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE ordem_de_servico
        SET status = %s,
            prioridade = %s,
            defeito_relatado = %s,
            diagnostico = %s,
            solucao = %s,
            valor_servico = %s,
            valor_pecas = %s,
            desconto = %s,
            valor_total = %s,
            observacoes = %s,
            updated_at = NOW()
        WHERE id_ordem = %s
          AND status_registo = 1
    """
    valores = (
        ordem_servico.status,
        ordem_servico.prioridade,
        ordem_servico.defeito_relatado,
        ordem_servico.diagnostico,
        ordem_servico.solucao,
        ordem_servico.valor_servico,
        ordem_servico.valor_pecas,
        ordem_servico.desconto,
        ordem_servico.valor_total,
        ordem_servico.observacoes,
        ordem_servico.id_ordem,
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def excluir(id_ordem):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE ordem_de_servico
        SET status_registo = 0,
            deleted_at = NOW()
        WHERE id_ordem = %s
          AND status_registo = 1
    """

    cursor.execute(sql, (id_ordem,))
    conexao.commit()

    cursor.close()
    conexao.close()