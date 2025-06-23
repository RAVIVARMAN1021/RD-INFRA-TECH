class ToDo:
    def __init__(self):
        self.todo = dict()
        self.completed_list = dict()

    def add(self, item, priority):
        self.todo[item] = priority
        print("Task added successfully!")

    def mark_as_completed(self, task):
        if task in self.todo:
            priority = self.todo.pop(task)
            self.completed_list[task] = priority
            print(f"Task '{task}' marked as completed | Priority: {priority}")
        else:
            print("Task not found in the To-Do list.")

    def delete_task(self, task):
        if task in self.todo:
            popped = self.todo.pop(task)
            print(f"Task '{task}' (Priority: {popped}) removed from To-Do list.")
        elif task in self.completed_list:
            popped = self.completed_list.pop(task)
            print(f"Task '{task}' (Priority: {popped}) removed from Completed list.")
        else:
            print("Task not found in any list.")

    def display_todo(self):
        print("\nPending Tasks:")
        if not self.todo:
            print("No pending tasks.")
        else:
            for index, (val, priority) in enumerate(self.todo.items(), start=1):
                print(f"{index}. {val} | Priority: {priority}")
        print(f"Total Pending Tasks: {len(self.todo)}")

    def display_completed(self):
        print("\nCompleted Tasks:")
        if not self.completed_list:
            print("No completed tasks.")
        else:
            for index, (val, priority) in enumerate(self.completed_list.items(), start=1):
                print(f"{index}. {val} | Priority: {priority}")
        print(f"Total Completed Tasks: {len(self.completed_list)}")


# ---- MAIN LOOP ----
todo = ToDo()

while True:
    print("\n====== TO-DO MENU ======")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Delete Task")
    print("4. View To-Do List")
    print("5. View Completed Tasks")
    print("0. Exit")
    print("========================")
    
    try:
        choice = int(input("Enter a choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        task = input("Enter the task you want to add: ").strip()
        try:
            priority = int(input("Enter Priority (1: Low, 2: Medium, 3: High): "))
            while priority not in [1, 2, 3]:
                print("Invalid priority! Try again.")
                priority = int(input("Enter Priority (1: Low, 2: Medium, 3: High): "))
            priority_map = {1: "Low", 2: "Medium", 3: "High"}
            todo.add(task, priority_map[priority])
        except ValueError:
            print("Priority must be a number.")

    elif choice == 2:
        task = input("Enter the task you've completed: ").strip()
        todo.mark_as_completed(task)

    elif choice == 3:
        task = input("Enter the task name to delete: ").strip()
        todo.delete_task(task)

    elif choice == 4:
        todo.display_todo()

    elif choice == 5:
        todo.display_completed()

    elif choice == 0:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid menu choice. Please try again.")
