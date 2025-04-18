import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from app.agenda import salvar_agendamento, listar_agendamentos, inicializar_banco
import re  # Para validação do formato de hora

# Inicializa o banco de dados
inicializar_banco()

def validar_hora(hora):
    """Verifica se o horário está no formato HH:MM"""
    return bool(re.match(r"^(?:2[0-3]|[01]?[0-9]):[0-5][0-9]$", hora))

def agendar():
    nome = nome_entry.get().strip()
    servico = servico_entry.get().strip()
    data = data_entry.get_date().strftime("%Y-%m-%d")
    hora = hora_entry.get().strip()

    # Validação para garantir que todos os campos foram preenchidos corretamente
    if nome and servico and hora:
        if not validar_hora(hora):
            messagebox.showwarning("Erro", "O horário deve estar no formato HH:MM (ex: 14:00).")
            return

        data_hora = f"{data} {hora}"
        salvar_agendamento(nome, servico, data_hora)
        
        # Mensagem de sucesso com feedback visual
        mostrar_mensagem(f"Agendamento salvo para {data_hora} com sucesso!", "green")

        nome_entry.delete(0, tk.END)
        servico_entry.delete(0, tk.END)
        hora_entry.delete(0, tk.END)
        mostrar_agendamentos()
    else:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")

def mostrar_agendamentos():
    agendamentos = listar_agendamentos()
    agendamentos_text.config(state="normal")
    agendamentos_text.delete(1.0, tk.END)

    if not agendamentos:
        agendamentos_text.insert(tk.END, "Nenhum agendamento encontrado.\n")
    else:
        for nome, servico, data_hora in agendamentos:
            agendamentos_text.insert(tk.END, f"{data_hora} - {nome} - {servico}\n")
    agendamentos_text.config(state="disabled")

def mostrar_mensagem(texto, cor="green"):
    """Mostra uma mensagem temporária na tela."""
    status_label.config(text=texto, foreground=cor)
    status_label.after(4000, lambda: status_label.config(text=""))  # Esconde após 4 segundos

# Interface
root = tk.Tk()
root.title("Agenda de Cortes de Cabelo")
root.geometry("450x600")
root.resizable(False, False)

# Estilo dos elementos
style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TEntry", padding=6)

# Frame principal
frame = ttk.Frame(root, padding="20")
frame.pack(fill="both", expand=True)

# Título
ttk.Label(frame, text="Agenda de Cortes de Cabelo", font=("Segoe UI", 14, "bold")).pack(pady=10)

# Campos de entrada
ttk.Label(frame, text="Nome do Cliente:").pack(anchor="w")
nome_entry = ttk.Entry(frame, width=40)
nome_entry.pack()

ttk.Label(frame, text="Serviço (ex: corte, barba):").pack(anchor="w", pady=(10, 0))
servico_entry = ttk.Entry(frame, width=40)
servico_entry.pack()

ttk.Label(frame, text="Data do Agendamento:").pack(anchor="w", pady=(10, 0))
data_entry = DateEntry(frame, width=17, background='darkblue', foreground='white', borderwidth=2, locale='pt_BR')
data_entry.pack()

ttk.Label(frame, text="Hora (HH:MM):").pack(anchor="w", pady=(10, 0))
hora_entry = ttk.Entry(frame, width=10)
hora_entry.insert(0, "14:00")
hora_entry.pack()

# Botões de ação
btn_frame = ttk.Frame(frame)
btn_frame.pack(pady=15)

ttk.Button(btn_frame, text="Agendar", command=agendar).pack(side="left", padx=5)
ttk.Button(btn_frame, text="Mostrar Agendamentos", command=mostrar_agendamentos).pack(side="left", padx=5)

# Área de exibição dos agendamentos
agendamentos_text = tk.Text(frame, height=15, width=52, font=("Consolas", 10))
agendamentos_text.pack(pady=10)
agendamentos_text.config(state="disabled")

# Label para exibir mensagens de status temporárias
status_label = ttk.Label(frame, text="", font=("Segoe UI", 10, "italic"))
status_label.pack(pady=5)

# Carrega os agendamentos ao iniciar
mostrar_agendamentos()

root.mainloop()
