import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from app.agenda import salvar_agendamento, listar_agendamentos

def agendar():
    nome = nome_entry.get()
    servico = servico_entry.get()
    data = data_entry.get_date()

    if nome and servico:
        salvar_agendamento(nome, servico, data)
        messagebox.showinfo("Sucesso", "Agendamento realizado com sucesso!")
        nome_entry.delete(0, tk.END)
        servico_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Preencha todos os campos.")

def mostrar_agendamentos():
    agendamentos = listar_agendamentos()
    agendamentos_text.delete(1.0, tk.END)
    for ag in agendamentos:
        agendamentos_text.insert(tk.END, f"{ag[1]} - {ag[2]} - {ag[3]}\n")

# Interface
root = tk.Tk()
root.title("Agenda de Cortes de Cabelo")
root.geometry("400x500")

tk.Label(root, text="Nome do Cliente:").pack()
nome_entry = tk.Entry(root)
nome_entry.pack()

tk.Label(root, text="Serviço (ex: corte, barba):").pack()
servico_entry = tk.Entry(root)
servico_entry.pack()

tk.Label(root, text="Data do Agendamento:").pack()
data_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, locale='pt_BR')
data_entry.pack()

tk.Button(root, text="Agendar", command=agendar).pack(pady=10)
tk.Button(root, text="Mostrar Agendamentos", command=mostrar_agendamentos).pack()

agendamentos_text = tk.Text(root, height=15, width=50)
agendamentos_text.pack(pady=10)

root.mainloop()
