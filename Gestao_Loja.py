def menu_principal():
    # FASE 3: Dados estruturados por categoria
    # Inicializamos a loja com os itens que você forneceu
    inventario = [
        # 🏠 Household
        {"nome": "Sofa", "categoria": "Household", "preco": 250.00, "quantidade": 5},
        {"nome": "Lamp", "categoria": "Household", "preco": 15.00, "quantidade": 20},
        # 🍎 Fruits
        {"nome": "Apple", "categoria": "Fruits", "preco": 0.50, "quantidade": 100},
        {"nome": "Watermelon", "categoria": "Fruits", "preco": 3.00, "quantidade": 10},
        # 🍔 Foods
        {"nome": "Rice", "categoria": "Foods", "preco": 1.20, "quantidade": 50},
        {"nome": "Pasta", "categoria": "Foods", "preco": 0.90, "quantidade": 40},
        # 🛁 Bathing
        {"nome": "Soap", "categoria": "Bathing", "preco": 1.10, "quantidade": 80},
        {"nome": "Shampoo", "categoria": "Bathing", "preco": 4.50, "quantidade": 30},
        # 🧹 Cleaning
        {"nome": "Detergent", "categoria": "Cleaning", "preco": 2.80, "quantidade": 25},
        {"nome": "Broom", "categoria": "Cleaning", "preco": 5.00, "quantidade": 12}
    ]

    while True:
        print("\n" + "="*30)
        print("     GESTÃO DE LOJA V1.0")
        print("="*30)
        print("1 – Adicionar")
        print("2 – Listar")
        print("3 – Procurar")
        print("4 – Remover")
        print("0 – Sair")
        
        opcao = input("\nSelecione uma opção: ")

        if opcao == "1":
            print("\n--- ADICIONAR NOVO ITEM ---")
            nome = input("Nome do item: ")
            cat = input("Categoria (ex: Foods, Cleaning): ")
            preco = float(input("Preço: "))
            qtd = int(input("Quantidade: "))
            inventario.append({"nome": nome, "categoria": cat, "preco": preco, "quantidade": qtd})
            print(f"✅ {nome} adicionado com sucesso!")

        elif opcao == "2":
            print("\n--- 📦 INVENTÁRIO COMPLETO ---")
            print(f"{'Produto':<15} | {'Categoria':<12} | {'Preço':<8} | {'Qtd'}")
            print("-" * 50)
            for p in inventario:
                print(f"{p['nome']:<15} | {p['categoria']:<12} | {p['preco']:>6.2f}€ | {p['quantidade']}")

        elif opcao == "3":
            print("\n--- 🔍 PROCURAR ---")
            busca = input("O que deseja procurar? ").lower()
            encontrado = False
            for p in inventario:
                if busca in p['nome'].lower() or busca in p['categoria'].lower():
                    print(f"📍 {p['nome']} ({p['categoria']}) - Stock: {p['quantidade']}")
                    encontrado = True
            if not encontrado:
                print("❌ Item não encontrado.")

        elif opcao == "4":
            print("\n--- 🗑️ REMOVER ---")
            remover = input("Nome do item para remover: ").lower()
            for p in inventario:
                if p['nome'].lower() == remover:
                    inventario.remove(p)
                    print(f"✅ {p['nome']} removido!")
                    break
            else:
                print("❌ Produto não encontrado.")

        elif opcao == "0":
            print("Encerrando... Volte sempre!")
            break
        else:
            print("⚠️ Opção Inválida.")

if __name__ == "__main__":
    menu_principal()
