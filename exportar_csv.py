
print("Script iniciado")
import sqlite3
import pandas as pd
import os

# Caminho para o seu banco de dados
caminho_banco = 'meu_banco.db'

# Conectar ao banco
conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

# Criar pasta para os arquivos CSV
os.makedirs('csv_exportados', exist_ok=True)

# Buscar todas as tabelas do banco
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

# Exportar cada tabela para um CSV
for tabela in tabelas:
    nome_tabela = tabela[0]
    df = pd.read_sql_query(f"SELECT * FROM {nome_tabela}", conexao)
    df.to_csv(f"csv_exportados/{nome_tabela}.csv", index=False)
    print(f"Tabela '{nome_tabela}' exportada com sucesso!")

# Fechar conexão
conexao.close()
print("Exportação concluída.")
