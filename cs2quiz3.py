#GRADED: 100% on terminology and reading. 9/10 for program for no main function initially
#Section 1: Terminology
# 1) What is a recursive function?
# A function that calls itself as a means of repeating certain lines of code
#
#
# 2) What happens if there is no base case defined in a recursive function?
# It will recurse infinitely and thus you will get an error something like "Maximum recursion limit reached"
#
#
# 3) What is the first thing to consider when designing a recursive function?
# What the base case, or base cases are. That is when and how your function will end and return something
#
#
# 4) How do we put data into a function call?
# By using parameters
#
# 
# 5) How do we get data out of a function call?
# By using parameters
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 8
#a2 = 8
#a3 = -1

#b1 = 2
#b2 = 2
#b3 = 4

#c1 = -2
#c2 = 4
#c3 = 10 + 9 +8+7+6+5 = 45

#d1 = 1 - (1 - (1 + (2+1+2))) = 6
#d2 = 1 + (3+1+3) = 8
#d3 = 1 - (1- (1+1+2)) = 4

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

#GRADING:
# +2 base case is present (MUST BE LABELED)
# +2 recursive case is present (MUST BE LABELED)
# +1 base case returns sum/ct (or equivalent)
# +2 recursive case filters even numbers
# +1 recursive case increments sum and ct correctly
# +1 recursive case returns correct recursive call
# -1 main function present AND called 

def avg_odd_input(summation=0, odds=0):
    num = raw_input("Next number: ")
    #Base case
    if num == "":
        return "The average of your odd numbers was {}".format(summation/odds)
    #Recursive cases
    else:
        if float(num) % 2 == 1:
            return avg_odd_input(summation + float(num), odds +1)
        else:
            return avg_odd_input(summation, odds)

def main():
    return avg_odd_input()

print main()
