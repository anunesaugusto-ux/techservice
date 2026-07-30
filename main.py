from src.models.cliente import Cliente
from src.repositories.cliente_repository import (
    inserir,
    listar,
    pesquisar,
    atualizar,
    excluir,
)

while True:
    print("\n===== MENU CLIENTE =====")
    print("1. Criar Cliente")
    print("2. Listar Clientes")
    print("3. Pesquisar Cliente")
    print("4. Editar Cliente")
    print("5. Remover Cliente")
    print("0 - Sair")

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
        inserir(cliente)
        print(f"Cliente criado com sucesso! ID atribuído: {cliente.id_cliente}")

    elif opcao == "2":
        print("\n--- LISTA DE CLIENTES ---")
        clientes = listar()
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
        cliente = pesquisar(id_cliente)
        if cliente:
            print(f"\nCliente Encontrado:")
            print(f"Nome: {cliente['nome']}")
            print(f"Email: {cliente['email']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"NIF: {cliente['nif']}")
            print(f"Morada: {cliente['morada']}")
        else:
            print("Cliente não encontrado ou inativo.")

    elif opcao == "4":
        print("\n--- EDITAR CLIENTE ---")
        id_cliente = int(input("ID do Cliente a editar: "))
        

        existente = pesquisar(id_cliente)
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
        atualizar(cliente)
        print("Cliente atualizado com sucesso!")

    elif opcao == "5":
        print("\n--- REMOVER CLIENTE ---")
        id_cliente = int(input("ID do Cliente a remover: "))
        excluir(id_cliente)
        print("Cliente removido (inativado) com sucesso!")

    elif opcao == "0":
        print("Menu encerrado.")
        break

    else:
        print("Opção inválida!")