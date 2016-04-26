def countup(n):
    if n == 10:
        print "Blastoff!"
    else:
        print n
        return countup(n+1)

def main():
    return countup(int(raw_input("Pick an integer less than 10: ")))

#main()

def countup_from(start, end):
    if start == end:
        print "Finished"
    else:
        print start
        return countup_from(start + 1, end)

def countdown_from(start, end):
    if start == end:
        print "Finished"
    else:
        print start
        return countdown_from(start - 1, end)

countup_from(1,10)
countdown_from(10,1)
