# ==========================================
# DEV 2: Módulo de Autenticação
# ==========================================
def modulo_autenticacao():
    print("\n--- [DEV 2] AUTENTICAÇÃO DE USUÁRIOS ---")
    usuario = input("Digite o nome do usuário: ").strip()
    if usuario in banco_dados["usuarios"]:
        print(f"Usuário '{usuario}' já existe no sistema.")
    else:
        senha = input("Digite a senha: ").strip()
        banco_dados["usuarios"][usuario] = senha
        print(f"Usuário '{usuario}' cadastrado com sucesso!")
