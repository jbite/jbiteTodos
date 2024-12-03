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

def addTodo(filename):
    todo = input("Enter a todo: ") + '\n'
    todos = rFile(filename)
    todos.append(todo)
    wFile(filename, todos)

def showTodos(filename) -> list:
    """
    
    """
    todos=rFile(filename)
    for index, item in enumerate(todos):
        print(f"{index + 1}-{item.strip("\n")}")

    return todos


def editTodo(filename):
    number = int(input("Number of the todo to edit: "))
    number = number - 1
    new_todo = input("Enter new todo: ")
    todos = rFile(filename)
    todos[number] = new_todo + '\n'
    wFile(filename, todos)

def completeTodo(filename):
    todos = showTodos(filename)
    number = int(input("Please choose the complete todo in list: ")) - 1
    todos.pop(number)
    wFile(filename, todos) 