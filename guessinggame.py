import random

def hum_guess(reps=5, num=(random.randint(0,100))):
    if reps == 5:
        raw_input("The computer has a number, proceed to guesss it, good luck! (Press enter to continue)")
    guess = float(raw_input("Guess a number: "))
    if reps == 0:
        print "You suck at this"
        return False
    elif guess == num:
        print "Correct!"
        return True
    elif guess < num:
        print "Too low"
        return hum_guess(reps-1, num)
    else:
        print "Too high"
        return hum_guess(reps-1, num)

def comp_guess(reps=5, low=0, high=100):
    if reps == 5:
        raw_input("Think of a number before pressing enter")
    guess = low + ((high - low)/2)
    result = raw_input(("Computer's guess: {} (c, l, or h)".format(guess)))
    if reps == 0:
        print "Computer, you suck at this"
        return False
    elif result == "c":
        print "Argh you computer, that was my number"
        return True
    elif result == "l":
        print "Too low"
        return comp_guess(reps-1, guess, high)
    else:
        print "Too high"
        return comp_guess(reps-1, low, guess)

def rounds(num_rounds, hum_score, comp_score):
    if num_rounds == 0:
        if hum_score > comp_score:
            winner = "Human"
        elif hum_score < comp_score:
            winner = "Computer"
        elif hum_score == comp_score:
            winner = "no one"
        print """Human score: {}
Computer score: {}
{} wins!
""".format(hum_score, comp_score, winner)
    else:
        if hum_guess() == True:
            hum_score += 1
        if comp_guess() == True:
            comp_score += 1
        return rounds(num_rounds - 1, hum_score, comp_score)

def main(num_rounds=1, hum_score=0, comp_score=0):
    print """This is a guessing game of you against the computer. It is three rounds long. Each round both you and the computer will take a turn thinking of a number between 0 and 100 and guessing up to 5 times what the other's number is. In the case of the computer guesssing your number, type "c" for correct, "l" for low, or "h" for high."""
    rounds(num_rounds, hum_score, comp_score)

main()
