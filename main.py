
lista_de_pacientes = []


def cadastrar_paciente():
    """Função para adicionar um novo paciente."""
    print("\n--- CADASTRO DE PACIENTE ---")
    nome_paciente = input("Digite o nome completo: ").strip()

    while True:
        try:
            idade_input = input("Digite a idade: ")
            idade_paciente = int(idade_input)

            if idade_paciente <= 0:
                print("Idade não pode ser zero ou negativa. Tente novamente.")
                continue

            break

        except ValueError:
            print("ERRO: A idade precisa ser um número, não letras.")

    telefone_paciente = input("Digite o telefone (com DDD): ").strip()


    novo_registro = {
        "nome": nome_paciente,
        "idade": idade_paciente,
        "telefone": telefone_paciente
    }

    lista_de_pacientes.append(novo_registro)
    print("\n[OK] Paciente cadastrado com sucesso!")


def ver_estatisticas():
    """Função para calcular e mostrar os dados da clínica."""
    if len(lista_de_pacientes) == 0:
        print("\nNão há pacientes suficientes para gerar estatísticas.")
        return  # Sai da função

    print("\n--- ESTATÍSTICAS GERAIS ---")

    total_pacientes = len(lista_de_pacientes)
    soma_idades = 0

    paciente_mais_novo = lista_de_pacientes[0]
    paciente_mais_velho = lista_de_pacientes[0]

    for paciente in lista_de_pacientes:
        soma_idades = soma_idades + paciente["idade"]

        if paciente["idade"] < paciente_mais_novo["idade"]:
            paciente_mais_novo = paciente

        if paciente["idade"] > paciente_mais_velho["idade"]:
            paciente_mais_velho = paciente

    idade_media = soma_idades / total_pacientes

    print(f"Total de Pacientes: {total_pacientes}")
    print(f"Idade Média: {idade_media:.2f} anos")
    print("-" * 25)
    print(f"Paciente Mais Novo: {paciente_mais_novo['nome']} ({paciente_mais_novo['idade']} anos)")
    print(f"Paciente Mais Velho: {paciente_mais_velho['nome']} ({paciente_mais_velho['idade']} anos)")
    print("-" * 25)


def buscar_paciente():
    """Função para buscar um paciente pelo nome."""
    if not lista_de_pacientes:
        print("\nLista de pacientes vazia.")
        return

    nome_busca = input("\nDigite o nome (ou parte) do paciente para buscar: ").strip().lower()

    pacientes_encontrados = []

    for paciente in lista_de_pacientes:
        if nome_busca in paciente["nome"].lower():
            pacientes_encontrados.append(paciente)

    if len(pacientes_encontrados) > 0:
        print(f"\n--- PACIENTES ENCONTRADOS ({len(pacientes_encontrados)}) ---")
        for p in pacientes_encontrados:
            print(f"Nome: {p['nome']} | Idade: {p['idade']} | Tel: {p['telefone']}")
    else:
        print(f"\nNenhum paciente encontrado com '{nome_busca}'.")


def listar_todos_os_pacientes():
    """Função para mostrar a lista completa de pacientes."""
    if not lista_de_pacientes:
        print("\nNão há pacientes cadastrados.")
        return

    print("\n--- LISTAGEM COMPLETA ---")

    # Cabeçalho da tabela
    print(f"{'#':<4}{'Nome':<30}{'Idade':<10}{'Telefone':<20}")
    print("-" * 64)

    for i, paciente in enumerate(lista_de_pacientes, 1):
        print(f"{i:<4}{paciente['nome']:<30}{paciente['idade']:<10}{paciente['telefone']:<20}")
    print("-" * 64)


def menu_principal():
    """Função que inicia o programa e controla o fluxo."""

    while True:
        print("\n" + "=" * 5 + " SISTEMA CLÍNICA VIDA+ " + "=" * 5)
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente por nome")
        print("4. Listar todos os pacientes")
        print("5. Sair do programa")
        print("=" * 34)

        opcao = input("Escolha a opção desejada (1 a 5): ")

        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            ver_estatisticas()
        elif opcao == '3':
            buscar_paciente()
        elif opcao == '4':
            listar_todos_os_pacientes()
        elif opcao == '5':
            print("\nEncerrando o Sistema. Até mais!")
            break  # Sai do loop 'while True'
        else:
            print("\nOpção inválida. Digite apenas um número de 1 a 5.")


# Ponto de entrada do programa
if __name__ == "__main__":
    menu_principal()