from tkinter import *

root = Tk()
root.title("Radiobutton Example")

radio_var = StringVar()
radio_var.set("Option 1")

def update_label():
    selected_value = radio_var.get()
    label.config(text=f"Selected : {selected_value}")

rb1 = Radiobutton(root,text="CASH",variable=radio_var,value="cash",command=update_label)
rb1.pack(anchor=W)

rb2 = Radiobutton(root,text="CHEQUE",variable=radio_var,value="chaque",command=update_label)
rb2.pack(anchor=W)

rb3 = Radiobutton(root,text="DD",variable=radio_var,value="dd",command=update_label)
rb3.pack(anchor=W)

label=Label(text="")
label.pack()

root.mainloop()
