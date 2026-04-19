import json

DATA_FILE = "todos.json"

def load_todos():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def add_todo():
    todos = load_todos()
    title = input("Enter todo title: ")
    new_id = max([t["id"] for t in todos], default=0) + 1
    todos.append({"id": new_id, "title": title, "completed": False})
    save_todos(todos)
    print(f'Todo "{title}" added!')

def list_todos():
    todos = load_todos()
    if not todos:
        print("No todos found.")
        return
    for t in todos:
        status = "[x]" if t["completed"] else "[ ]"
        print(f'{t["id"]}: {status} {t["title"]}')

def mark_done():
    todos = load_todos()
    todo_id = int(input("Enter todo ID to mark done: "))
    for t in todos:
        if t["id"] == todo_id:
            t["completed"] = True
            save_todos(todos)
            print(f'Todo {todo_id} marked done!')
            return
    print(f'Todo {todo_id} not found.')

def main():
    while True:
        print("\n1. Add todo\n2. List todos\n3. Mark done\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_todo()
        elif choice == "2":
            list_todos()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()


                                
                        