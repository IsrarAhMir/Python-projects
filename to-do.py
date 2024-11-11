def main():
    tasks = []
    
    while True:
        print("/n===== TO DO list =====")
        print("1. Add task")
        print("2. Show task")
        print("3. Mark task as done")
        print("4. Exit")

        choice =  input("Enter your choice: ")

        if choice == '1':
            n_tasks = int(input("how many tasks you want to add:"))

            for i in range(n_tasks):
                task = input("Enter the task:")
                tasks.append({"task" : task, "done": False})
                print("Task added!")

        elif  choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "done"  if task["done"] else "not done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif  choice == '3':
            task_index = int(input("Enter the task number you want to mark as done:"))
            if 0 <= task_index - 1 < len(tasks):
                tasks[task_index - 1]["done"] = True
                print("Task marked as done!")
            else:
                print("invalid task")
        
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
if  __name__ == "__main__":
    main()







