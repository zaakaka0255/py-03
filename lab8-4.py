from tkinter  import *
main = Tk()
main.geometry("800x600")
main.title("โปรแกรมเช็คเกรด โดย ภาสกรณ์ แสนปาง")
answer = StringVar()

lb1 =Label(main, text="คะแนนเก็บ: ", font = ("Cooper Black", 14))
lb1.place(x=10,y=20)
tb1 = Entry(main)
tb1.place(x=190, y=20, width= 150, height=30)

lb2 =Label(main, text="คะแนนกลางภาค: ", font = ("Cooper Black", 14))
lb2.place(x=10,y=60)
tb2 = Entry(main)
tb2.place(x=190, y=60, width= 150, height=30)



lb3 =Label(main, text="คะแนนปลายภาค: ", font = ("Cooper Black", 14))
lb3.place(x=10,y=100)
tb3 = Entry(main)
tb3.place(x=190, y=100, width= 150, height=30)