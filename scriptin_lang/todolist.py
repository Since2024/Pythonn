class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append({"task": task, "completed": False})
        print(f"✓ Added: '{task}'")
    
    def view_tasks(self):
        """Display all tasks with their status"""
        if not self.tasks:
            print("Your to-do list is empty! 🎉")
            return
        
        print("\n" + "="*40)
        print("YOUR TO-DO LIST")
        print("="*40)
        
        for i, task_info in enumerate(self.tasks, 1):
            status = "✓" if task_info["completed"] else "○"
            print(f"{i}. [{status}] {task_info['task']}")
        print("="*40)
    
    def mark_completed(self, task_number):
        """Mark a task as completed"""
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"✓ Marked task #{task_number} as completed!")
        else:
            print("❌ Invalid task number!")
    
    def remove_task(self, task_number):
        """Remove a task from the list"""
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"🗑️ Removed: '{removed_task['task']}'")
        else:
            print("❌ Invalid task number!")
    
    def clear_completed(self):
        """Remove all completed tasks"""
        completed_count = sum(1 for task in self.tasks if task["completed"])
        self.tasks = [task for task in self.tasks if not task["completed"]]
        print(f"🧹 Cleared {completed_count} completed task(s)!")

def main():
    todo = TodoList()
    
    while True:
        print("\n" + "-"*30)
        print("TO-DO LIST MANAGER")
        print("-"*30)
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark task as completed")
        print("4. Remove a task")
        print("5. Clear completed tasks")
        print("6. Exit")
        print("-"*30)
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            task = input("Enter your task: ").strip()
            if task:
                todo.add_task(task)
            else:
                print("❌ Task cannot be empty!")
        
        elif choice == "2":
            todo.view_tasks()
        
        elif choice == "3":
            if not todo.tasks:
                print("Your list is empty! Add some tasks first.")
                continue
            todo.view_tasks()
            try:
                task_num = int(input("Enter task number to mark as completed: "))
                todo.mark_completed(task_num)
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == "4":
            if not todo.tasks:
                print("Your list is empty! Add some tasks first.")
                continue
            todo.view_tasks()
            try:
                task_num = int(input("Enter task number to remove: "))
                todo.remove_task(task_num)
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == "5":
            todo.clear_completed()
        
        elif choice == "6":
            print("👋 Goodbye! Have a productive day!")
            break
        
        else:
            print("❌ Invalid option! Please choose 1-6.")

if __name__ == "__main__":
    main()