import sqlite3
import os

# Caminho para o banco de dados
caminho_banco = os.path.join('database_ic', 'meu_banco.db')
os.makedirs('database_ic', exist_ok=True)

# Conecta (ou cria) o banco de dados
conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

# Cria a tabela de alunos
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    turma TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    data_nascimento TEXT NOT NULL
)
''')

# Dados de exemplo
dados = [
    (1, "João", "primeiro ano", 'joao@colegio.com', "senha123", "2010-01-01"),
    (2, "Maria", "primeiro ano", 'maria@colegio.com', "senha456", "2010-02-02"),
    (3, "Pedro", "primeiro ano", 'pedro@colegio.com', "senha789", "2010-03-03"),
    (4, "Ana", "segundo ano", 'ana@colegio.com', "senha101", "2009-04-04"),
    (5, "Lucas", "segundo ano", 'lucas@colegio.com', "senha102", "2009-05-05"),
    (6, "Fernanda", "segundo ano", 'fernanda@colegio.com', "senha103", "2009-06-06"),
    (7, "Carlos", "terceiro ano", 'carlos@colegio.com', "senha104", "2008-07-07"),
    (8, "Juliana", "terceiro ano", 'juliana@colegio.com', "senha105", "2008-08-08"),
    (9, "Roberto", "primeiro ano", 'Roberto@colegio.com', "senha106", "2010-09-09"),
    (10, "Patrícia", "terceiro ano", 'patricia@colegio.com', "senha107", "2007-10-10")
]

cursor.executemany("INSERT OR IGNORE INTO alunos (id, nome, turma, email, senha, data_nascimento) VALUES (?, ?, ?, ?, ?, ?)", dados)

# Cria as outras tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS boletins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER,
    disciplina TEXT,
    nota REAL,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
)
''')





cursor.execute('''
CREATE TABLE IF NOT EXISTS frequencias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER,
    data TEXT,
    presente BOOLEAN,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
)
''')

conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso em:", caminho_banco)
