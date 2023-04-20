prompt = "Enter a todo:"
todos = []

i = 1
while i < 3:
    todo = input(prompt + "\n")
    todos.append(todo.capitalize())
    i += 1

print(todos)
