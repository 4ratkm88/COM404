Health=100
print("Your health is "+str(Health)+"%. Escape is in progress... ")
for x in range(5,0,-1):
    print("...Oh dear, who is that?")
    name=str(input())
    if name=="smiler":
        Health-=40
        print("Time to jam out of here.")
    elif name=="hacker":
        Health=Health+20
        print("Yay! Better follow this one!")
    else:
        print("Phew, just another emoji!")
if Health > 0:
    print("Escaped! Health is "+str(Health))
elif Health < 0:
    print("Yo Ded")
else:
    print("You barely survived")
        