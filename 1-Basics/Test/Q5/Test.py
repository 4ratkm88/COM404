def smiler(dmg):
    dmg-=20
    health=health-dmg
    print("Time to jam out of here")

def hacker(dmg):
    dmg==20
    health=health+dmg
    print("Yay! Better follow this one!")


for x in range(5, 0, -1):
    print("...Oh dear, who is that? ")
    name=str(input())
    if name=="smiler":
        smiler()
    else:
        hacker()     