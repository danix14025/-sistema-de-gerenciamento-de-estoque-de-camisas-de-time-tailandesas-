estoque = {}

def adicionar_produto():
    nome = input("Digite o nome da camisa: ")
    quantidade = int(input("Digite a quantidade: "))
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    print(f"{quantidade} unidades de {nome} adicionadas ao estoque.")

def remover_produto():
    nome = input("Digite o nome da camisa para remover: ")
    if nome in estoque:
        quantidade = int(input("Digite a quantidade a remover: "))
        if quantidade >= estoque[nome]:
            del estoque[nome]
            print(f"Todas as unidades de {nome} foram removidas.")
        else:
            estoque[nome] -= quantidade
            print(f"{quantidade} unidades de {nome} removidas.")
    else:
        print("Produto não encontrado no estoque.")

def listar_produtos():
    if estoque:
        print("\nEstoque Atual:")
        for nome, quantidade in estoque.items():
            print(f"{nome}: {quantidade} unidades")
    else:
        print("O estoque está vazio.")

def pesquisar_produto():
    nome = input("Digite o nome da camisa para pesquisar: ")
    if nome in estoque:
        print(f"{nome}: {estoque[nome]} unidades disponíveis.")
    else:
        print("Produto não encontrado no estoque.")

def menu():
    while True:
        print("\n--- Menu de Gerenciamento de Estoque ---")
        print("1 - Adicionar Produto")
        print("2 - Remover Produto")
        print("3 - Listar Produtos")
        print("4 - Pesquisar Produto")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            remover_produto()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            pesquisar_produto()
        elif opcao == "5":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida, tente novamente.")

menu()
