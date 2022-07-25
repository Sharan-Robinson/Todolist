import time

tasklist = []

class task():
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
        self.created_time = time.localtime()

    def gettitle(self):
        return self.title

    def getdesc(self):
        return self.desc

    def gettime(self):
        return time.strftime('%m/%d/%Y', self.created_time)


def addnewtask():
    title = input("Please enter a title:")
    desc = input("Please enter a description:")

    tasklist.append(task(title, desc))
    return


def showalltasks():
    for n, i in enumerate(tasklist):
        print(f"Task {n + 1}:")
        print(f'Task Name: {i.gettitle()}')
        print(f'Task Description: {i.getdesc()}')
        print(f'Created at {i.gettime()}')
    return

def deletetask():
    if not tasklist:
        print("You have not added any tasks!\n")
        return
    for n,i in enumerate(tasklist):
        print(f"{n + 1}. {i.gettitle}")
    print("Enter the number of the task that you would like to delete:")
    tasknum = int(input())
    for i in tasklist:
        if (tasknum - 1) == tasklist.index(i):
            tasklist.remove(i)


def choices():
    print("\nTodoList - Please choose an option:")
    print("1. Add a task. \n"
          "2. Show all tasks \n"
          "3. Delete a task \n"
          "4. Exit")
    num = input("\nEnter number here:")
    return num


def chose(var):
    num = int(var)
    if num == 1:
        addnewtask()
    elif num == 2:
        showalltasks()
    elif num == 3:
        deletetask()
    elif num == 4:
        exit()
    else:
        print("That's not a valid option, please choose again. ")
        var = choices()
        print(var)
        chose(var)

while True:
    option = choices()
    chose(option)

