#variables are assigned values:
name = "Ieuan"
yrs = 16
months = 11/12.0
days = 29/365.0
age_yr = yrs + months + days #Ieuan's age in years as a decimal
age_avg = 67.2 #in years as found on Google search for "average life expectancy"
height_m = 1.76 #Ieuan's height in metres
avg_height_m = 1.75 #as cited by the BBC for 16 year old UK males
square_length = 1
rectangle_length = 2
rectangle_height = 3

#calculations:
age_mth = age_yr * 12 #variable age_yr is multiplied by 12 to find subject's age in months (there are 12 months in a year)
age_left = age_avg - age_yr #subject's age is subtracted from the average life expectancy to find approximate years left to live 
height_ft = height_m * 3.28084 #subject's height in metres is multiplied by the value of 1 metre in feet, to find subject's height in ft
height_diff = height_m - avg_height_m #average height of 16 year old male in UK is subtracted from subject's height in metres
square_area = square_length**2 #length of square is squared to find area of square
cube_vol_half = 0.5 * square_length**3 #length of square is cubed and then halved to find half the volume of cube
rectangle_area_ninth = 1/9.0 * rectangle_length * rectangle_height #length and height of rectangle are multiplied to find area of rectangle which is then divided by 9

#output
print "This is " + str(name) + " telling the computer what to say. I'm " + str(age_yr) + " years old - that's " + str(age_mth) + " months old, meaning that I probably have about " + str(age_left) + " years left to live. And based on the deviation of my height from the average height (" + str(height_diff) + "m) it seems that average statistics are a very accurate standard to go by." #output message to be displayed includes 5 variables and uses concatenation method
print #free line is printed for aesthetics
print "If a square is",square_length,"units long, then it's area is", square_area, "units squared, and half of its volume is", cube_vol_half,"units cubed. If a rectangle's side lengths are",rectangle_length,"units and",rectangle_height,"units, then one ninth of its area is",rectangle_area_ninth,"units squared." #out put message to be displayed includes 6 variables, and uses comma method
print ";)" * 10000 #string ";)" is made to print 10000 times

