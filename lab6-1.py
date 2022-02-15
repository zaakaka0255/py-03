f = open("myfile2.txt","w") 
txt1="siam dhurakit \n" 
txt1 +="นาย ภาสกรณ์ แสนปาง \n"

s = f.write(txt1)
f.close()
         
print("เขียนลงไฟล์แล้ว")   