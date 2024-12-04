import functions as fun
import time
filename = 'todos.txt'
while True:
    print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
    user_action = input("Type add, show, edit or exit with your todo item: ")
    
    if user_action.startswith("add"):
        todo = user_action = user_action[4:]
        fun.addTodo(filename, todo)
    elif user_action.startswith("show"):
        fun.showTodos(filename)
    elif user_action.startswith("edit"):
        fun.editTodo(filename)
    elif user_action.startswith("complete"):
        fun.completeTodo(filename)
    elif user_action.startswith("exit"):
        break