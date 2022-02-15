from tkinter import *
window = Tk()
window.geometry("800x500")
window.title("โดย ภาสกรณ์ แสนปาง")
lb = Label(window , text="ยินดีต้อนรับเข้าสู่ pyton", font=("Tahoma",24))
lb.place(x=50, y=10)
lb2 =Label(window,text= "รับค่ารัศมี",font=("Cooper Black",18))
lb2.place(x=50, y=80)

tb1 =Entry()
tb1.place(x=160, y=90)


lb3 =Label(window,text = "ผลลัพธ์",font = ("Cooper Black",18))
lb3.place(x=50, y=120)
tb2 =Entry()
tb2.place(x=160, y=130)