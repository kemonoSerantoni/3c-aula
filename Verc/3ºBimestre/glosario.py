import random

def enviar_alerta(status, texto):
    """
    Função para enviar um alerta com base no status e no texto fornecidos.
    
    Args:
        status (str): O status da mensagem (sucesso ou erro).
        texto (str): O texto da mensagem.
    """
    print("")
    if status == "sucesso":
        print("✅ --- ALERTA DE SUCESSO ---")
        print("   Mensagem: ", texto)
        print("   Status: ", status)
        print("   Detalhes: Build concluído com sucesso.")
        print("-------------------------------")
    else:
        print("❌ --- ALERTA DE ERRO ---")
        print("   Mensagem: ", texto)
        print("   Status: ", status)
        print("   Detalhes: Erro ao executar o build.")
        print("-------------------------------")

def executar_build():
    """
    Função para simular a execução de um build.
    
    Retorna:
        bool: True se o build for um sucesso, False se falhar.
    """
    resultado = random.randint(1, 2)
    if resultado == 1:
        return True
    else:
        return False

def main():
    build_sucesso = executar_build()

    if build_sucesso:
        enviar_alerta("sucesso","O build da versão 1.2.0 foi concluído.")
    else:
        enviar_alerta("erro", "O build falhou no commit 'a3b1c9'.")

if __name__ == "__main__":
    main()