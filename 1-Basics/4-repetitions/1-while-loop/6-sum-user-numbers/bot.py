print("How many numbers should I sum up?")
calc=int(input())
count = 1
while count <=calc:
    print("Enter number "+str(count)+" of "+str(calc))
    num=int(input())
    result=num+num
    count += 1
print("The result is "+str(result))
