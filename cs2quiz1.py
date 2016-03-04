#40/40
#Part 1: Terminology (15 points) --> 15/15
#1 1pt) What is the symbol "=" used for?
#to assign and store values to and in variables
# 1pt
#
#2 3pts) Write a technical definition for 'function'
#a named sequence of calculations which takes input and returns output
# 3pts
#
#3 1pt) What does the keyword "return" do?
#it gives back the output or result of the function
#   1pt
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: integer ex: 1, 2
#	2: floating point ex: 1.2, 1.3
#	3: string ex: "hi", "hello"
#	4: boolean ex: True, False
#	5: tuple ex: ("HEllo", 3), ("Bob", 10, "fat")
# 5pts
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#a function definition does not result in any output being presented, it simply defines a set of calculations which are run if and only if they are called by a function call
# 2pts
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:input (the program takes some input values, most often from the user)
#	2:processing (the program does something with those input values to for instance calculate something)
#	3:output (the program returns the product of its labours (processing) often a something printed
# 3pts
#
#Part 2: Programming (25 points) --> 25/25
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi (a = pi(r)^2) so r = sqrt(a/pi)

import math


#1 pt for header line
#3 pt for correct formula
#1 pt for return value
#1 pt for parameter name
#1 pt for function name
def circarea_to_diameter(circarea):
	return 2 * (math.sqrt(circarea/math.pi)) #finds radius and multiples by 2 to get diameter

def sum_three(x, y, z): #takes three values and adds them
    return x + y + z

#1pt for header line
#1pt for parameter names
#1pt for return value
#1pt for correct output format
#3pt for correct use of format function
def output(d1, d2, d3, total):
    return """
Circle	Diameter
C1  {}
C2 	{}
C3 	{}
Totals	{}
""".format(d1, d2, d3, total)

#1pt header line
#1pt getting input
#1pt converting input
#1pt for calling output function
#2pt for correct diameter formula
#1pt for variable names
def main():
    #input
    C1 = raw_input("Area of C1: ")
    C2 = raw_input("Area of C2: ")
    C3 = raw_input("Area of C3: ")
    #processing
    d1 = circarea_to_diameter(float(C1))
    d2 = circarea_to_diameter(float(C2))
    d3 = circarea_to_diameter(float(C3))
    total = sum_three(d1, d2, d3)
    #output
    print output(d1, d2, d3, total)

#1pt for calling main
main()

#1pt explanatory comments
#1pt code format
        

