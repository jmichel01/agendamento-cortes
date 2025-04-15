from app.database import conectar

def salvar_agendamento(nome, servico, data):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO agendamentos (nome, servico, data) VALUES (%s, %s, %s)", (nome, servico, data))
    conn.commit()
    conn.close()

def listar_agendamentos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agendamentos ORDER BY data")
    agendamentos = cursor.fetchall()
    conn.close()
    return agendamentos
