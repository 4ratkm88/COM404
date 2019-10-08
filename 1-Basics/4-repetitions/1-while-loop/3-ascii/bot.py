import time
print("How many bars should be charged?")

bars = 1
count = int(input(""))

while bars < count:
    print("Charging: "+"█"*bars)
    time.sleep(1)
    bars += 1
if bars == count:
    while bars != 0:
        print("Discharging: "+"█"*bars)
        time.sleep(1)
        bars -=1
else:
    print("The battery is fully charged.")
   