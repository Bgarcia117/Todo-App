# from functions import get_todos, write_todos 
import functions
import time 

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

prompt = "Type add, show, edit, complete, or exit:"

while True:
    user_action = input(prompt)
    user_action = user_action.strip()
    # Using the strip method like this allows us to keep the changes to spacings when the variable is called again.

    
    if user_action.startswith("add"):
        todo = user_action[4:]
        # This is a list slice 

        todos = functions.get_todos()
           
        todos.append(todo + '\n')  

        functions.write_todos(todos)
        
    elif user_action.startswith("show"):
    # elif stops the program from checking these blocks of code when it executes one

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]
        # This is a list comprehension. It works like a for & in

        for index, item in enumerate(todos):
        # Enumerate adds counter to each item in the list
        #Use 'for # in #' to display a list without brackets
            # item.capatlize()
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            # print(number) 
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            # Pop removes an item using its index. 

            functions.write_todos(todos)
            
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    # case _:
    #     print("Hey you entered an unknown command.")

