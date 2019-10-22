from function import under
print("Please enter a word")
word=str(input())
print("What would you like to do?")
print("Press 1 to under")
print("Press 2 to over")
print("Press 3 to under and over")
print("Press 4 to grid")
option=str(input())
if option==str(1):
    underword=word
    under(underword)
else:
    print("thats it for now")



