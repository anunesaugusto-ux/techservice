from src.database.conexao import conectar


def inserir(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO equipamento (id_cliente, tipo, marca, modelo, numero_serie, data_compra)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (
        equipamento.id_cliente,
        equipamento.tipo,
        equipamento.marca,
        equipamento.modelo,
        equipamento.numero_serie,
        equipamento.data_compra,
    )

    cursor.execute(sql, valores)
    conexao.commit()
    equipamento.id_equipamento = cursor.lastrowid

    cursor.close()
    conexao.close()
    return equipamento


def listar():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_equipamento, id_cliente, tipo, marca, modelo, numero_serie, 
               data_compra, status, created_at, updated_at, deleted_at
        FROM equipamento
        WHERE status = 1
        ORDER BY id_equipamento
    """

    cursor.execute(sql)
    equipamentos = cursor.fetchall()

    cursor.close()
    conexao.close()
    return equipamentos


def pesquisar(id_equipamento):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_equipamento, id_cliente, tipo, marca, modelo, numero_serie, 
               data_compra, status, created_at, updated_at, deleted_at
        FROM equipamento
        WHERE id_equipamento = %s
          AND status = 1
    """

    cursor.execute(sql, (id_equipamento,))
    equipamento = cursor.fetchone()

    cursor.close()
    conexao.close()
    return equipamento


def atualizar(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE equipamento
        SET id_cliente = %s,
            tipo = %s,
            marca = %s,
            modelo = %s,
            numero_serie = %s,
            data_compra = %s,
            updated_at = NOW()
        WHERE id_equipamento = %s
          AND status = 1
    """
    valores = (
        equipamento.id_cliente,
        equipamento.tipo,
        equipamento.marca,
        equipamento.modelo,
        equipamento.numero_serie,
        equipamento.data_compra,
        equipamento.id_equipamento,
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def excluir(id_equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE equipamento
        SET status = 0,
            deleted_at = NOW()
        WHERE id_equipamento = %s
          AND status = 1
    """

    cursor.execute(sql, (id_equipamento,))
    conexao.commit()

    cursor.close()
    conexao.close()