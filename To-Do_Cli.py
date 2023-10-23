
import os
import subprocess

def save_tasks_to_file(filename, tasks):
    try:
        with open(filename, 'w') as file:
            for task in tasks:
                status = "[X]" if task["status"] == "[X]" else "[ ]"
                file.write(f"{status}  {task['title']}\n")
        print(f"Tarefas salvas em {filename}.")
    except Exception as e:
        print(f"Erro ao salvar tarefas: {e}")

def load_tasks_from_file(filename):
    tasks = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('  ', 1)
                if len(parts) == 2:
                    status, title = parts[0], parts[1]
                    task = {"title": title, "status": status}
                    tasks.append(task)
    except FileNotFoundError:
        pass  # Arquivo inexistente, não há tarefas a carregar
    except Exception as e:
        print(f"Erro ao carregar tarefas: {e}")
    return tasks

def list_tasks(tasks):
    if not tasks:
        print("Lista de Tarefas Vazia.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "[X]" if task['status'] == "[X]" else "[ ]"
            print(f"{i}. {status} {task['title']}")

def toggle_task_status(tasks, task_num):
    if 1 <= task_num <= len(tasks):
        task = tasks[task_num - 1]
        if task['status'] == "[X]":
            task['status'] = "[ ]"
            print(f'Tarefa "{task["title"]}" desmarcada como concluída.')
        else:
            task['status'] = "[X]"
            print(f'Tarefa "{task["title"]}" marcada como concluída.')
    else:
        print("Número de tarefa inválido. Nenhuma tarefa foi marcada como concluída.")

def remove_task(tasks, task_num):
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f'Tarefa "{removed_task["title"]}" removida com sucesso.')
    else:
        print("Número de tarefa inválido. Nenhuma tarefa foi removida.")

def main():
    filename = 'tarefas.txt'
    tasks = load_tasks_from_file(filename)
    
    while True:
        print("#################################################################################")
        print("\n")
        print("\n")
        print("      ##############                            #########                      ")
        print("           ##          ###########             ##       ##      ###########   ")
        print("          ##         ##         ##            ##        ##    ##         ##  ")
        print("         ##         ##         ##   ######   ##        ##    ##         ##  ")
        print("        ##         ##         ##            ##        ##    ##         ##  ")
        print("       ##          ###########             ###########      ###########  ")
        print("\nOpções:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar/Desmarcar Tarefa")
        print("4. Remover Tarefa")
        print("5. Sair")
        print("")
        print("")
        print("#################################################################################")
        choice = input("\nEscolha uma opção: ")
        print("")
        
        
        if choice == "1":
            new_task = input("Digite o título da nova tarefa: ")
            tasks.append({'status': '[ ]', 'title': new_task})
            save_tasks_to_file(filename, tasks)
            print(f'Tarefa "{new_task}" adicionada com sucesso.')
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            list_tasks(tasks)
            task_num = int(input("Digite o número da tarefa a ser marcada/desmarcada como concluída: "))
            toggle_task_status(tasks, task_num)
            save_tasks_to_file(filename, tasks)
        elif choice == "4":
            list_tasks(tasks)
            task_num = int(input("Digite o número da tarefa a ser removida: "))
            remove_task(tasks, task_num)
            save_tasks_to_file(filename, tasks)
        elif choice == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
