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
    (4, "Ana", "primeiro ano", 'ana@colegio.com', "senha101", "2010-04-04"),
    (5, "Lucas", "primeiro ano", 'lucas@colegio.com', "senha102", "2010-05-05"),
    (6, "Fernanda", "primeiro ano", 'fernanda@colegio.com', "senha103", "2010-06-06"),
    (7, "Carlos", "primeiro ano", 'carlos@colegio.com', "senha104", "2010-07-07"),
    (8, "Juliana", "primeiro ano", 'juliana@colegio.com', "senha105", "2010-08-08"),
    (9, "Roberto", "primeiro ano", 'Roberto@colegio.com', "senha106", "2010-09-09"),
    (10, "Patrícia", "primeiro ano", 'patricia@colegio.com', "senha107", "2010-10-10"),
    (11, "Bruno", "segundo ano", 'bruno@colegio.com', "senha201", "2009-01-11"),
    (12, "Camila", "segundo ano", 'camila@colegio.com', "senha202", "2009-02-12"),
    (13, "Eduardo", "segundo ano", 'eduardo@colegio.com', "senha203", "2009-03-13"),
    (14, "Larissa", "segundo ano", 'larissa@colegio.com', "senha204", "2009-04-14"),
    (15, "Thiago", "segundo ano", 'thiago@colegio.com', "senha205", "2009-05-15"),
    (16, "Beatriz", "segundo ano", 'beatriz@colegio.com', "senha206", "2009-06-16"),
    (17, "André", "segundo ano", 'andre@colegio.com', "senha207", "2009-07-17"),
    (18, "Natália", "segundo ano", 'natalia@colegio.com', "senha208", "2009-08-18"),
    (19, "Vinícius", "segundo ano", 'vinicius@colegio.com', "senha209", "2009-09-19"),
    (20, "Renata", "segundo ano", 'renata@colegio.com', "senha210", "2009-10-20"),
    (21, "Gustavo", "terceiro ano", 'gustavo@colegio.com', "senha301", "2008-01-21"),
    (22, "Isabela", "terceiro ano", 'isabela@colegio.com', "senha302", "2008-02-22"),
    (23, "Felipe", "terceiro ano", 'felipe@colegio.com', "senha303", "2008-03-23"),
    (24, "Tatiane", "terceiro ano", 'tatiane@colegio.com', "senha304", "2008-04-24"),
    (25, "Marcelo", "terceiro ano", 'marcelo@colegio.com', "senha305", "2008-05-25"),
    (26, "Aline", "terceiro ano", 'aline@colegio.com', "senha306", "2008-06-26"),
    (27, "Rafael", "terceiro ano", 'rafael@colegio.com', "senha307", "2008-07-27"),
    (28, "Débora", "terceiro ano", 'debora@colegio.com', "senha308", "2008-08-28"),
    (29, "Henrique", "terceiro ano", 'henrique@colegio.com', "senha309", "2008-09-29"),
    (30, "Sabrina", "terceiro ano", 'sabrina@colegio.com', "senha310", "2008-10-30")
]

cursor.executemany("INSERT OR IGNORE INTO alunos (id, nome, turma, email, senha, data_nascimento) VALUES (?, ?, ?, ?, ?, ?)", dados)


cursor.execute('''
CREATE TABLE IF NOT EXISTS avaliacoes (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 nota REAL NOT NULL,
 disciplina TEXT NOT NULL,
 aluno_id INTEGER NOT NULL,
 aprovacao TEXT CHECK(aprovacao IN ('Aprovado', 'Reprovado', 'Em Recuperação')) NOT NULL DEFAULT 'Em Recuperação',
 FOREIGN KEY (aluno_id) REFERENCES alunos(id)
)
''')


import random

disciplinas = [
     "Língua Portuguesa", "Matemática", "História", "Geografia",
     "Física", "Química", "Biologia", "Educação Física",
     "Arte", "Língua Estrangeira Moderna (Inglês)"
 ]

cursor.execute('''
CREATE TABLE IF NOT EXISTS faltas (
id INTEGER PRIMARY KEY AUTOINCREMENT,
data DATE  NOT NULL,
aluno_id INTEGER NOT NULL,
FOREIGN KEY (aluno_id) REFERENCES alunos(id)
)
''')

for aluno_id in range(1, 31): # IDs dos alunos de 1 a 30
    for disciplina in disciplinas:
        nota = round(random.uniform(0.0, 10.0), 1) # nota entre 0.0 e 10.0
        if nota >=7.0:
            aprovacao = 'Aprovado'
        else:  
            aprovacao = 'Reprovado'
            
        cursor.execute('''
 INSERT INTO avaliacoes (aluno_id, disciplina, nota, aprovacao)
 VALUES (?, ?, ?, ?)
 ''', (aluno_id, disciplina, nota, aprovacao))
        
    

#Gerando notas aleatórias para cada disciplina


from datetime import datetime, timedelta 

#datetime para trabalhar com datas e horas
#timedelta para representar uma diferença de tempo (ex: adicionar dias a uma data)

for _ in range(100):
 aluno_id = random.randint(1, 30) # IDs de 1 a 30
 dias_aleatorios = random.randint(0, 200)
 data = datetime(2025, 3, 1) + timedelta(days=dias_aleatorios)
 data_formatada = data.strftime('%Y-%m-%d')

 cursor.execute('''
 INSERT INTO faltas (data, aluno_id)
 VALUES (?, ?)
 ''', (data_formatada, aluno_id))




conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso em:", caminho_banco)
