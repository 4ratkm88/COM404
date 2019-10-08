import os
import time


print("What level of brightness is required?")
count=int(input())
time.sleep(1)
print("Adjusting brightness.")

time.sleep(1)
#os.system('cls')
print("Adjusting brightness..")

time.sleep(1)

print("Adjusting brightness...")
time.sleep(1)
for count in range(0, count, 2):
    time.sleep(1)
    print("Beep's brightness level:"+int(count)*"*")
    print("Bop's brightness level:"+int(count)*"*")
