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

def convert_caps(text):
    text = text.upper()
    return text

def main():
    #output1
    print "This quiz will test your IQ!"
    raw_input("Hit 'enter' to begin") #hitting enter finishes the raw_input part and gets the script to continue running
    

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
