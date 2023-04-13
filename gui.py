import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
# Tooltip displays text when hovering over the input box
add_button = sg.Button("Add")



window = sg.Window('My To-Do App', 
                   layout=[[label], [input_box, add_button]], 
                   font=('Helvetica', 20))
# Adds the labels to the window and each list in 'layout' represents a row.
while True:
    event, values = window.read()
# displays the window
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            # This gets the value from the dictionary using the key and adds a break like for the user.
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
    
window.close()