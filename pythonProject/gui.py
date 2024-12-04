import functions
import FreeSimpleGUI as fsg
FILENAME = 'todos.txt'
label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo", key="todo")
add_button = fsg.Button("Add")

layout = [[label], [input_box,add_button]]

window = fsg.Window('My To-Do App', 
                    layout=layout, 
                    font=('Helvetica', 20))
while True:
    event, v = window.read()
    print(event)
    print(v)
    match event:
        case 'Add':
            functions.addTodo(filename=FILENAME, todo=v['todo'])
        case fsg.WIN_CLOSED:
            break
    
window.close()