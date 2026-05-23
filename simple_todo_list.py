#create empty list to store task
tasks=[]
Choice=0
#loop execution
while Choice !=3:

#Display menu
    print("==== TO DO LIST =======")
    print("1.Add task\n2. View task\n3. Exit")
#ask user to  choose option
    Choice=input("Ente choice: ")
#option for add
    if Choice == "1":
        task=input("Enter task: ")
        tasks.append(task)
        print("Task added succesiful")
    elif Choice == "2":
        if len(tasks)==0:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
#display all tasks
            for i in range(len(tasks)):
                print(i+1,".", tasks[i])
#choice for exit program
    elif Choice == "3":
        print("program eited")
        break
    else:
        print("Invalid choice")