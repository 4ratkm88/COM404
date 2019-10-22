print("How many zones must I cross?")
zone=int(input())
for zone in range(zone, 0, -1):
    print("…crossed zone "+ str(zone))
print("Crossed all zones.  Jumanji!")