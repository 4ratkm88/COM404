print("Please enter a number")
fact=int(input())
count = 1
result = 0
while count <= fact:
   
    calc=count*count+1
    result+=calc
    count += 1
print("The result is "+str(result))
