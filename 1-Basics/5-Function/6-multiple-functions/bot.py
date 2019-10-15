def displayLadder(steps):

    for count in range(0, steps, 1):
        print("| |")
        print("***")

def create_ladder():
    print("How many steps?")
    steps=int(input())
    displayLadder(steps)


create_ladder()

