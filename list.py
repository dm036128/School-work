import time as t
import os
todo = ["",""]
num = 1
def do():
    os.system('cls')
    global num, todo
    t.sleep(0.5)
    print("Here is your To-Do list:")
    num = 1
    for i in todo:
        print(str(num)+": "+i)
        num+=1
    num =1
    t.sleep(0.5)
    print("Options.\nChange\t1\nAdd\t2\nRemove\t3")
    inp=input("")
    if inp == "1":
        change()
    elif inp =="2":
        add()
    elif inp =="3":
        remove()
    else:
        do()
def change():
    global todo, num
    os.system('cls')
    t.sleep(0.5)
    print("Here is your To-Do list:")
    for i in todo:
        print(str(num)+": "+i)
        num+=1
    print("What would you like to change?")
    inp = input("")
    todo[int(inp)-1] = input("Change it to?\n")
    do()
def add():
    global todo, num
    os.system('cls')
    t.sleep(0.5)
    print("Add what?")
    inp = input()
    todo.append(inp)
    do()
def remove():
    global todo, num
    t.sleep(0.5)
    print("Remove what?")
    inp=input()
    print("Type the exact text to confirm: ")
    inp = input()
    todo.remove(inp)
    do()
do()
