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
    turno TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    data_nascimento TEXT NOT NULL
)
''')

# Dados de exemplo
dados = [
    (1, "João", "manhã", 'joao@colegio.com', "senha123", "2010-01-01"),
    (2, "Maria", "tarde", 'maria@colegio.com', "senha456", "2010-02-02"),
    (3, "Pedro", "manhã", 'pedro@colegio.com', "senha789", "2010-03-03"),
    (4, "Ana", "noite", 'ana@colegio.com', "senha101", "2009-04-04"),
    (5, "Lucas", "noite", 'lucas@colegio.com', "senha102", "2009-05-05"),
    (6, "Fernanda", "tarde", 'fernanda@colegio.com', "senha103", "2009-06-06"),
    (7, "Carlos", "manhã", 'carlos@colegio.com', "senha104", "2008-07-07"),
    (8, "Juliana", "tarde", 'juliana@colegio.com', "senha105", "2008-08-08"),
    (9, "Roberto", "noite", 'Roberto@colegio.com', "senha106", "2010-09-09"),
    (10, "Patrícia", "manhã", 'patricia@colegio.com', "senha107", "2007-10-10")
]

cursor.executemany("INSERT OR IGNORE INTO alunos (id, nome, turno, email, senha, data_nascimento) VALUES (?, ?, ?, ?, ?, ?)", dados)

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

cursor.execute('''
CREATE TABLE IF NOT EXISTS avisos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    conteudo TEXT,
    data TEXT
)
''')

conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso em:", caminho_banco)
