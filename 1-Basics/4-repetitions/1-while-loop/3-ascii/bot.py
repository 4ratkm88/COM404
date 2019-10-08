import time
print("How many bars should be charged?")

bars = 1
count = int(input(""))

while bars < count:
    print("\033[0;32;40m Charging Up: "+"█"*bars+str(bars))
    time.sleep(0.5)
    bars += 1
if bars == count:
    while bars > 0:
        print("\033[0;31;40m Discharging: "+"█"*bars+str(bars))
        time.sleep(0.1)
        bars -=2
else:
    print("The battery is fully charged.")
   