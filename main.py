prompt = "Type add, show, edit, complete, or exit:"

while True:
    user_action = input(prompt)
    user_action = user_action.strip()
    # Using the strip method like this allows us to keep the changes to spacings when the variable is called again.

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('Files/todos.txt', 'r') as file:
                 todos = file.readlines()
                # This creates a list by reading what is on that file. The benefit of using with and as is that you do not need close the file. (As file is works like "file =")

            todos.append(todo) 

            with open('Files/todos.txt', 'w') as file:
                file.writelines(todos)
            
        case 'show' | 'display':
        # This is a bitwise or operator

            with open('Files/todos.txt', 'r') as file:
                todos = file.readlines()

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

            with open('Files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo

            with open('Files/todos.txt', 'w') as file:
                file.writelines(todos)

        case "complete":
            number = int(input("Enter the number of the todo item to complete: "))

            with open('Files/todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index.strip('\n')]
            todos.pop(number - 1)
            # Pop removes an item using its index. 

            with open('Files/todos.txt', 'w') as file:
                file.writelines(todos)
            
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        case 'exit':
            break
        # case _:
        #     print("Hey you entered an unknown command.")

