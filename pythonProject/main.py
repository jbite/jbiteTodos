import icecream as ic
import functions as fun

filename = 'todos.txt'
while True:
    user_action = input("Type add,  show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            fun.addTodo(filename)
        case 'show':
            fun.showTodos(filename)
        case 'edit':
            fun.editTodo(filename)
        case 'complete':
            fun.completeTodo(filename)
        case 'exit':
            break