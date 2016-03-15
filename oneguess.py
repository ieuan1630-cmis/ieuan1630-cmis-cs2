import random

def output1(minnum, maxnum):
    return "I'm thinking of a number from {} to {}.".format(minnum, maxnum)

def output2(target, guess, difference):
    print """
The target was {}.
Your guess was {}.""".format(target, guess)
    if difference == 0:
        return "That's correct! You must be psychic!"
    elif difference < 0:
        difference = abs(difference)
        return "That's over by {}.".format(difference)
    else: #if reaches here difference should be > 0
        return "That's under by {}.".format(difference)

def main():
    #input1
    minnum = raw_input("What is the minimum number? ")
    maxnum = raw_input("What is the maximum number? ")
    #output1
    print output1(minnum, maxnum)
    #input2
    guess = raw_input("What do you think it is? ")
    #processing1
    target = random.randint(int(minnum),int(maxnum))
    difference = target - int(guess)
    #output2
    print output2(target, guess, difference)
    

main()
