import os
tasklist=[]
def Add_task():
    print("\t\tENTER THE TASK")
    t=input("\t:-")
    tasklist.append(t)
    print("\n\t\tTasks added succesfully.")
    
def View_task():
    i=1
    print("\n\t-----Task List-----\n") 
    if not tasklist:
        print("\t(No tasks available)")
    else:
        for e in tasklist:
            print("\t",i,". ",e,sep='')
            i+=1
        
def Delete_task():
    View_task()
    if tasklist:
        try:
            t=int(input("\n\tEnter the task number to delete: "))
            if not (1 <= t <= len(tasklist)):
                print("\tInvalid task number!")
            else:  
                os.system("cls")  
                del  tasklist[t-1]
                print("\n\tTask number ",t,"has been deleted.")
                View_task()
        except ValueError:
            print("\tEnter number only.")  
def Save_task():
    if len(tasklist):
        file=open("task.txt",'w')
        for e in tasklist:
            file.write(e)
            file.write("\n")
        file.close()  
        print("\n\tSave all task in file.")
    else:
        print("\n\tNo tasks available to save")     
        
def Load_task():
    tasklist.clear()
    try:
        file=open("task.txt",'r')
        t_task=file.read()
        for e in t_task.split("\n"):
            tasklist.append(e)
        del tasklist[-1]    
        file.close()  
        if tasklist:
            print("\n\t",len(tasklist),"tasks added successfully.")     
    except FileNotFoundError:
        print("\n\t\tFile doesn't exists!")  
    except IndexError:
        print("\n\tNot any task available to load!")            
                                   
Load_task()        
while True:
    os.system("cls")
    print("\n\t\t**MENU**\n")
    print("\t1. Add tasks")
    print("\t2. View tasks")
    print("\t3. Delete tasks")
    print("\t4. Save and Load")
    print("\t5. Exit")
    
    ch=input("\n\tEnter your choice: ")
    os.system("cls")
    match ch:
        case "1":
            Add_task()
            input("\n\tPress Enter to return to HOME")
        case "2":
            View_task()
            input("\n\tPress Enter to return to HOME")
        case "3":
            Delete_task()
            input("\n\tPress Enter to return to HOME")
        case "4":
            Save_task()
            input("\n\tPress Enter to return to HOME")
        case "5":
            input("\n\tPress Enter to EXIT\n\n")
            exit()
        case _:
            print("\n\tEnter the valid option!") 
            input("\n\t\tPress Enter to return to HOME")   
                        
