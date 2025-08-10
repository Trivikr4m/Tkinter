from tkinter import *
root = Tk()
root.title("Label Example")
root.geometry("300x300+400+200")
lbx1 = Label(root,text="Vijayawada",fg='red',bg='yellow',font=('Arial',20,'bold'))
lbx1.pack()
lbx1 = Label(root,text="Trivikram",fg='blue',bg='pink',font=('times new roman',20,'bold'))
lbx1.pack(pady=20)
mainloop()