print("What is your name human?")
name=input()
print("How old are you (in years)?")
age=int(input())
print("How tall are you (in meters)?")
height=float(input())
print("How much do you weight?")
weight=int(input())
num=height*height
bmi=weight/num

print(name + " you are " +str(age) +" years old and your bmi is "+ str(bmi))