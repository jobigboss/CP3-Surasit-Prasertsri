from tkinter import *
import math
def BMI(event):
    BMISum=(float(TextBoxWidth.get())/math.pow(float(TextBoxHeight.get())/100,2))
    if BMISum >= 30 :
        labelShow.configure(text ="อ้วนมาก")
    elif BMISum >=25 :
        labelShow.configure(text="อ้วน")
    elif BMISum >= 23:
        labelShow.configure(text="น้ำหนักเกิน")
    elif BMISum >= 18.6:
        labelShow.configure(text="น้ำหนักปกติ เหมาะสม")
    else:
        labelShow.configure(text="ผอมเกินไป")

mainWindown = Tk()
labelBMI = Label(mainWindown,text = "BMI Program",font = ("Angsana New ",25),fg = "white",bg = "black").grid(row = 0,column = 0)
labelWidth = Label(mainWindown,text = "Width (Cm.)",font = ("Angsana New",20))
labelWidth.grid(row = 1 ,column = 0)
TextBoxWidth = Entry(mainWindown,text = "น้ำหนัก(Kg.)",font = ('Angsana New',18),fg ="black")
TextBoxWidth.grid(row = 1,column = 1)
labelHeight = Label(mainWindown,text = "Height(Cm.)",font = ("Angsana New",20))
labelHeight.grid(row = 2,column = 0)
TextBoxHeight = Entry(mainWindown,text = "ส่วนสูง(Cm.)",font = ("Angsana New",18),fg = "black")
TextBoxHeight.grid(row = 2,column = 1)
btn_calculate  = Button(mainWindown,text = "คำนวณ BMI",font = ("Angsana New",20),fg ="gold",bg = "black")
btn_calculate.grid(row = 3,column = 0)
btn_calculate.bind("<Button>",BMI)
labelShow = Label(mainWindown,text = "ผลสำรวจบอกว่า",font =("Angsana New",20),fg = "black")
labelShow.grid(row = 3, column = 1)
mainWindown.mainloop()