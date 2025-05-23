import os

def load_tasks():
    if not os.path.exists("tasks.txt"):
        return []
    with open("tasks.txt", "r") as file:
        return file.read().splitlines()

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        file.write("\n".join(tasks))

def show_tasks(tasks):
    if not tasks:
        print("Список дел пуст!")
    else:
        print("Твои задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Добавить задачу\n2. Удалить задачу\n3. Показать задачи\n4. Выйти")
        choice = input("Выбери действие: ")
        
        if choice == "1":
            task = input("Введи задачу: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Задача добавлена!")
        
        elif choice == "2":
            show_tasks(tasks)
            num = int(input("Номер задачи для удаления: ")) - 1
            if 0 <= num < len(tasks):
                tasks.pop(num)
                save_tasks(tasks)
                print("Задача удалена!")
            else:
                print("Неверный номер!")
        
        elif choice == "3":
            show_tasks(tasks)
        
        elif choice == "4":
            break
        
        else:
            print("Неверный ввод!")

if __name__ == "__main__":
    main()
