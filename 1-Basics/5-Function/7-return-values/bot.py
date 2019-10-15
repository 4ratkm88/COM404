def sum_weights(wbeep, wbop):
    totalw = wbeep + wbop
    return totalw

def calc_avg_weight(wbeep, wbop):
    avgw = (wbeep+wbop)/2
    return avgw

def run():
    print("What is the weight of Beep?")
    wbeep=int(input())
    print("What is the weight of bop?")
    wbop=int(input())
    print("What would you like to calcluate (sum or average)?")
    calc=input()
    totalw = sum_weights(wbeep, wbop)
    avgw = calc_avg_weight(wbeep, wbop)

    if calc=="sum":
       print("Total weight is: " + str(totalw)) 
    elif calc=="average": 
        print("Average weight is: " + str(avgw)) 
    else:
        print("Incorrect input")
run()