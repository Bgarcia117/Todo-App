def get_todos(filepath='todos.txt'):
    """ Reads a text files and returns a list of the items in the file."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
         # This creates a list by reading what is on that file. The benefit of using with and as is that you do not need close the file. (As file_local works like "file =")
    return todos_local

def write_todos(todos_arg, filepath='todos.txt'):
     """ Writes items to the text file."""
     with open(filepath, 'w') as file:
            file.writelines(todos_arg)



if __name__ == "__main__":
     print('hello')
     print(get_todos())