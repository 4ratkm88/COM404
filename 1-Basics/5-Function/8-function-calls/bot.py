#1) Display in a Box – display the word in an ascii art box 
def ascii(asciiword):
    print("#####################")
    print("#                   #")
    print("#                   #")
    print("#      " + word + "   #")
    print("#                   #")
    print("#                   #")
    print("#                   #")
    print("#####################")


#2) Display Lower-case – display the word in lower-case e.g. hello 
def lower(lowerword):
    lowerword ==lower(word)
    print(str(word))
#3) Display Upper-case – display the word in upper-case e.g. HELLO
def upper(upperword):
    upperword == Upper(word)
    print(str(upperword))

 
#4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH 
#5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.
def run():
    print("Type a word")
    word=str(input())
    print("How many times should i display?")
    times=int(input())
    for count in range(0, times, 1):
        lower(lowerword)
        upper(upperword)
        ascii()


run()