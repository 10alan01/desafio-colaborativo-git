# ==========================================
# DEV 5: Módulo de Vendas
# ==========================================
def modulo_vendas():
    print("\n--- [DEV 5] MÓDULO DE VENDAS ---")
    modulo_produtos()
    try:
        cod = int(input("\nCódigo do produto para venda: "))
        if cod in banco_dados["produtos"]:
            qtd = int(input("Quantidade: "))
            prod = banco_dados["produtos"][cod]
            if prod["estoque"] >= qtd:
                prod["estoque"] -= qtd
                total = qtd * prod["preco"]
                banco_dados["vendas"].append({"produto": prod["nome"], "qtd": qtd, "total": total})
                print(f"Venda realizada! Total: R$ {total:.2f}")
            else:
                print("Estoque insuficiente!")
        else:
            print("Produto não encontrado!")
    except ValueError:
        print("Entrada inválida!")
