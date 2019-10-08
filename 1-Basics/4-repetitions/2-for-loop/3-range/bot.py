import os
import time

os.system('cls' if os.name == 'nt' else "printf '\033c'")
time.sleep(2)
print("What level of brightness is required?")
count=int(input())
time.sleep(2)
os.system('cls' if os.name == 'nt' else "printf '\033c'")
print("Adjusting brightness.")
time.sleep(2)
os.system('cls' if os.name == 'nt' else "printf '\033c'")
print("Adjusting brightness..")
time.sleep(2)
os.system('cls' if os.name == 'nt' else "printf '\033c'")
print("Adjusting brightness...")
time.sleep(2)
os.system('cls' if os.name == 'nt' else "printf '\033c'")
    for count in range(0, count, 2):
    print("Beep's brightness level:"+int(count)*"*")
    print("Bop's brightness level:"+int(count)*"*")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else "printf '\033c'")