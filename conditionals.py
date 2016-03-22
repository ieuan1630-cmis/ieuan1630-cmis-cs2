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

def convert_caps(text): #for Free response questions
    text = text.replace(".", "") #removes periods
    caps = text.upper() #converts text to caps
    return caps

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

def main():
    score = 0
    print "This quiz will test your IQ!"
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

    A2 = convert_caps(raw_input("""Q2: What does IQ stand for?
"""))
    if A2 == "INTELLIGENCE QUOTIENT":
        score = score + 1

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

    raw_input("MULTIPLE CHOICE SECTION:")# for multiple choice should make sure responses are in allowed responses
    A5 = raw_input("""Q5: The month in secret code reads: kbpbdfbq, what month is it?
a) February b) November c) December
""")
    R5 = mc_answer_check(A5, "c")
    score = score + mc_points(R5)

    A6 = raw_input("""Q6: How many times can you subtract 10 from 100?
a) ten times b) five times c) one time
""")
    R6 = mc_answer_check(A6, "c")
    score = score + mc_points(R6)

    A7 = raw_input("""Q7: Mary's mother had three children, the first was called April, the second May, what was the name of the third child?
a) June b) July c) Mary
""")
    R7 = mc_answer_check(A7, "c")
    score = score + mc_points(R7)
 
    A8 = raw_input("""Q8: If you were running in a race and paced the person in 2nd place what position would you be in?
a) 1st b) 2nd c) 3rd
""")
    R8 = mc_answer_check(A8, "b")
    score = score + mc_points(R8)

    A9 = raw_input("""Q9: If an electric train is traveling south, which way is the smoke going?
a)North b) East c) Neither
""")
    R9 = mc_answer_check(A9, "c")
    score = score + mc_points(R9)
 
    A10 = raw_input("""Q10: Is it legal for a man to marry a widow's sister?
a)Yes b) In some countries c) He can't
""")
    R10 = mc_answer_check(A10, "c")
    score = score + mc_points(R10)

    A11 = raw_input("""Q11: Which month has 28 days?
a)All b) February c) February only on non leap years
""")
    R11 = mc_answer_check(A11, "a")
    score = score + mc_points(R11)

    A12 = raw_input("""Q12: Before Mt. Everest was discovered, which was the highest mountain in the world?
a) Mt. Fuji b) Mt Everest c) Mt. Mckinley
""")
    R12 = mc_answer_check(A12, "b")
    score = score + mc_points(R12)
    print score


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
