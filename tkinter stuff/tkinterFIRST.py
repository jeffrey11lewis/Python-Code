from tkinter import *
from tkinter import ttk


def changeText():
    ttk.Label(frm, text = "you pressed a button!! YAYYYY").grid(column=0,row=0)

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text = "Press Me!", command=changeText).grid(column=2, row = 0)
root.mainloop()


