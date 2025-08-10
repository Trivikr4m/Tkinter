from tkinter import *
import math
root = Tk()
root.title("Interest Calculator")
root.geometry("450x300")

lbx1 = Label(root,text="Principle Amnt:")
lbx1.grid(row=0,column=0,padx=10,pady=10)
ent1 = Entry(root)
ent1.grid(row=0,column=1,padx=10,pady=10)

lbx2 = Label(root,text="rate of interest:")
lbx2.grid(row=1,column=0,padx=10,pady=10)
ent2 = Entry(root)
ent2.grid(row=1,column=1,padx=10,pady=10)

lbx3 = Label(root,text="Time(in years) :")
lbx3.grid(row=2,column=0,padx=10,pady=10)
ent3 = Entry(root)
ent3.grid(row=2,column=1,padx=10,pady=10)

def si():
    try:
        principle = float(ent1.get())
        rate = float(ent2.get())
        time = float(ent3.get())
        interest = (principle*rate*time)/100 
        lbx_result.config(text=f"Interest :{interest:.2f}")
    except ValueError:
        lbx_result.config(text="Please enter a valid number")

def ci():
    try:
        principle = float(ent1.get())
        rate = float(ent2.get())
        time = float(ent3.get())
        amount = principle*(1+rate/100)**time
        interest = amount - principle
        lbx_result.config(text=f"interst:{interest:.2f}")
    except ValueError:
        lbx_result.config(text="Please enter a valid number")

def clear_fields():
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    lbx_result.config(text="")

def quit_app():
    root.quit()

btn_cal = Button(root,text="Calculate interest",command=si)
btn_cal.grid(row=3,column=0,padx=10,pady=10)

btn_cal_ci = Button(root,text="Calculate ci",command=ci)
btn_cal_ci.grid(row=3,column=1,padx=10,pady=10)

btn_clear=Button(root,text="Clear Fields",command=clear_fields)
btn_clear.grid(row=3,column=2,padx=10,pady=10)

btn_quit=Button(root,text="Quit",command=quit_app)
btn_quit.grid(row=3,column=3,padx=10,pady=10)

lbx_result = Label(root,text="")
lbx_result.grid(row=4,columnspan=3,padx=10,pady=10)



mainloop()

