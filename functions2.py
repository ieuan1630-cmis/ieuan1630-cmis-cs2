#import:
from math import pi
from math import sqrt
import str_manip

#define functions:
    #basic maths functions
def add(x, y): #takes two variables and adds their values
    return x + y

def sub(x, y): #takes two variables and subtracts the second from the first value
    return x - y

def mul(x, y): #takes two variables and multiplies their values
    return x * y

def div(x, y): #takes two variables and divides the second from the first value
    return x / (y + 0.0)

    #complex functions
def secs_to_hrs(secs): #takes a value of seconds and converts it to a value in hrs
    return secs / 3600.0

def circle_area(r): #takes the radius r of a circle and returns its area
    return pi * r**2

def sphere_vol(r): #takes the radius r of a sphere and returns its volume
    return (4/3.0) * pi * r**3

def avg_two_vols(r1, r2): #takes the radii r1 and r2 of two spheres and returns the average of their volumes
    return (sphere_vol(r1) + sphere_vol(r2))/ 2.0

def tri_area(s1, s2, s3): #takes the side lengths of a triangle and returns its area
    s = (s1 + s2 + s3)/2.0 #s = side length
    return sqrt(s * (s - s1) * (s - s2) * (s - s3))

def right_align(txt): #aligns txt to the right side of an 80 characters wide screen
    return " " * (80 - len(txt)) + txt

def centre(txt): #centres text for an 80 characters wide screen
    return " " * (40- (len(txt)/2)) + txt




def msg_box(txt): #takes text and returns it in a message box composed of various strings
    return "+" + ((len(txt) + 4) * "-") + "+" + "\n" + "|  " + txt + "  |" + "\n" + "+" + ((len(txt) + 4) * "-") + "+"






#storing function calls (2 per function) in variables:
#list of functions needing to be called twice each: add2, sub2, mul2, div2, secs_to_hrs2, circle_area2, sphere_vol2, avg_two_vols2, tri_area2, right_align, centre, msg_box
output = "There are " + str(mul(24, 3600)) + " seconds in a day. Which means there are " + str(secs_to_hrs(mul(24, 3600))) + " hours in a day. If you have 6000 seconds to complete an exam, you have " + str(secs_to_hrs(6000)) + " hours to complete it. Taking that there are 5 weekdays and 2 weekend days, there are " + str(add(5, 2)) + " days in a week. Also, " + str(add(7, 7)) + " days in a fortnight. Given 365 days in a year there are " + str(div(365, 7)) + " weeks in a year. Given 41 days passed this year, " + str(div(41, 7)) + " weeks have passed; and there are " + str(sub(365, 41)) + " days left this year. And " + str(sub(100, 41)) + " days until the 100th day of the year." + "\n" + "\n" + "Given a circle's radius as 5, that circle's area is " + str(circle_area(5)) + " units squared; if this circle was instead a sphere its volume would be " + str(sphere_vol(5)) + " units cubed. If our circle's radius is 6 units, this yields an area of " + str(circle_area(6)) + " units squared; a sphere with the same radius has a volume of " + str(sphere_vol(6)) + " units cubed. The average of the volumes of spheres with these two radii is " + str(avg_two_vols(5, 6)) + " units cubed. The average of the volumes of shperes with raddi 7 and 8 respectively is " + str(avg_two_vols(7, 8)) + " units cubed." + "\n" + "\n" + "Moving briefly on to triangles, given side lengths 3, 4, 5 - the area of this right triangle is " + str(tri_area(3, 4, 5)) + " units squared. This function also works for non right triangles such as one with side lenghts 6, 7, 8 - this hypothetical triangle's area would be " + str(tri_area(6, 7, 8)) + " units squared." + "\n" + "\n" + centre("Hey") + "\n" +  right_align("You") + centre("This text is centred") + "\n" + right_align("This text is right aligned") + msg_box("Here's a message box") + "\n" + msg_box("and another")

#print output:
print str_manip.msg_box(output)
