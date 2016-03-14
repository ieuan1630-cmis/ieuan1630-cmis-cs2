import random

def set_range(minnum, maxnum):
    rnge = range(minnum, maxnum)
    return rnge

def output1(minnum, maxnum):
    return "I'm thinking of a number from {} to {}.".format(minnum, maxnum)

def output2(target, guess, difference):
    return """
The target was {}.
Your guess was {}.
That's under by {}.
""".format(target, guess, difference)

def main():
    #input1
    minnum = raw_input("What is the minimum number? ")
    maxnum = raw_input("What is the maximum number? ")
    #processing1
    rnge = set_range(int(minnum), int(maxnum))
    #output1
    print output(minnum, maxnum)
    #input2
    guess = raw_input("What do you think it is? ")
    #processing2
    #output2
    output2(target, guess, difference)
    

main()
