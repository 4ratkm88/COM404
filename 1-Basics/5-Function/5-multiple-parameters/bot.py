def climb_ladder(steprem, stepcrossed):

    if steprem > stepcrossed:
        print("Still some way to go!")
    elif stepcrossed >= steprem:
        print("We made it!")
    else:
        print("invalid numbers")

climb_ladder(2, 5)
climb_ladder(5, 5)