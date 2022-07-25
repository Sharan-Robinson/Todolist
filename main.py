import time
import sqlite3

class task():
    def __init__(self, title, desc, created_time, section):
        self.title = title
        self.desc = desc
        self.created_time = created_time
        self.section = section

    def gettitle(self):
        return self.title

    def getdesc(self):
        return self.desc

    def gettime(self):
        return self.created_time

    def settime(self, time):
        self.created_time = time

    def setsection(self, section):
        self.section = section

    def getsection(self):
        return self.section


tasklist = []
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("""
        CREATE TABLE IF NOT EXISTS main(
        title TEXT, 
        desc TEXT,
        time TEXT,
        section TEXT
        )""")
c.execute("SELECT * FROM main")

taskdata = c.fetchall()

conn.close()

for i in taskdata:
    tasklist.append(task(i[0], i[1], i[2], i[3]))


def connecttodb(tasklist):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    if tasklist:
        for i in tasklist:
            taskinfo = (i.gettitle(), i.getdesc(), i.gettime(), i.getsection())
            c.execute("""
            INSERT INTO main VALUES(
            ?, ? , ?, ?)""", taskinfo)

    c.execute("SELECT * FROM main")
    print(c.fetchall())
    conn.commit()
    conn.close()

def addnewtask(section = 'default'):
    title = input("Please enter a title:")
    desc = input("Please enter a description:")

    tasklist.append(task(title, desc, time.localtime(), section))
    return


def showalltasks():
    for n, i in enumerate(tasklist):
        print(f"Task {n + 1}:")
        print(f'Task Name: {i.gettitle()}')
        print(f'Task Description: {i.getdesc()}')
        print(f'Created at {i.gettime()}')
        if i.getsection() != 'default':
            print(f'Classified Under: {i.getsection()}')
    return


def deletetask():
    if not tasklist:
        print("You have not added any tasks!\n")
        return
    for n, i in enumerate(tasklist):
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


def exittodo():
    connecttodb(tasklist)
    exit()


def chose(var):
    num = int(var)
    if num == 1:
        addnewtask()
    elif num == 2:
        showalltasks()
    elif num == 3:
        deletetask()
    elif num == 4:
         exittodo()
    else:
        print("That's not a valid option, please choose again. ")
        var = choices()
        print(var)
        chose(var)


while (True):
    option = choices()
    chose(option)
