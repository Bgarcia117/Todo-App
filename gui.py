import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
# Tooltip displays text when hovering over the input box
add_button = sg.Button("Add")



window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
# Adds the labels to the window and each list in 'layout' represents a row.
window.read()
# displays the window
window.close()