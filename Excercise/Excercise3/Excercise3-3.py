#This function prints the string followed by number of spaces such that the last character of the string comes at 70th position

def right_justify(s):
    lenght=len(s)
    spaces=""
    for i in range(70 - lenght):
        spaces +="d"
    print spaces+s


right_justify('allen')