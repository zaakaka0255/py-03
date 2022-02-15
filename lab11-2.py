# Python code to illustrate
# working of try()
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by Best ")
 
# Look at parameters and note the working of Program
divide(3,0)

print("ภาสกรณ์ แสนปาง")