#import:
from math import pi

#define functions:
    #basic maths functions
def add(x1, x2):
    return x1 + x2

def sub(x1, x2):
    return x1 - x2

def mul(x1, x2):
    return x1 * x2

def div(x1, x2):
    return x1 // x2

    #complex functions
def secs_to_hrs(secs):
    return secs / 3600.0

def circle_area(r):
    return pi * r**2

def sphere_vol(r):
    return (4/3.0) * pi * r**3

def avg_two_vols(r1, r2):
    return (sphere_vol(r1) + sphere_vol(r2))/ 2.0

#calculations (r = result):
r_add = add(3, 4)
r_sub = sub(3, 4)
r_mul = mul(3, 4)
r_div = div(3, 4)
r_secs_to_hrs = secs_to_hrs(3600 * 1.5)
r_circle_area = circle_area(1.1)
r_sphere_vol = sphere_vol(1.1)
r_avg_two_vols = avg_two_vols (1, 1.1)

#ouput
print r_add
print r_sub
print r_mul
print r_div
print r_secs_to_hrs
print r_circle_area
print r_sphere_vol
print r_avg_two_vols
