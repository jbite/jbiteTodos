import functions
import FreeSimpleGUI as fsg
import time

# fsg.theme("Dark Amber 5")
clock = fsg.Text('', key='clock')
label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo", key="todo")
add_button = fsg.Button(size=10, image_source="add.png",key="Add",mouseover_colors="LightBlue2",tooltip="Add Todo")
list_box = fsg.Listbox(values=functions.showTodos(),key='todos',
                       enable_events=True,size=[45, 10])
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")


layout = [[label],
          [clock],
          [input_box,add_button],
          [list_box,[edit_button],[complete_button]],
          [exit_button]    
          ]

window = fsg.Window('My To-Do App', 
                    layout=layout, 
                    font=('Helvetica', 20))
while True:
    event, v = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(v)
    match event:
        case 'Add':
            functions.addTodo(todo=v['todo'])
            todos = functions.showTodos()
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = v['todos'][0]
                new_todo = v['todo'] + "\n"
                todos = functions.showTodos()
                todos[todos.index(todo_to_edit)] = new_todo
                functions.wFile(todos=todos)
                window['todos'].update(values=todos)
            except IndexError:
                fsg.popup("Please select an item first.", font=("Helvetica",20))
                print("error")
        case 'todos':
            window['todo'].update(value=v['todos'][0])
        case 'Complete':
            try:
                todo_to_complete = v['todos'][0]
                todos = functions.showTodos()
                print("complete event: ",todo_to_complete)
                todos.pop(todos.index(todo_to_complete))
                functions.wFile(todos=todos)
                window['todos'].update(values=todos)
            except IndexError:
                fsg.popup("Please select an item first.", font=("Helvetica",20))
                print("error")
        case 'Exit':
            break
        case fsg.WIN_CLOSED:
            break
    
window.close()