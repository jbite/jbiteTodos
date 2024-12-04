# import icecream as ic
import os 
def wFile(filename, todos):
    """
    Write todo list to file

    Args:
        filename: define file name to read from
        todos: the todo content to write
    
    """
    with open(filename, 'w') as f:
        f.writelines(todos)

def rFile(filename) -> list:
    """
    write content into file

    Args:
        filename: define file name to read from
    
    Returns:
        list: Return line from filename
    """
    with open(filename, 'r') as f:
        content = f.readlines()

    return content

def addTodo(filename, todo):
    """add todo in todo file

    Args:
        filename (str): the file name which you store todo list
        todo (str): todo 
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    todo = todo + '\n'
    todos = rFile(filename)
    todos.append(todo)
    wFile(filename, todos)

def showTodos(filename) -> list:
    """show todo list and return todos by list

    Args:
        filename (str): the file name which you store todo list
        
    Returns:
        list: returned todo list 
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    todos=rFile(filename)
    for index, item in enumerate(todos):
        print(f"{index + 1}-{item.strip("\n")}")

    return todos


def editTodo(filename):
    """start edit your todo, you need to put the number and new todo.

    Args:
        filename (str): the file name which you store todo list
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    number = int(input("Number of the todo to edit: "))
    number = number - 1
    new_todo = input("Enter new todo: ")
    todos = rFile(filename)
    todos[number] = new_todo + '\n'
    wFile(filename, todos)

def completeTodo(filename):
    """Start complete your todos and choose a number which you finished.

    Args:
        filename (str): the file name which you store todo list
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    todos = showTodos(filename)
    number = int(input("Please choose the complete todo in list: ")) - 1
    todos.pop(number)
    wFile(filename, todos) 