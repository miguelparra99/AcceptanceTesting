def create_task(description, category, priority, completed=False):
    return {
        "Descripcion": description,
        "Categoria": category,
        "Prioridad": priority,
        "Completado": completed
    }


def add_task(todo_list, task):
    return todo_list + [task]


def list_tasks(todo_list):
    for index, task in enumerate(todo_list, start=1):
        status = "✓" if task["Completado"] else " "
        print(f"{index}. [{status}] {task['Descripcion']} (Categoria: {task['Categoria']}, Prioridad: {task['Prioridad']})")


def mark_task_completed(todo_list, task_index):
    updated_list = todo_list[:]
    if 0 <= task_index < len(updated_list):
        updated_list[task_index]["Completado"] = True
    return updated_list


def clear_todo_list():
    return []


# Adding new feature about editing a Task
def edit_task(todo_list, task_index, new_description, new_priority, new_category):
    updated_list = todo_list[:]
    if 0 <= task_index < len(updated_list):
        updated_list[task_index]["Descripcion"] = new_description
        updated_list[task_index]["Prioridad"] = new_priority
        updated_list[task_index]["Categoria"] = new_category
    return updated_list


def main():
    todo_list = []

    while True:
        print("\nPrograma de lista de actividades")
        print("1. Añadir tarea")
        print("2. Lista de tareas")
        print("3. Marcar tareas como completas")
        print("4. Limpiar lista de actividades")
        print("5. Editar tareas")
        print("6. Salir")

        choice = input("Ingresa tu opcion: ")

        if choice == "1":
            description = input("Ingresa descripcion de tarea: ")
            category = input("Ingresa categoria: ")
            priority = input("Ingresa prioridad: ")
            new_task = create_task(description, category, priority)
            todo_list = add_task(todo_list, new_task)
            print("Tarea añadida.")

        elif choice == "2":
            if todo_list:
                list_tasks(todo_list)
            else:
                print("Tarea no esta en la lista.")

        elif choice == "3":
            if todo_list:
                list_tasks(todo_list)
                task_index = int(input("Ingresa el indice de la tarea a marcar como completa: ")) - 1
                todo_list = mark_task_completed(todo_list, task_index)
                print("Tarea marcada como completa")
            else:
                print("No hay tarea para mostrar")

        elif choice == "4":
            todo_list = clear_todo_list()
            print("Lista de tarea vacia")

        elif choice == "5":
            if todo_list:
                list_tasks(todo_list)
                task_index = int(input("Ingrese el inidice de la tarea a editar: ")) - 1
                new_description = input("Ingresa nueva descripcion de tarea: ")
                new_priority = input("Ingresa nueva prioridad: ")
                new_category = input("Ingresa nueva categoria: ")
                todo_list = edit_task(todo_list, task_index, new_description, new_priority, new_category)
                print("Tarea editada")
            else:
                print("Tarea no esta en la lista")

        elif choice == "6":
            break

