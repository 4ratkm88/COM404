
print("How many live cables should I avoid?")

cables =int(input(""))
count = cables

while count > 0:
    print("Avoiding...Done! "+str(count)+" live cables avoided.")
    count -= 1

print("Avoiding...Done! All live cables avoided.")
