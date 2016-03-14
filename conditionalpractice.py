def which_path():
    which_path = raw_input("Should she take the forest path or the main road? (f or m): ")
    if which_path == "f":
        print "Little Red took the forest path to pick some flowers, but as a result her grandmother got eaten by a wolf."
    elif which_path == "m":
        print "Little Red took the main path and lived happily ever after."
    else:
        print "Please type f or m"
        return which_path()

def which_path2():
    which_path2 = raw_input("Please type f or m: ")
    return which_path()

def storytime():
    print "Once upon a time Little Red Riding Hood went for a walk..."
    return which_path()

storytime()


   


def bingo(): #get input and if input is bingo return true
    x = raw_input("Type a word: ")
    return bool(x == "bingo" or x == "Bingo")

def JK():
    in_the_house = raw_input("Is jk in the house? ")
    if in_the_house == "YES" or in_the_house == "Yes" or in_the_house == "yes":
        return "That's right"
    else:
        return "You're blind dumbo, of course he's in the house"


def clapYourHands():
    print "clap clap"
def stompYourFeet():
    print "stomp stomp"
def TrueorFalse(string):
    if string == "Yes" or string == "YES" or string == "yes":
        string = True
    else:
        string = False
    return string
        
def happymain():
    youreHappy = TrueorFalse(raw_input("Are you happy? "))
    youKnowIt = TrueorFalse(raw_input("Do you know it? "))
    
    if youreHappy and youKnowIt:
        clapYourHands()
        stompYourFeet()

    print "Good bye"
