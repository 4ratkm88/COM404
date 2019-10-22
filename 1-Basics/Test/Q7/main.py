from function import under,over,underover

print("Please enter a word")
word=str(input())
print("What would you like to do?")
print("Press 1 to under")
print("Press 2 to over")
print("Press 3 to under and over")
print("Press 4 to grid")
option=str(input())
if option==str(1):
    under(word)
elif option==str(2):
    over(word)
elif option==str(3):
    underover(word)
else:
    print("thats it for now")



