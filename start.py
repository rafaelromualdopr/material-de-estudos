import subprocess
import time
import os

# Função para abrir o Google Chrome com perfis/contas diferentes
def open_chrome_with_accounts():
    # Caminho para o executável do Chrome
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    # Lista de URLs ou perfis a serem abertos
    profiles = [
        r'--profile-directory="Profile 1"', #Perfil Trabalho
        r'--profile-directory="Profile 4"', # Pesquisa/ IA
        r'--profile-directory="Default"',   # Perfil Padrão
    ]

    for profile in profiles:
        command = f'"{chrome_path}" {profile}'
        subprocess.Popen(command, shell=True)
        time.sleep(3)  # Tempo para o Chrome carregar

# Função para iniciar o n8n localmente
def start_n8n():
    # Comando do ngrok
    ngrok_command = (
        "ngrok http --url=https://bold-collie-greatly.ngrok-free.app 5678"
    )
    # Comando do n8n
    webhook_command = (
        'set WEBHOOK_URL=https://bold-collie-greatly.ngrok-free.app&&start n8n'
    )

    # Executa o comando ngrok
    subprocess.Popen(ngrok_command, shell=True)
    time.sleep(5)  # Espera para garantir que o ngrok esteja funcionando

    # Executa o comando do n8n
    subprocess.Popen(webhook_command, shell=True)

# Função principal
def main():
    print("Iniciando rotina...")

    # Abrir Google Chrome com perfis/contas diferentes
    open_chrome_with_accounts()

    # Iniciar n8n localmente
    start_n8n()

    print("Rotina concluída.")

if __name__ == "__main__":
    main()
