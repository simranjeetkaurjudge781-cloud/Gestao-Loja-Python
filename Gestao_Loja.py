# Gestão de Loja - Projeto Python

# FASE 3: Funções Obrigatórias (Uso de 'def')
def mostrar_estatisticas(inventario):
    """FASE 4: Funcionalidade Extra - Estatísticas"""
    if not inventario:
        print("\nInventário vazio. Sem estatísticas.")
        return
    
    total_itens = sum(item['quantidade'] for item in inventario)
    valor_total = sum(item['preco'] * item['quantidade'] for item in inventario)
    print(f"\n--- ESTATÍSTICAS ---")
    print(f"Total de produtos diferentes: {len(inventario)}")
    print(f"Quantidade total em stock: {total_itens}")
    print(f"Valor total do inventário: {valor_total:.2f}€")

def procurar_produto(inventario, nome_procura):
    for item in inventario:
        if item['nome'].lower() == nome_procura.lower():
            return item
    return None

# FASE 2: Estrutura Base
def menu():
    loja = [] # FASE 3: Lista de Dicionários
    
    while True: # FASE 2: Ciclo While
        print("\n=== GESTÃO DE LOJA ===")
        print("1 – Adicionar Produto")
        print("2 – Listar Todos")
        print("3 – Procurar Produto")
        print("4 – Remover Produto")
        print("5 – Ver Estatísticas (Extra)")
        print("0 – Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            qtd = int(input("Quantidade: "))
            loja.append({"nome": nome, "preco": preco, "quantidade": qtd})
            print("Produto adicionado com sucesso!")

        elif opcao == "2":
            print("\n--- LISTA DE PRODUTOS ---")
            for i, item in enumerate(loja):
                print(f"{i}. {item['nome']} | Preço: {item['preco']}€ | Qtd: {item['quantidade']}")

        elif opcao == "3":
            nome_busca = input("Nome do produto a procurar: ")
            resultado = procurar_produto(loja, nome_busca)
            if resultado:
                print(f"Encontrado: {resultado['nome']} - Stock: {resultado['quantidade']}")
            else:
                print("Produto não encontrado.")

        elif opcao == "4":
            nome_remov = input("Nome do produto a remover: ")
            produto = procurar_produto(loja, nome_remov)
            if produto:
                loja.remove(produto)
                print("Produto removido!")
            else:
                print("Produto não encontrado.")

        elif opcao == "5":
            mostrar_estatisticas(loja)

        elif opcao == "0":
            print("A encerrar o programa...")
            break # FASE 2: Opção sair
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
