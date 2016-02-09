#import:
from math import pi
from math import sqrt

#define functions:
    #basic maths functions
def add(x, y): #takes two variables and adds their values
    return x + y

def sub(x, y): #takes two variables and subtracts the second from the first value
    return x - y

def mul(x, y): #takes two variables and multiplies their values
    return x * y

def div(x, y): #takes two variables and divides the second from the first value
    return x // y

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

#calculations (r = result):
r_add = add(3, 4)
r_sub = sub(3, 4)
r_mul = mul(3, 4)
r_div = div(3, 4)
r_secs_to_hrs = secs_to_hrs(3600 * 1.5)
r_circle_area = circle_area(1.1)
r_sphere_vol = sphere_vol(1.1)
r_avg_two_vols = avg_two_vols (1, 1.1)
r_tri_area = tri_area(3, 4, 5)
r_right_align = right_align("Hello")
r_centre = centre("Hello")
r_msg_box1 = msg_box("Hello")
r_msg_box2 = msg_box("I eat cats!")

#ouput
print r_add
print r_sub
print r_mul
print r_div
print r_secs_to_hrs
print r_circle_area
print r_sphere_vol
print r_avg_two_vols
print r_tri_area
print r_right_align
print r_centre
print r_msg_box1
print r_msg_box2
