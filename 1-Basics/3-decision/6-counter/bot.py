print("Please enter the first whole number.")
nr1 = int(input())
print("Please enter the second whole number.")
nr2 = int(input())
print("Please enter the third whole number.")
nr3 = int(input())

if (nr1 == 0 or nr2==0  or nr3==0):
     print("0 is not even nor odd")
elif ((nr1 % 2) == 0 and (nr2 % 2) == 0 and (nr3 % 2) == 0):
    print("There were 3 even and 0 odd numbers.")

   
elif ((nr1 % 2) == 0 and (nr2 % 2) == 0 and (nr3 % 2) != 0):
    print("There were 2 even and 1 odd numbers.")
elif ((nr1 % 2) == 0 and (nr2 % 2) != 0 and (nr3 % 2) == 0):
    print("There were 2 even and 1 odd numbers.")
elif ((nr1 % 2) == 0 and (nr2 % 2) != 0 and (nr3 % 2) != 0):
    print("There were 0 even and 2 odd numbers.")
elif ((nr1 % 2) != 0 and (nr2 % 2) == 0 and (nr3 % 2) == 0):
    print("There were 2 even and 1 odd numbers.")
elif ((nr1 % 2) != 0 and (nr2 % 2) != 0 and (nr3 % 2) == 0):
    print("There were 1 even and 2 odd numbers.")
elif ((nr1 % 2) != 0 and (nr2 % 2) == 0 and (nr3 % 2) != 0):
    print("There were 1 even and 2 odd numbers.")
elif ((nr1 % 2) != 0 and (nr2 % 2) != 0 and (nr3 % 2) != 0):
    print("There were 0 even and 3 odd numbers.")

else:
    print("Missing calculation")
