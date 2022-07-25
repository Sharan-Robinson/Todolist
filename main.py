import time

print("TodoList - Please choose an option:")

class task():
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
        self.created_time = time.localtime()

    def __str__(self):
        pass


tasklist = []

def addnewtask():
    title = input("Please enter a title:")
    desc = input("Please enter a description:")

    tasklist.append(task(title, desc))
    return


def showalltasks():
    pass


def choices():
    print("1. Add a task. \n"
          "2. Show all task \n"
          "3. Exit \n")
    num = input("\nEnter number here:")
    return num


def chose(var):
    num = int(var)
    if num == 1:
        addnewtask()
    elif num == 2:
        showalltasks()
    elif num == 3:
        exit()
    else:
        print("That's not a valid option, please choose again. ")
        var = choices()
        print(var)
        chose(var)


option = choices()
chose(option)

print(tasklist)