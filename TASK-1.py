class to_do:
    def _init_(self):
        self.todo=dict()
        self.completed_list=dict()
    def add(self,item,priority):
        self.todo[item]=priority
        print("Task added successfully")
    def mark_as_completed(self,task):
        try:
            priority=self.todo.pop(task)
            self.completed_list[task]=priority
            print(f"Congrats! You've successfully completed the task {task}|Priority: {priority}")
        except KeyError:
            print("Oops! task not in the To-Do list")
    def delete_task(self,task):
        if task in self.todo:
            try:
                popped=self.todo.pop(task)
                print(f"Task {task} of priority:{popped} removed successfully from To-Do list!")
            except KeyError:
                print("Oops! the specified task is not in the list")
        else:
            try:
                popped=self.completed_list.pop(task)
                print(f"Task {task} of priority:{popped} removed successfully from completed list!")
            except KeyError:
                print("Oops! the specified task is not in the list")
    def displaytodo(self):
        print("Pending Tasks on To-Do List")
        for index,(val,priority) in enumerate(self.todo.items()):
            print(f"{index+1}:{val}|Priority:{priority}")
        print("Tasks To-Do:",len(self.todo))
    def displaycompleted(self):
        print("Completed Tasks")
        for index,(val,priority) in enumerate(self.completed_list.items()):
            print(f"{index+1}:{val}|priority:{priority}")
        print("Tasks completed:",len(self.completed_list))
todo=to_do()
while True:
    print()
    print("""TO-DO MENU""")
    print("1.Add task")
    print("2.Mark a task as done")
    print("3.Delete a task")
    print("4.To-Do list")
    print("5.Completed Tasks")
    print("0.Exit")
    choice=int(input("Enter a choice:"))
    if choice==1:
        task=input("Task you need to add:").strip()
        priority=int(input("Enter Priority level (1-Low/2-Medium/3.High):"))
        while priority<1 or priority>3:
            print("Invalid Input! Please try again")
            priority=int(input("Enter Priority level (1-Low/2-Medium/3.High):"))
        priority_map={1:"Low",2:"Medium",3:"High"}
        priority_text=priority_map[priority]
        todo.add(task,priority_text)
    elif choice==2:
        element=input("Task that you completed:").strip()
        try:
            todo.mark_as_completed(element)
        except ValueError:
            print("Oops! Item not in the list")
        
    elif choice==3:
        element=input("Enter task name to delete:")
        todo.delete_task(element)
    elif choice==4:
        todo.displaytodo()
    elif choice==5:
        todo.displaycompleted()
    elif choice==0:
        print("exiting program")
        break
