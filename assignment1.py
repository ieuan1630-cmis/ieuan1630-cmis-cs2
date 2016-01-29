#variables:
name = "Ieuan"
yrs = 16
months = 11/12.0
days = 29/365.0
age_yr = yrs + months + days
age_avg = 67.2
height_m = 1.76
avg_height_m = 1.75
square_length = 1
rectangle_length = 2
rectangle_height = 3

#calculations:
age_mth = float(age_yr) * 12
age_left = age_avg - age_yr
height_ft = height_m * 3.28084
height_diff = height_m - avg_height_m
square_area = 1**2
cube_vol_half = 0.5 * 1**3
rectangle_area_ninth = 1/9.0 * rectangle_length * rectangle_height



#display:
print age_mth
print ";)" * 1
print rectangle_area_ninth

