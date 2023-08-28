# step1: importing
from tkinter import *
#
# step2: gui interaction
window = Tk()
window.title("*****Digital Calculator*****")
window.geometry('350x450')

label1 = Label(window , text = "                                              <<<Insert Your Values Please?" , bg = "red" , fg = "white")
label2 = Label(window , text = "Calc" , bg = "blue" , fg = "white")
label3 = Label(window , text = "Calc" , bg = "green" , fg = "white")
label4 = Label(window , text = "Calc" , bg = "yellow" , fg = "white")

label1.pack(side = TOP , fill = X , expand = False)
label2.pack(side = LEFT , fill = Y , expand = False)
label3.pack(side = RIGHT , fill = Y , expand = False)
label4.pack(side = BOTTOM , fill = X , expand = False)


# step3: adding inputs

# ENTRY BOX
e = Entry(window , width = 26, borderwidth = 8)
e.place(x = 0, y = 0)


#BUTTONS
def click(num):
    result = e.get()
    e.insert(0, str(result) + str(num))

b = Button(window , text = '1', width = 12 , command = lambda:click(1))
b.place(x = 30 , y = 60)

b = Button(window , text = '2' , width = 12 , command = lambda:click(2))
b.place(x = 125 , y = 60)

b = Button(window , text = '3' , width = 12 , command = lambda:click(3))
b.place(x = 220 , y = 60)

b = Button(window , text = '4' , width = 12 , command = lambda:click(4))
b.place(x = 30 , y = 120)

b = Button(window , text = '5' , width = 12 , command = lambda:click(5))
b.place(x = 125 , y = 120)

b = Button(window , text = '6' , width = 12 , command = lambda:click(6))
b.place(x = 220 , y = 120)

b = Button(window , text = '7' , width = 12 , command = lambda:click(7))
b.place(x = 30 , y = 180)

b = Button(window , text = '8' , width = 12 , command = lambda:click(8))
b.place(x = 125 , y = 180)

b = Button(window , text = '9' , width = 12 , command = lambda:click(9))
b.place(x = 220 , y = 180)

b = Button(window , text = '0' , width = 12 , command = lambda:click(0))
b.place(x = 30 , y = 240)


# OPERATORS:
def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0, END)
b = Button(window , text = '+' , width = 12 , command = add)
b.place(x = 125 , y = 240)

def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0, END)
b = Button(window , text = '-' , width = 12 , command = sub)
b.place(x = 220 , y = 240)

def mult():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, END)
b = Button(window , text = '*' , width = 12 , command = mult)
b.place(x = 30 , y = 300)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0, END)
b = Button(window , text = '/' , width = 12 , command = div)
b.place(x = 125 , y = 300)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, i + int(n2))
    elif math == "subtraction":
        e.insert(0, i - int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))
    elif math == "division":
        e.insert(0, i / int(n2))

b = Button(window , text = '=' , width = 12 , command = equal)
b.place(x = 220 , y = 300)
def clear():
    e.delete(0,END)
b = Button(window , text = 'Clear' , width = 12 , command = clear)
b.place(x = 30 , y = 350)

b = Button(window , text = 'Syed Ahmed' , width = 12)
b.place(x = 220 , y = 380)


#step4: mainloop
mainloop()


