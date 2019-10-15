def sum_weights(wbeep, wbop):
    totalw = wbeep + wbop
    print("The sum of Beep and Bop's weight is " + str(totalw))

def calc_avg_weight(wbeep, wbop):
    avgw = (wbeep+wbop)/2
    print("The avg weight of the robots is " + str(avgw))

def run():
    print("What is the weight of Beep?")
    wbeep=int(input())
    print("What is the weight of bop?")
    wbop=int(input())
    print("What would you like to calcluate (sum or average)?")
    calc=input()
    if calc=="sum":
        sum_weights(wbeep, wbop)
    elif calc=="average": 
        calc_avg_weight(wbeep, wbop)
    else:
        print("Incorrect input")
run()