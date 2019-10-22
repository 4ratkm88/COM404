def is_league_united(hero1,hero2):
    if hero1=="Superman" and hero2=="Wonderwoman":
        return True
    else:
        return False

def decide_plan(hero1,hero2):
    
    if is_league_united(hero1,hero2):
        print("Time to save the world!")
    else:
        print("We must unite the league!")

def run():
    print("Who is hero1")
    hero1=str(input())
    print("Who is hero2")
    hero2=str(input())
    print("league or plan")
    decision=str(input())
    if decision=="league":
        is_league_united(hero1,hero2)
    elif decision=="plan":
        decide_plan(hero1,hero2)
    else:
        print("Not working")

run()