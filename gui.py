import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text("", key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
# Tooltip displays text when hovering over the input box
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", 
                      enable_events=True, size=[45,10])
                    # Size is width by hieght
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App', 
                   layout=[[clock],
                           [label], 
                           [input_box, add_button], 
                           [list_box, edit_button, complete_button],
                           [exit_button]], 
                   font=('Helvetica', 20))
# Adds the labels to the window and each list in 'layout' represents a row.

while True:
    event, values = window.read(timeout=200)
    # runs the time every 200 miliseconds
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            # This gets the value from the dictionary using the key and adds a break like for the user.
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            # Updates the list to display the new value. .update works on the Listbox

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                # When a todo is clicked, it appears in the terminal with its labels
                new_todo = values['todo']
                # These are using the keys to get the values that were stored in the input box and list

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                # Gets the index of the todo_to_edit in the list
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                # Updates the value that is replaced in the list. .update works on the Listbox
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                # .remove() is a list method
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                # Replaces the items with the new updated list
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
            

        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])
            # Updates the inputbox to display what is clicked on. 

        case sg.WIN_CLOSED:
            break
    
window.close()