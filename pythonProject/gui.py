import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo", key="todo")
add_button = fsg.Button("Add")
list_box = fsg.Listbox(values=functions.showTodos(),key='todos',
                       enable_events=True,size=[45, 10])
edit_button = fsg.Button("Edit")
layout = [[label], 
          [input_box,add_button],
          [list_box,edit_button]]

window = fsg.Window('My To-Do App', 
                    layout=layout, 
                    font=('Helvetica', 20))
while True:
    event, v = window.read()
    print(event)
    print(v)
    match event:
        case 'Add':
            functions.addTodo(todo=v['todo'])
            todos = functions.showTodos()
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = v['todos'][0]
            new_todo = v['todo'] + "\n"
            todos = functions.showTodos()
            todos[todos.index(todo_to_edit)] = new_todo
            functions.wFile(todos=todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=v['todos'][0])
        case fsg.WIN_CLOSED:
            break
    
window.close()