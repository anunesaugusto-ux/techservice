from src.models.cliente import Cliente
from src.models.equipamento import Equipamento
from src.models.ordem_servico import OrdemServico

# Repositório do Cliente
from src.repositories.cliente_repository import (
    inserir as inserir_cliente_db,
    listar as listar_clientes_db,
    pesquisar as pesquisar_cliente_db,
    atualizar as atualizar_cliente_db,
    excluir as excluir_cliente_db,
)

# Repositório do Equipamento
from src.repositories.equipamento_repository import (
    inserir as inserir_equipamento_db,
    listar as listar_equipamentos_db,
    pesquisar as pesquisar_equipamento_db,
    atualizar as atualizar_equipamento_db,
    excluir as excluir_equipamento_db,
)

# Repositório da Ordem de Serviço
from src.repositories.ordem_servico_repository import (
    inserir as inserir_os_db,
    listar as listar_os_db,
    pesquisar as pesquisar_os_db,
    atualizar as atualizar_os_db,
    excluir as excluir_os_db,
)

while True:
    print("\n===== MENU TECHSERVICE =====")
    print("1. Gestão de Clientes")
    print("2. Gestão de Equipamentos")
    print("3. Gestão de Ordens de Serviço")
    print("0 - Sair")

    escolha_principal = input("Escolha uma opção: ")

    if escolha_principal == "1":
        while True:
            print("\n--- MENU CLIENTE ---")
            print("1. Criar Cliente")
            print("2. Listar Clientes")
            print("3. Pesquisar Cliente")
            print("4. Editar Cliente")
            print("5. Remover Cliente")
            print("0 - Voltar ao Menu Principal")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("\n--- CRIAR CLIENTE ---")
                nome = input("Nome: ")
                email = input("Email: ")
                telefone = input("Telefone: ")
                nif = input("NIF: ")
                morada = input("Morada: ")

                cliente = Cliente(
                    nome=nome, email=email, telefone=telefone, nif=nif, morada=morada
                )
                inserir_cliente_db(cliente)
                print(f"Cliente criado com sucesso! ID atribuído: {cliente.id_cliente}")

            elif opcao == "2":
                print("\n--- LISTA DE CLIENTES ---")
                clientes = listar_clientes_db()
                if not clientes:
                    print("Nenhum cliente encontrado.")
                else:
                    for c in clientes:
                        print(
                            f"ID: {c['id_cliente']} | Nome: {c['nome']} | Email: {c['email']} | NIF: {c['nif']} | Telefone: {c['telefone']} | Morada: {c['morada']}"
                        )

            elif opcao == "3":
                print("\n--- PESQUISAR CLIENTE ---")
                id_cliente = int(input("ID do Cliente a pesquisar: "))
                cliente = pesquisar_cliente_db(id_cliente)
                if cliente:
                    print(f"\nCliente Encontrado:")
                    print(f"Nome: {cliente['nome']}")
                    print(f"Email: {cliente['email']}")
                    print(f"Telefone: {cliente['telefone']}")
                    print(f"NIF: {cliente['nif']}")
                    print(f"Morada: {cliente['morada']}")
                else:
                    print("Cliente não encontrado.")

            elif opcao == "4":
                print("\n--- EDITAR CLIENTE ---")
                id_cliente = int(input("ID do Cliente a editar: "))

                existente = pesquisar_cliente_db(id_cliente)
                if not existente:
                    print("Cliente não encontrado.")
                    continue

                nome = input(f"Novo Nome [{existente['nome']}]: ") or existente['nome']
                email = input(f"Novo Email [{existente['email']}]: ") or existente['email']
                telefone = input(f"Novo Telefone [{existente['telefone']}]: ") or existente['telefone']
                nif = input(f"Novo NIF [{existente['nif']}]: ") or existente['nif']
                morada = input(f"Nova Morada [{existente['morada']}]: ") or existente['morada']

                cliente = Cliente(
                    nome=nome,
                    email=email,
                    telefone=telefone,
                    nif=nif,
                    morada=morada,
                    id_cliente=id_cliente,
                )
                atualizar_cliente_db(cliente)
                print("Cliente atualizado com sucesso!")

            elif opcao == "5":
                print("\n--- REMOVER CLIENTE ---")
                id_cliente = int(input("ID do Cliente a remover: "))
                excluir_cliente_db(id_cliente)
                print("Cliente removido com sucesso!")

            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    elif escolha_principal == "2":
        while True:
            print("\n--- MENU EQUIPAMENTO ---")
            print("1. Criar Equipamento")
            print("2. Listar Equipamentos")
            print("3. Pesquisar Equipamento")
            print("4. Editar Equipamento")
            print("5. Remover Equipamento")
            print("0 - Voltar ao Menu Principal")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("\n--- CRIAR EQUIPAMENTO ---")
                id_cliente = int(input("ID do Cliente dono do equipamento: "))
                
                # Validação para garantir que o cliente existe
                cliente_existente = pesquisar_cliente_db(id_cliente)
                if not cliente_existente or cliente_existente.get('status_registo', 1) == 0:
                    print("Erro: O cliente não existe.")
                    continue

                tipo = input("Tipo: ")
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                numero_serie = input("Número de Série: ")
                data_compra = input("Data de Compra (AAAA-MM-DD ou deixe vazio): ") or None

                equipamento = Equipamento(
                    id_cliente=id_cliente,
                    tipo=tipo,
                    marca=marca,
                    modelo=modelo,
                    numero_serie=numero_serie,
                    data_compra=data_compra,
                )
                inserir_equipamento_db(equipamento)
                print(f"Equipamento criado com sucesso! ID atribuído: {equipamento.id_equipamento}")

            elif opcao == "2":
                print("\n--- LISTA DE EQUIPAMENTOS ---")
                equipamentos = listar_equipamentos_db()
                if not equipamentos:
                    print("Nenhum equipamento encontrado.")
                else:
                    for e in equipamentos:
                        print(
                            f"ID: {e['id_equipamento']} | Cliente ID: {e['id_cliente']} | Tipo: {e['tipo']} | Marca: {e['marca']} | Modelo: {e['modelo']} | Série: {e['numero_serie']}"
                        )

            elif opcao == "3":
                print("\n--- PESQUISAR EQUIPAMENTO ---")
                id_equipamento = int(input("ID do Equipamento a pesquisar: "))
                e = pesquisar_equipamento_db(id_equipamento)
                if e:
                    print(f"\nEquipamento Encontrado:")
                    print(f"Cliente ID: {e['id_cliente']}")
                    print(f"Tipo: {e['tipo']}")
                    print(f"Marca: {e['marca']}")
                    print(f"Modelo: {e['modelo']}")
                    print(f"Número de Série: {e['numero_serie']}")
                    print(f"Data de Compra: {e['data_compra']}")
                else:
                    print("Equipamento não encontrado.")

            elif opcao == "4":
                print("\n--- EDITAR EQUIPAMENTO ---")
                id_equipamento = int(input("ID do Equipamento a editar: "))

                existente = pesquisar_equipamento_db(id_equipamento)
                if not existente:
                    print("Equipamento não encontrado.")
                    continue

                id_cliente = input(f"Novo ID de Cliente [{existente['id_cliente']}]: ") or existente['id_cliente']
                tipo = input(f"Novo Tipo [{existente['tipo']}]: ") or existente['tipo']
                marca = input(f"Nova Marca [{existente['marca']}]: ") or existente['marca']
                modelo = input(f"Novo Modelo [{existente['modelo']}]: ") or existente['modelo']
                numero_serie = input(f"Novo Nº de Série [{existente['numero_serie']}]: ") or existente['numero_serie']
                data_compra = input(f"Nova Data de Compra [{existente['data_compra']}]: ") or existente['data_compra']

                equipamento = Equipamento(
                    id_cliente=int(id_cliente),
                    tipo=tipo,
                    marca=marca,
                    modelo=modelo,
                    numero_serie=numero_serie,
                    data_compra=data_compra,
                    id_equipamento=id_equipamento,
                )
                atualizar_equipamento_db(equipamento)
                print("Equipamento atualizado com sucesso!")

            elif opcao == "5":
                print("\n--- REMOVER EQUIPAMENTO ---")
                id_equipamento = int(input("ID do Equipamento a remover: "))
                excluir_equipamento_db(id_equipamento)
                print("Equipamento removido com sucesso!")

            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    elif escolha_principal == "3":
        while True:
            print("\n--- MENU ORDEM DE SERVIÇO ---")
            print("1. Criar Ordem de Serviço")
            print("2. Listar Ordens de Serviço")
            print("3. Pesquisar Ordem de Serviço")
            print("4. Editar Ordem de Serviço")
            print("5. Remover Ordem de Serviço")
            print("0 - Voltar ao Menu Principal")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("\n--- CRIAR ORDEM DE SERVIÇO ---")
                id_equipamento = int(input("ID do Equipamento: "))
                
                # Validação para garantir que o equipamento existe
                equipamento_existente = pesquisar_equipamento_db(id_equipamento)
                if not equipamento_existente or equipamento_existente.get('status_registo', 1) == 0:
                    print("Erro: O equipamento não existe.")
                    continue

                defeito_relatado = input("Defeito Relatado: ")
                prioridade = input("Prioridade (BAIXA / MEDIA / ALTA) [MEDIA]: ") or "MEDIA"
                status = input("Status (ABERTA / EM ANDAMENTO / AGUARDANDO PECAS / CONCLUIDA) [ABERTA]: ") or "ABERTA"
                
                diagnostico = input("Diagnóstico: ") or None
                solucao = input("Solução: ") or None
                
                valor_servico = float(input("Valor do Serviço [0.00]: ") or 0.00)
                valor_pecas = float(input("Valor das Peças [0.00]: ") or 0.00)
                desconto_percentagem = float(input("Desconto em percentagem (ex: 10 para 10%) [0.00]: ") or 0.00)
                
                # Cálculo automático do total
                subtotal = valor_servico + valor_pecas
                desconto = subtotal * (desconto_percentagem / 100)
                valor_total = subtotal - desconto
                
                observacoes = input("Observações: ") or None

                os_obj = OrdemServico(
                    id_equipamento=id_equipamento,
                    defeito_relatado=defeito_relatado,
                    prioridade=prioridade,
                    status=status,
                    diagnostico=diagnostico,
                    solucao=solucao,
                    valor_servico=valor_servico,
                    valor_pecas=valor_pecas,
                    desconto=desconto,
                    valor_total=valor_total,
                    observacoes=observacoes
                )
                inserir_os_db(os_obj)
                print(f"Ordem de Serviço criada com sucesso! ID atribuído: {os_obj.id_ordem} | Valor Total: {valor_total:.2f}€")

            elif opcao == "2":
                print("\n--- LISTA DE ORDENS DE SERVIÇO ---")
                ordens = listar_os_db()
                if not ordens:
                    print("Nenhuma ordem de serviço encontrada.")
                else:
                    for o in ordens:
                        print(
                            f"ID OS: {o['id_ordem']} | Cliente ID: {o['id_cliente']} | Equipamento ID: {o['id_equipamento']} | Status: {o['status']} | Prioridade: {o['prioridade']} | Defeito: {o['defeito_relatado']}"
                        )

            elif opcao == "3":
                print("\n--- PESQUISAR ORDEM DE SERVIÇO ---")
                id_ordem = int(input("ID da Ordem de Serviço a pesquisar: "))
                o = pesquisar_os_db(id_ordem)
                if o:
                    print(f"\nOrdem de Serviço Encontrada:")
                    print(f"Cliente ID: {o['id_cliente']}")
                    print(f"Equipamento ID: {o['id_equipamento']}")
                    print(f"Data Abertura: {o['data_abertura']}")
                    print(f"Status: {o['status']}")
                    print(f"Prioridade: {o['prioridade']}")
                    print(f"Defeito Relatado: {o['defeito_relatado']}")
                    print(f"Diagnóstico: {o['diagnostico']}")
                    print(f"Solução: {o['solucao']}")
                    print(f"Valor Serviço: {o['valor_servico']}€")
                    print(f"Valor Peças: {o['valor_pecas']}€")
                    print(f"Desconto (Valor): {o['desconto']}€")
                    print(f"Valor Total: {o['valor_total']}€")
                    print(f"Observações: {o['observacoes']}")
                else:
                    print("Ordem de serviço não encontrada.")

            elif opcao == "4":
                print("\n--- EDITAR ORDEM DE SERVIÇO ---")
                id_ordem = int(input("ID da Ordem de Serviço a editar: "))

                existente = pesquisar_os_db(id_ordem)
                if not existente:
                    print("Ordem de serviço não encontrada.")
                    continue

                status = input(f"Novo Status [{existente['status']}]: ") or existente['status']
                prioridade = input(f"Nova Prioridade [{existente['prioridade']}]: ") or existente['prioridade']
                defeito_relatado = input(f"Novo Defeito Relatado [{existente['defeito_relatado']}]: ") or existente['defeito_relatado']
                diagnostico = input(f"Novo Diagnóstico [{existente['diagnostico']}]: ") or existente['diagnostico']
                solucao = input(f"Nova Solução [{existente['solucao']}]: ") or existente['solucao']
                
                valor_servico = float(input(f"Novo Valor Serviço [{existente['valor_servico']}]: ") or existente['valor_servico'])
                valor_pecas = float(input(f"Novo Valor Peças [{existente['valor_pecas']}]: ") or existente['valor_pecas'])
                
                desconto_percentagem_atual = 0.0
                subtotal_existente = existente['valor_servico'] + existente['valor_pecas']
                if subtotal_existente > 0:
                    desconto_percentagem_atual = (existente['desconto'] / subtotal_existente) * 100

                desconto_percentagem = float(input(f"Novo Desconto em percentagem [{desconto_percentagem_atual:.1f}%]: ") or desconto_percentagem_atual)
                
                # Cálculo automático do total na edição
                subtotal = valor_servico + valor_pecas
                desconto = subtotal * (desconto_percentagem / 100)
                valor_total = subtotal - desconto

                observacoes = input(f"Novas Observações [{existente['observacoes']}]: ") or existente['observacoes']

                os_obj = OrdemServico(
                    id_equipamento=existente['id_equipamento'],
                    defeito_relatado=defeito_relatado,
                    prioridade=prioridade,
                    status=status,
                    diagnostico=diagnostico,
                    solucao=solucao,
                    valor_servico=valor_servico,
                    valor_pecas=valor_pecas,
                    desconto=desconto,
                    valor_total=valor_total,
                    observacoes=observacoes,
                    id_ordem=id_ordem,
                )
                atualizar_os_db(os_obj)
                print(f"Ordem de Serviço atualizada com sucesso! Novo Total: {valor_total:.2f}€")

            elif opcao == "5":
                print("\n--- REMOVER ORDEM DE SERVIÇO ---")
                id_ordem = int(input("ID da Ordem de Serviço a remover: "))
                excluir_os_db(id_ordem)
                print("Ordem de Serviço removida com sucesso!")

            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    elif escolha_principal == "0":
        print("Aplicação encerrada.")
        break

    else:
        print("Opção inválida!")