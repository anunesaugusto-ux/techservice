from src.database.conexao import conectar


def inserir(historico):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO historico_ordem_servico 
        (id_ordem, status_anterior, status_novo, observacao, data_alteracao, usuario) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (
        historico.id_ordem,
        historico.status_anterior,
        historico.status_novo,
        historico.observacao,
        historico.data_alteracao,
        historico.usuario
    )

    cursor.execute(sql, valores)
    conexao.commit()
    historico.id_historico = cursor.lastrowid

    cursor.close()
    conexao.close()
    return historico


def atualizar(historico):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE historico_ordem_servico 
        SET id_ordem = %s, 
            status_anterior = %s, 
            status_novo = %s, 
            observacao = %s, 
            data_alteracao = %s, 
            usuario = %s
        WHERE id_historico = %s
    """
    valores = (
        historico.id_ordem,
        historico.status_anterior,
        historico.status_novo,
        historico.observacao,
        historico.data_alteracao,
        historico.usuario,
        historico.id_historico
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def listar_por_ordem(id_ordem):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_historico, id_ordem, status_anterior, status_novo, observacao, data_alteracao, usuario 
        FROM historico_ordem_servico 
        WHERE id_ordem = %s 
        ORDER BY data_alteracao DESC
    """

    cursor.execute(sql, (id_ordem,))
    historico = cursor.fetchall()

    cursor.close()
    conexao.close()
    return historico