def hum_guess():

def comp_guess():


def rounds(num_rounds):
    if num_rounds == 0:
        if hum_score > cpu_score:
            winner = "Human"
        elif hum_score < cpu_score:
            winner = "Computer"
        elif hum_score == cpu_score:
            winner = "no one"
        return """Human score: {}
Computer score: {}
The {} wins!
""".format(hum_score, cpu_score, winner)
    else:
        hum_guess()
        comp_guess()
        return rounds(num_rounds - 1)
    

def main(num_rounds=3, hum_score=0, cpu_score=0):
    print "This is a guessing game of you against the computer..."
	rounds(num_rounds)
    

main()
