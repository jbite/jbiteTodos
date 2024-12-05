# import icecream as ic
FILENAME = 'todos.txt'
def wFile(filename=FILENAME, todos=[]):
    """
    Write todo list to file

    Args:
        filename: define file name to read from
        todos: the todo content to write
    
    """
    with open(filename, 'w') as f:
        f.writelines(todos)

def rFile(filename=FILENAME) -> list:
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

def addTodo(filename=FILENAME, todo=''):
    """add todo in todo file

    Args:
        filename (str): the file name which you store todo list
        todo (str): todo 
    """

    todo = todo + '\n'
    todos = rFile(filename)
    todos.append(todo)
    wFile(filename, todos)

def showTodos(filename=FILENAME) -> list:
    """show todo list and return todos by list

    Args:
        filename (str): the file name which you store todo list
        
    Returns:
        list: returned todo list 
    """

    todos=rFile(filename=FILENAME)
    for index, item in enumerate(todos):
        print(f"{index + 1}-{item.strip("\n")}")

    return todos


def editTodo(filename=FILENAME):
    """start edit your todo, you need to put the number and new todo.

    Args:
        filename (str): the file name which you store todo list
    """

    number = int(input("Number of the todo to edit: "))
    number = number - 1
    new_todo = input("Enter new todo: ")
    todos = rFile(filename=FILENAME)
    todos[number] = new_todo + '\n'
    wFile(filename=FILENAME, todos=todos)

def completeTodo(filename=FILENAME):
    """Start complete your todos and choose a number which you finished.

    Args:
        filename (str): the file name which you store todo list
    """

    todos = showTodos(filename=FILENAME)
    number = int(input("Please choose the complete todo in list: ")) - 1
    todos.pop(number)
    wFile(filename=FILENAME, todos=todos) 