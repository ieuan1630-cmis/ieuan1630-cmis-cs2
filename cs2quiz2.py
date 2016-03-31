#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) 5*2 == 1*10
#b) 8**3 <= 200
#c) 34 >= 76*0.4
#
#2) What does 'return' do?
# It spits out a value as a result of a function call which can be used by other parts of a program.
#
#
#
#3) What are 2 ways indentation is important in python code?
#a) Lines that are indented after the line in which the "def" key word indicates the start of a function definition tell the program they are part of the same function definition - if they are not indented they are considerd a new line of code separate to this definition.
#b) Indentation tells functions and programs what to execute if a certain conditional statement is true (the lines indented after such a statement are the ones executed).
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) = -36
#problem1_b) = -math.sqrt(3)
#problem1_c) = 0
#problem1_d) = -5
#
#problem2_a) = True
#problem2_b) = False
#problem2_c) = False
#problem2_d) = False
#
#problem3_a) = 0.3
#problem3_b) = 0.5
#problem3_c) = 0.5
#problem3_d) = 0.5
#
#problem4_a) = 7
#problem4_b) = 5
#problem4_c) = 0.125
#problem4_d) = 5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

def different_or_not(a, b, c):
    if a != b and a != c and b != c: # checks if numbers are all different
        if a > b and a > c: # checks if a is greatest
            return a
        elif b > a and b > c: # checks if b is greatest
            return b
        elif c > a and c > b: # checks if c is greatest
            return c
    else:
        return False #if one number isn't greater than both others, False is returned

def output(largest):
    if largest == False:
        return "You didn't follow directions"
    else:
        return "The largest number was {}".format(largest)

def main():
    print "Type in 3 different numbers (decimals are OK!)"
    #input
    A = float(raw_input("A: "))
    B = float(raw_input("B: "))
    C = float(raw_input("C: "))
    #processing
    largest = different_or_not(A, B, C)
    #output
    print output(largest)

main()

