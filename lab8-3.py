from tkinter import *
main = Tk()
main.geometry("800x600")
main.title("โปรแกรมหาพื้นที่สามเหลี่ยม โดย ภาสกรณ์ แสนปาง")
base= StringVar()
high= StringVar()
area= StringVar()

lb1 = Label(main, text="รับค่าฐาน: ", font = ("Cooper Blac", 18))
lb1.place(x=10,y=20)
tb1 =Entry(main, textvariable= base)
tb1.place(x=120, y=30, width=200, height=30)

lb2 =Labal(main, text="")
    