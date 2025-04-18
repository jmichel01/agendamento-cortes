import sqlite3  # ou outro banco de dados, dependendo da escolha do seu time
from datetime import datetime

# Função para inicializar o banco de dados
def inicializar_banco():
    conn = sqlite3.connect('agenda.db')  # Banco de dados local
    c = conn.cursor()

    # Criação da tabela se não existir
    c.execute('''
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        servico TEXT NOT NULL,
        data_hora TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

# Função para salvar um agendamento
def salvar_agendamento(nome, servico, data_hora):
    conn = sqlite3.connect('agenda.db')
    c = conn.cursor()

    # Inserção dos dados no banco de dados
    c.execute('''
    INSERT INTO agendamentos (nome, servico, data_hora)
    VALUES (?, ?, ?)
    ''', (nome, servico, data_hora))

    conn.commit()
    conn.close()

# Função para listar os agendamentos
def listar_agendamentos():
    conn = sqlite3.connect('agenda.db')
    c = conn.cursor()

    c.execute('SELECT nome, servico, data_hora FROM agendamentos ORDER BY data_hora ASC')
    agendamentos = c.fetchall()

    conn.close()

    return agendamentos
