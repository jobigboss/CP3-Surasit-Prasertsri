from tkinter import  *
import  math
def BMIClickButton(event):
    BMI = float(testBoxWidth.get())/math.pow(float(testBoxHeight.get())/100,2)
    if BMI >= 30:
        labelResule.configure(text="อ้วนมาก")
        labelDetal.configure(text = "ค่อนข้างอันตราย เพราะเข้าเกณฑ์อ้วนมาก"
                                    " เสี่ยงต่อการเกิดโรคร้ายแรงที่แฝงมากับความอ้วน "
                                    "หากค่า BMI อยู่ในระดับนี้ จะต้องระวังการรับประทาน"
                                    "ไขมัน และควรออกกำลังกายอย่างสม่ำเสมอ "
                                    "และหากเลขยิ่งสูงกว่า 40.0 ยิ่งแสดงถึงความอ้วนที่มากขึ้น")
    elif BMI>=25:
        labelResule.configure(text = "อ้วน")
        labelDetal.configure(text ="")
    elif BMI >= 25:
        labelResule.configure(text="อ้วน")
        labelDetal.configure(text="คุณอ้วนในระดับหนึ่ง ถึงแม้จะไม่ถึงเกณฑ์ที่ถือว่าอ้วนมาก ๆ แต่ก็ยังมีความเสี่ยงต่อการเกิดโรคที่มากับความอ้วนได้เช่นกัน ทั้งโรคเบาหวาน และความดันโลหิตสูง")
    elif BMI >= 23:
        labelResule.configure(text="น้ำหนักเกิน")
        labelDetal.configure(text="พยายามอีกนิดเพื่อลดน้ำหนักให้เข้าสู่ค่ามาตรฐาน"
                                  " เพราะค่า BMI ในช่วงนี้ยังถือว่าเป็นกลุ่มผู้ที่มีความอ้วนอยู่บ้าง "
                                  "แม้จะไม่ถือว่าอ้วน แต่หากประวัติคนในครอบครัวเคยเป็นโรคเบาหวานและความดันโลหิตสูง ก็ถือว่ายังมีความเสี่ยงมากกว่าคนปกติ")
    elif BMI >= 18.6:
        labelResule.configure(text="น้ำหนักปกติ เหมาะสม")
        labelDetal.configure(text="น้ำหนักที่เหมาะสมสำหรับคนไทยคือค่า BMI ระหว่าง 18.5-22.9 "
                                  "จัดอยู่ในเกณฑ์ปกติ ห่างไกลโรคที่เกิดจากความอ้วน และมีความเสี่ยงต่อการเกิดโรคต่าง ๆ "
                                  "น้อยที่สุด ควรพยายามรักษาระดับค่า BMI ให้อยู่ในระดับนี้ให้นานที่สุด")
    else:
        labelResule.configure(text="ผอมเกินไป")
        labelDetal.configure(text="น้ำหนักน้อยกว่าปกติก็ไม่ค่อยดี "
                                  "หากคุณสูงมากแต่น้ำหนักน้อยเกินไป"
                                  " อาจเสี่ยงต่อการได้รับสารอาหารไม่เพียงพอหรือได้รับพลังงานไม่เพียงพอ "
                                  "ส่งผลให้ร่างกายอ่อนเพลียง่าย การรับประทานอาหารให้เพียงพอและออกกำลังกายแบบเวทเทรนนิ่งเพื่อเสริมสร้างกล้ามเนื้อ "
                                  "สามารถช่วยเพิ่มค่า BMI ให้อยู่ในเกณฑ์ปกติได้")



MainWindow = Tk()
labelHeight = Label(MainWindow,text = "ส่วนสูง  (Cm.)",font = ("Angsana New",16))
labelHeight.grid(row = 0,column = 0)
testBoxHeight = Entry(MainWindow)
testBoxHeight.grid(row = 0,column = 1)
labelWidth = Label(MainWindow,text = "น้ำหนัก  (Kg.)",font = ("Angsana New",16))
labelWidth.grid(row = 1,column = 0)
testBoxWidth = Entry(MainWindow)
testBoxWidth.grid(row = 1,column = 1)
calculateButton = Button(MainWindow,text = "คำนวณ",font = ("Angsana New",16))
calculateButton.bind("<Button-1>",BMIClickButton)
calculateButton.grid(row =2,column = 0)
labelResule =Label(MainWindow,text = "ผลลัพธ์",font  = ("Angsana New",16))
labelResule.grid(row  = 2,column = 1)
labelDetal = Label(MainWindow,text ="ผลสำรวจบอกว่า",font =("Angsana New",16))
labelDetal.grid(row = 3,column = 1)
MainWindow.mainloop()