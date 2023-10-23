import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
from tkinter.font import Font

tasks = [] 

def add_task():
    global tasks  # Indique que você está usando a variável global tasks
    new_task = entry.get()
    if new_task:
        tasks.append({"status": "[  ]", "title": new_task})
        entry.delete(0, tk.END)
        update_task_list()

def update_task_list():
    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)
    font = Font(size=14)
    for i, task in enumerate(tasks, 1):
        text_widget.insert(tk.END, f"{i}. {task['status']} {task['title']}\n")
    text_widget.config(state=tk.DISABLED)

def toggle_task_status():
    task_num = int(entry.get())
    if 1 <= task_num <= len(tasks):
        task = tasks[task_num - 1]
        if task['status'] == "[X]":
            task['status'] = "[  ]"
        else:
            task['status'] = "[X]"
        entry.delete(0, tk.END)
        update_task_list()

def remove_task():
    task_num = int(entry.get())
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        entry.delete(0, tk.END)
        update_task_list()

def import_tasks():
    global filename, tasks
    filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    tasks = load_tasks_from_file(filename)
    update_task_list()

def export_tasks():
    global filename
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    save_tasks_to_file(filename, tasks)

def save_tasks_to_file(filename, tasks):
    try:
        with open(filename, 'w') as file:
            for task in tasks:
                file.write(f"{task['status']} {task['title']}\n")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar tarefas: {e}")

def load_tasks_from_file(filename):
    tasks = [ ]
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    status = line[0:4]
                    title = line[4:]
                    tasks.append({"status": status, "title": title})
    except FileNotFoundError:
        pass
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar tarefas: {e}")
    return tasks

def clear_and_save_tasks():
    global tasks
    unsaved_tasks = [task for task in tasks if task['status'] == '[  ]']
    if unsaved_tasks:
        if messagebox.askyesno("Aviso", "Existem tarefas não salvas. Deseja salvar antes de limpar?"):
            export_tasks()  # Chama a função export_tasks para salvar as tarefas
    tasks = [task for task in tasks if task['status'] == '[  ]']
    update_task_list()

def on_closing():
    global tasks
    unsaved_tasks = [task for task in tasks if task['status'] == '[  ]']
    if unsaved_tasks:
        if messagebox.askyesno("Aviso", "Existem tarefas não salvas. Deseja salvar antes de sair?"):
            export_tasks()
    app.destroy()

app = tk.Tk()
app.option_add('*Font', 'Arial 12')
app.title("To-Do CLI")
app.state('zoomed')
app.configure(bg="black")

frame = tk.Frame(app, padx=10, pady=10, bg="BLACK")
frame.pack(fill=tk.BOTH, expand=True)

button_frame = tk.Frame(frame, bg="black")
button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

add_button = tk.Button(button_frame, text="Adicionar Tarefa", command=add_task, bg="Gainsboro", fg="black", height=2, width=20, relief=tk.RAISED, borderwidth=5)
add_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

remove_button = tk.Button(button_frame, text="Remover Tarefa", command=remove_task, bg="Gainsboro", fg="black", height=2, width=20, relief=tk.RAISED, borderwidth=5)
remove_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

toggle_button = tk.Button(button_frame, text="Marcar/Desmarcar Tarefa", command=toggle_task_status, bg="Gainsboro", fg="black", height=2, width=20, relief=tk.RAISED, borderwidth=5)
toggle_button.grid(row=0, column=4, padx=5, pady=5, sticky="ew")

import_button = tk.Button(button_frame, text="Abrir", command=import_tasks, bg="Gainsboro", fg="black", height=2, width=17, relief=tk.RAISED, borderwidth=5)
import_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

export_button = tk.Button(button_frame, text="Salvar Como...", command=export_tasks, bg="Gainsboro", fg="black", height=2, width=17, relief=tk.RAISED, borderwidth=5)
export_button.grid(row=0, column=5, padx=5, pady=5, sticky="ew")

clear_save_button = tk.Button(button_frame, text="Limpar", command=clear_and_save_tasks, bg="Gainsboro", fg="black", height=2, width=20, relief=tk.RAISED, borderwidth=5)
clear_save_button.grid(row=0, column=6, padx=5, pady=5, sticky="ew")

exit_button = tk.Button(button_frame, text="Sair", command=on_closing, bg="Gainsboro", fg="black", height=2, width=13, relief=tk.RAISED, borderwidth=5)
exit_button.grid(row=0, column=7, padx=5, pady=5, sticky="ew")

entry = tk.Entry(frame, bg="black", fg="white", width=80, font=("Arial", 14))
entry.grid(row=1, column=0, columnspan=6, padx=10, pady=10, sticky="ew")

text_widget = scrolledtext.ScrolledText(frame, state=tk.DISABLED, wrap=tk.WORD, height=15, bg="black", fg="white")
text_widget.grid(row=2, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

frame.columnconfigure(0, weight=1)
frame.rowconfigure(2, weight=1)

# Crie um rótulo para o rodapé
footer_label = tk.Label(app, text="VERSÃO 2.0\nCopyright © 2023 Todos os direitos reservados", bg="black", fg="white")
footer_label.place(relx=0.5, rely=1.0, anchor="s")

app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()