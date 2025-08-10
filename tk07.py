from tkinter import *
root= Tk()
root.geometry("500x500")
root.title("CheckBox Selection")


# def update_list():
#     selected=[text for var,text in zip(vars,texts) if var.get()==1]
#     label.config(text=",".join(selected))


def update_list():
    slected=[]
    for var, text in zip(vars, texts):
        if var.get() == 1:
            slected.append(text)
    label.config(text=",".join(slected))

vars = []
texts = ["DCA","PGDCA" , "PYTHON"]

for text in texts:
    var = IntVar()
    vars.append(var)
    checkbox = Checkbutton(text=text,variable=var,command=update_list)
    checkbox.pack(anchor='w')

label=Label(text="")
label.pack()

root.mainloop()



