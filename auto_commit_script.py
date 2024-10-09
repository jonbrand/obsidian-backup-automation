import os
import subprocess
from datetime import datetime
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém o caminho do diretório do Obsidian a partir das variáveis de ambiente
obsidian_dir = os.getenv('OBSIDIAN_DIR')

# Verifica se o diretório foi carregado corretamente
if obsidian_dir:
    # Navegue até o diretório do Obsidian
    os.chdir(obsidian_dir)

    # Verifica se há mudanças não commitadas
    status = subprocess.run(['git', 'status', '--porcelain'],
                            capture_output=True, text=True)

    if status.stdout:
        # Adiciona todas as mudanças ao controle de versão
        subprocess.run(['git', 'add', '.'])

        # Cria a mensagem de commit com data e hora
        commit_date = datetime.now().strftime("%Y/%m/%d %H:%M")
        commit_message = f"Backup automático: {commit_date}"

        # Realiza o commit
        subprocess.run(['git', 'commit', '-m', commit_message])

        # Faz o push das mudanças para o repositório remoto
        subprocess.run(['git', 'push', 'origin', 'main'])
    else:
        log_date = datetime.now().strftime("%Y/%m/%d %H:%M")
        log_message = f"Nenhuma mudança detectada: {log_date}"
        print(log_message)
else:
    print("Erro: Caminho do diretório do Obsidian não encontrado. Verifique o arquivo .env.")
