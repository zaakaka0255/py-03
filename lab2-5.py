midterm=int(input("midterm: "))
final=int(input("final: "))
homework=int(input("homework: "))

x= ( midterm*40/100)+(final*50/100)+(homework*10/100)
        
if x >= 90 and x <= 100:
        print("grade a")
elif x>= 85 and x <=90:
        print("grade b+")
elif x >= 80 and x <=85:
        print("grade b")
elif x>= 70 and x <=80:
        print("grade c+")
elif x >= 60 and x <=70:
        print("grade c")
elif x>= 55 and x <=60:
        print("grade d+")
elif x >= 50 and x <=55:
        print("grade d")        
elif x>= 0 and x <=50:
        print("grade f")