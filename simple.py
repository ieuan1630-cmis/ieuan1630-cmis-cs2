from math import pow

def div(x, y):
    return x / (y + 0.0)

def square(x):
    return pow(x, 2)

def BMI(weight, height):
    return div(weight, square(height))

def output(name, BMI1):
    return """
Hello {}
Your BMIS is {}
""".format(name, BMI1)

def main():
    #input
    name = raw_input("type your name: ")
    weight = raw_input("type your weight in kg: ")
    height = raw_input("type your height in metres: ")
    #processing
    BMI1 = BMI(weight, height)
    #output
    print output(name, BMI1)

main()
