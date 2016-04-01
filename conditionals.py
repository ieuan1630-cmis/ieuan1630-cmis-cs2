import random

def convert_caps(text): #for Free response questions
    text = text.replace(".", "") #removes periods
    caps = text.upper() #converts text to caps
    return caps

def list_to_string(text):
    text = str(text)
    text = text.replace("""['""", "")
    text = text.replace("""', '""", " ")
    text = text.replace("""']""", "")
    return text

def mc_answer_check(guess, answer):
    if guess == answer:
        return True
    else:
        return False

def mc_points(result):
    if result == True:
        return 1
    else:
        return 0

def delayed_gratification_check(answer):
    print list_to_string(["Haha", "hehe", "funny", "u are"][0:(random.randint(1,4)):1])
    see_answer = raw_input("Would you like to see the answer?(y or n)")
    if see_answer == "n":
        print ""
        return True
    elif not see_answer == "n":
        print "The best answer is: " + answer + "\n"
        return False

def calculate_IQ(score):    #mental age as calculated by their score divided by their actual age x100 = IQ
    age = float(raw_input("How old are you?"))
    if score == 0 or score == 46:
        mental_age = 120
    elif 0 < score <= 11.5:
        mental_age = 25
    elif 11.5 < score <= 23:
        mental_age = 50
    elif 23 < score <= 34.5:
        mental_age = 75
    elif 34.5 < score < 46:
        mental_age = 100
    IQ = (mental_age/age) *100
    IQ = IQ + ((random.choice([-1, 1])) * (random.random() * 15))
    return IQ


def main():
    score = 0
    print """This quiz will test your IQ!
Your score along with all the answers will be shown at the end."""
    raw_input("Hit 'enter' to begin") #hitting enter finishes the raw_input part and gets the script to continue running
    raw_input("FREE RESPONSE SECTION:")
    A1 = convert_caps(raw_input("""Q1: Define 'delayed gratification'.
"""))
    if "TEMPTATION" in A1 and "IMMEDIATE REWARD" in A1:
        score = score + 2
    elif "TEMPTATION" in A1 or "IMMEDIATE REWARD" in A1:
        score = score + 1
    else:
        score = score
    dgc1 = delayed_gratification_check("DELAYED GRATIFICATION REFERS TO THE TRADE OFF BETWEEN THE TEMPTATION OF AN IMMEDIATE REWARD AND A GREATER REWARD IN THE FUTURE")
    score = score + mc_points(dgc1)

    A2 = convert_caps(raw_input("""Q2: What does IQ stand for?
"""))
    if A2 == "INTELLIGENCE QUOTIENT":
        score = score + 1
    dgc2 = delayed_gratification_check("INTELLIGENCE QUOTIENT")
    score = score + mc_points(dgc2)

    A3 = convert_caps(raw_input("""Q3: Does your mother know you're stupid?
"""))
    if A3 == "EVEN A SCORPION IS A GAZELLE IN THE EYES OF ITS MOTHER":
        score = score + 10
    elif A3 == "SHE KNOWS I'M A GENIUS":
        score = score + 2
    elif A3 == "AT LEAST I HAVE A MOTHER":
        score = score + 1
    elif A3 == "YES" or A3 == "NO":
        score = score - 1
    else:
        score = score
    dgc3 = delayed_gratification_check("EVEN A SCORPION IS A GAZELLE IN THE EYES OF ITS MOTHER")
    score = score + mc_points(dgc3)


    A4 = convert_caps(raw_input("""Q4: What is the product of 0 and 1 over cosine 0?
"""))
    if A4 == "UNDEFINED":
        score = score + 1
    dgc4 = delayed_gratification_check("UNDEFINED")
    score = score + mc_points(dgc4)

    raw_input("MULTIPLE CHOICE SECTION (type a, b, c):")# for multiple choice should make sure responses are in allowed responses
    A5 = raw_input("""Q5: The month in secret code reads: kbpbdfbq, what month is it?
a) February b) November c) December
""")
    R5 = mc_answer_check(A5, "c")
    score = score + mc_points(R5)
    dgc5 = delayed_gratification_check("c")
    score = score + mc_points(dgc5)

    A6 = raw_input("""Q6: How many times can you subtract 10 from 100?
a) ten times b) five times c) one time
""")
    R6 = mc_answer_check(A6, "c")
    score = score + mc_points(R6)
    dgc6 = delayed_gratification_check("c")
    score = score + mc_points(dgc6)

    A7 = raw_input("""Q7: Mary's mother had three children, the first was called April, the second May, what was the name of the third child?
a) June b) July c) Mary
""")
    R7 = mc_answer_check(A7, "c")
    score = score + mc_points(R7)
    dgc7 = delayed_gratification_check("c")
    score = score + mc_points(dgc7)
 
    A8 = raw_input("""Q8: If you were running in a race and passed the person in 2nd place what position would you be in?
a) 1st b) 2nd c) 3rd
""")
    R8 = mc_answer_check(A8, "b")
    score = score + mc_points(R8)
    dgc8 = delayed_gratification_check("b")
    score = score + mc_points(dgc8)

    A9 = raw_input("""Q9: If an electric train is traveling south, which way is the smoke going?
a)North b) East c) Neither
""")
    R9 = mc_answer_check(A9, "c")
    score = score + mc_points(R9)
    dgc9 = delayed_gratification_check("c")
    score = score + mc_points(dgc9)
 
    A10 = raw_input("""Q10: Is it legal for a man to marry his widow's sister?
a)Yes b) In some countries c) He can't
""")
    R10 = mc_answer_check(A10, "c")
    score = score + mc_points(R10)
    dgc10 = delayed_gratification_check("c")
    score = score + mc_points(dgc10)

    A11 = raw_input("""Q11: Which month has 28 days?
a)All b) February c) February only on non leap years
""")
    R11 = mc_answer_check(A11, "a")
    score = score + mc_points(R11)
    dgc11 = delayed_gratification_check("a")
    score = score + mc_points(dgc11)

    A12 = raw_input("""Q12: Before Mt. Everest was discovered, which was the highest mountain in the world?
a) Mt. Fuji b) Mt Everest c) Mt. Mckinley
""")
    R12 = mc_answer_check(A12, "b")
    score = score + mc_points(R12)
    dgc12 = delayed_gratification_check("b")
    score = score + mc_points(dgc12)
    dgc_final = dgc1 + dgc2 + dgc3 + dgc4 + dgc5 + dgc6 + dgc7 + dgc8 + dgc9 + dgc10 + dgc11 + dgc12
    if dgc_final == 12:
        score = score + 12
        print """Good job you delayed your gratification! Here are the answers:
1)DELAYED GRATIFICATION REFERS TO THE TRADE OFF BETWEEN THE TEMPTATION OF AN IMMEDIATE REWARD AND A GREATER REWARD IN THE FUTURE
2)INTELLIGENCE QUOTIENT
3)EVEN A SCORPION IS A GAZELLE IN THE EYES OF ITS MOTHER
4)UNDEFINED
5)c
6)c
7)c
8)b
9)c
10)c
11)a
12)b"""        
    print """Your score is {}""".format(score)
    print """Your IQ is {}""".format(calculate_IQ(score))
    

main()


















#response collecting function
def response(prompt, allowed):
    resp = raw_input(prompt)
    #check to see if response is in the set of allowed responses
    if resp in allowed:
        #return it if it is
        return resp
    else:
        #call response() again if it is not
        print('Your answer must be one of the following:\n' + ", ".join(allowed))
        return response(prompt, allowed)



#--------Write a description of what your script will do first. This description can be written in gedit and used as the basis of your code later. See this example.
#-----------name the file conditionals.py
#----------2 conditional execution Q2 and Q4
#---------2 alternative execution mc_points and mc_checker
#---------2 chained conditionals 
#----------Use raw_input.
#--------Use good variable names.
#--------Use type conversion when necessary.
#----------------Define at least 4 functions that do something substantial (not just adding 2 numbers or multiplying).
#-----------At least 1 must return a boolean value and be used as a part of the flow control. mc_answer_check
#-----------At least one must return an integer or float. mc_points
#-----------At least 1 must return a string. convert_caps
#-----------The 4th can do what ever you want. dgchecker
#-----------Define a main() function to organize the flow of your program. Be sure to think about the three phases (input, processing, output)
#-----------Use at least 3 different relational operators. use to define IQ in IQ calculator
#-------------Use each of the logical operators at least once. and + or used
#-------------use not logical operator -- used to in mc_answer_check
#------------Use random.random() -- used to add or subtract deviation
#------------and random.randint() at least once each in your script. used to randomly print haha responses
#------------Use str.format() at least once in your script. print score
#------------Use """ or ''' strings at least once in your script.
#------------Write an interesting and/or entertaining story/game.
#------------Use the same structure we learned about in the simple program assignment.

#Program description:
#My function will test your "IQ"
#It will ask you a series of question and based on your answers return your smartness level
#all answers are converted before comparison to caps to avoid case issues, and all "." removed
#-- FREE RESPONSE:
#Q1: "Define delayed gratification."
#-- if answer includes word "temptation" or "immediate reward" award point 
#-- if both award 2 points
#Q2: "What does IQ stand for?"
#--answer compared with "INTELLIGENCE QUOTIENT"
#Q3: "Does your mother know you're stupid?"
#--if "AT LEAST I HAVE A MOTHER" or "SHE KNOWS I'M A GENIUS" award a point
#--- elif "EVEN A SCORPION IS A GAZELLE IN THE EYES OF ITS MOTHER" award 10 points
#Q4: "What is the product of 0 and 1 over cosine 0?"
#-- answer = UNDEFINED
#-- MULITPLE CHOICE:
#Q5: The month in secret code reads: kbpbdfbq, what month is it?
#a) February b) November c) December
# answer = december
#Q6: How many times can you subtract 10 from 100?
#a) ten times b) five times c) one time
#answer = c
#Q7: Mary's mother had three children, the first was called April, the second May, what was the name of the third child?
#a) June b) July c) Mary
#answer = c
#Q8: If you were running in a race and paced the person in 2nd place what position would you be in?
#a) 1st b) 2nd c) 3rd
#answer = b
#Q9: If an electric train is traveling south, which way is the smoke going?
#a)North b) East c) Neither
#answer = c
#Q10: Is it legal for a man to marry a widow's sister?
#a)Yes b) In some countries c) He can't
#answer = c
#Q11: Which month has 28 days?
#a)All b) February c) February only on non leap years
#answer = a
#Q12: Before Mt. Everest was discovered, which was the highest mountain in the world?
#a) Mt. Fuji b) Mt Everest c) Mt. Mckinley
#answer = b
# if answer is correct variable score in main is increased by set number, if not score remains unchanged. Regardless of the answer the text "HAHA" is printed.
#after each substantial question the question "Do you want to know the answer?" if no a point awarded if yes answer is shown and no point awarded
#at the end the player's score will be displayed
