from tkinter import *
import random
import string


root = Tk()
root.geometry("400x280")
root.resizable(FALSE,FALSE)
root.title("Random Password Generator")

title = StringVar()
label = Label(root, textvariable=title).pack()
title.set(" Strength of our password : ")


def selection():
    selection = choice.get()


choice = IntVar()
R1 = Radiobutton(root, text="WEAK", variable=choice, value=1,
                 command=selection).pack(anchor=CENTER)
R2 = Radiobutton(root, text="NORMAL", variable=choice,
                 value=2, command=selection).pack(anchor=CENTER)
R3 = Radiobutton(root, text="STRONG", variable=choice,
                 value=3, command=selection).pack(anchor=CENTER)

labelchoice = Label(root)
labelchoice.pack()


lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(root, textvariable=lenlabel).pack()


var = IntVar()
spinlenght = Spinbox(root, from_=8, to_=24, textvariable=var, width=13).pack()


def callback():
    lsum.config(text=passgen())


passgenButton = Button(root, text="Generate Password",
                       bd=5, height=2, command=callback, pady=3)
passgenButton.pack()
password = str(callback)


lsum = Label(root, text="")
lsum.pack(side=BOTTOM)


weak = string.ascii_uppercase + string.ascii_lowercase
normal = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
strong = weak + normal + symbols


def passgen():
    if choice.get() == 1:
        return "".join(random.sample(weak, var.get()))

    elif choice.get() == 2:
        return "".join(random.sample(normal, var.get()))
    elif choice.get() == 3:
        return "".join(random.sample(strong, var.get()))


root.mainloop()
