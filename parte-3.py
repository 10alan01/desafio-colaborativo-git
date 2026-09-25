# ==========================================
# DEV 3: Módulo de Clientes
# ==========================================
def modulo_clientes():
    print("\n--- [DEV 3] GESTÃO DE CLIENTES ---")
    nome = input("Nome do cliente: ").strip()
    cpf = input("CPF do cliente: ").strip()
    
    if nome and cpf:
        banco_dados["clientes"].append({"nome": nome, "cpf": cpf})
        print(f"Cliente {nome} cadastrado com sucesso!")
    else:
        print("Dados inválidos!")
