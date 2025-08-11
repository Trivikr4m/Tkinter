from tkinter import *
import math
root =Tk()
root.title("Marks List")
root.geometry("450x400")

lbx1 = Label(root,text="Name :")
lbx1.grid(row=0,column=0,padx=10,pady=10)
ent1 = Entry(root)
ent1.grid(row=0,column=1,padx=10,pady=10)

lbx2 = Label(root,text="Maths :")
lbx2.grid(row=1,column=0,padx=10,pady=10)
ent2 = Entry(root)
ent2.grid(row=1,column=1,padx=10,pady=10)


lbx3 = Label(root,text="Telugu :")
lbx3.grid(row=2,column=0,padx=10,pady=10)
ent3 = Entry(root)
ent3.grid(row=2,column=1,padx=10,pady=10)

lbx4 = Label(root,text="English :")
lbx4.grid(row=3,column=0,padx=10,pady=10)
ent4 = Entry(root)
ent4.grid(row=3,column=1,padx=10,pady=10)

lbx5 = Label(root,text="hindi :")
lbx5.grid(row=4,column=0,padx=10,pady=10)
ent5 = Entry(root)
ent5.grid(row=4,column=1,padx=10,pady=10)

lbx6 = Label(root,text="Science :")
lbx6.grid(row=5,column=0,padx=10,pady=10)
ent6 = Entry(root)
ent6.grid(row=5,column=1,padx=10,pady=10)

lbx7 = Label(root,text="Social :")
lbx7.grid(row=6,column=0,padx=10,pady=10)
ent7 = Entry(root)
ent7.grid(row=6,column=1,padx=10,pady=10)



def sum():
    maths = int(ent2.get())
    telugu = int(ent3.get())
    english = int(ent4.get())
    hindi = int(ent5.get())
    science = int(ent6.get())
    social = int(ent7.get())
    Total = maths + telugu + english + hindi + science + social
    lbx_result.config(text=f"Total Marks :{Total} ")


def Average():
    maths = int(ent2.get())
    telugu = int(ent3.get())
    english = int(ent4.get())
    hindi = int(ent5.get())
    science = int(ent6.get())
    social = int(ent7.get())
    Total = maths + telugu + english + hindi + science + social
    avg = Total / 6
    lbx_result.config(text=f"Average Marks :{avg:.2f} ")


def Pass():
    maths = int(ent2.get())
    telugu = int(ent3.get())
    english = int(ent4.get())
    hindi = int(ent5.get())
    science = int(ent6.get())
    social = int(ent7.get())
    if(maths >= 35 and telugu >= 35 and hindi >= 35 and science >= 35 and social >35 ):
        lbx_result.config(text="Pass")
    else:
        lbx_result.config(text="Fail")



    


btn_sum = Button(root,text="Total Marks",command=sum)
btn_sum.grid(row=7,column=0,padx=10,pady=10)

btn_avg = Button(root,text="Average",command=Average)
btn_avg.grid(row=7,column=1,padx=10,pady=10)

btn_pass = Button(root,text="Result",command=Pass)
btn_pass.grid(row=7,column=2,padx=10,pady=10)

lbx_result = Label(root,text="")
lbx_result.grid(row=8,column=1,columnspan=3,padx=10,pady=10)



mainloop()