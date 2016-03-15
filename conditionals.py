#Program description:
#My function will test your "IQ"
#It will ask you a series of question and based on your answers return your smartness level
#all answers are converted before comparison to caps to avoid case issues
#Q1: "Define delayed gratification."
#-- if answer includes word "temptation"
#Q2: "What does IQ stand for?"
#--answer compared with "INTELLIGENCE QUOTIENT"
#Q3: "Does your mother know you're stupid?"
#--if "AT LEAST I HAVE A MOTHER" or "SHE KNOWS I'M A GENIUS" award a point
#Q4:
#--
#Q5:
#--
# if answer is correct variable score in main is increased by 1, if not score remains unchanged. Regardless of the answer the text "HAHA" is printed.
#after each substantial question the question "Do you want to know the answer?" if no a point awarded if yes answer is shown and no point awarded

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
