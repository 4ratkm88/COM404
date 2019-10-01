print("What type of cover does the book have? soft/hard")
bookc=input()



if(bookc == "soft"):
    print("Is the book perfect-bound? yes/no")
    perf=input()
    if(perf =="yes"):
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("At least it has a soft cover")
else:
    print("Whatever")