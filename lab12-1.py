def login():
    username = tb1.get()
    password = tb2.get()
    if username == "best" and password == "123456789" :
        messagebox.showinfo("ผลลัพธิ์","ถูกต้อง!")
    else :
        messagebox.showinfo("ผลลัพธิ์","ไม่ถูกต้อง!")

from tkinter import *
window = Tk()
window.geometry("800x500")
window.title("โดยภาสกรณ์ แสนปาง")

lb1 = Label(window,text = "Username :",font = ("Cooper Black",20))
lb1.place(x=50, y=10)
tb1 =Entry(window)
tb1.place(x=250, y=10 , width=200 , height=30)


lb = Label(window,text = "Password:",font = ("Cooper Black",20))
lb.place(x=50, y=50)
tb2 =Entry(window)
tb2.place(x=250, y=50 , width=200 , height=30)

btn = Button(window,text="เข้าสู่ระบบ",font = ("Cooper Black", 17) , command= login)
btn.place(x=260, y=100)