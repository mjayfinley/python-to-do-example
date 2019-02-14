def show_menu():
    print("Please make a selection from the following list: ")
    print(" 1. Add a task you would like to do")
    print(" 2. View all tasks")
    print(" 3. Delete a task")
    print(" q. Quit program")


tasks = []


def add_task():
    task_name = input('Enter your task: ')
    task_priority = input("Enter priority (high, medium, low): ")

    task = {
        "title": task_name,
        "priority": task_priority,
    }

    tasks.append(task)


def show_tasks():
    for task in tasks:
        print(f"{tasks.index(task) + 1}. " +
              task.get('title') + ' - ' + task.get('priority'))


def delete_task():
    show_tasks()

    delete_input = int(input(
        'Enter task number you would like to delete: '))

    for task in tasks:
        if delete_input == (tasks.index(task) + 1):
            tasks.remove(task)
        else:
            print('Task does not exist')


user_input = ''

while user_input != 'q':
    show_menu()
    user_input = input("Enter selection: ")

    if user_input == '1':
        add_task()
    elif user_input == '2':
        show_tasks()
    elif user_input == '3':
        delete_task()
