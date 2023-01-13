prompt = "Type add, show, edit, complete, or exit:"

while True:
    user_action = input(prompt)
    user_action = user_action.strip()
    # Using the strip method like this allows us to keep the changes to spacings when the variable is called again.

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            # "/n" is a breakline

            file = open('Files/todos.txt', 'r')
            todos = file.readlines()
            # This creates a list by reading what is on that file 
            file.close()

            todos.append(todo) 

            file = open('Files/todos.txt', 'w')
            # Adding 'w' means write while 'r' means read.
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
        # This is a bitwise or operator

            file = open('Files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip('\n') for item in todos]
            # This is a list comprehension. It works like a for & in

            for index, item in enumerate(todos):
            # Enumerate adds counter to each item in the list
            #Use 'for # in #' to display a list without brackets
                # item.capatlize()
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Enter the number of the todo item to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Enter the number of the todo item to complete: "))
            todos.pop(number - 1)
            # Pop removes an item using its index. 

        case 'exit':
            break
        # case _:
        #     print("Hey you entered an unknown command.")

