import re

#open and read the input file
def get_input():
    with open("./inputday2.txt") as f:
        return f.read().split("\n")

def split_input(input):
    # Takes input (example 2-3 c: mbcc) and splits it into it's components
    # remove colons
    lowest, highest, token, password = re.split("[- :]+", input)
    #Convert a number or string to an integer, or return 0 if no arguments are given. If x is a number, return x.int()
    return(int(lowest), int(highest), token, password)

def passwordcount(input):
    i = 0
    for num in input:
        # Count amount of times the password meets the password requirements
        # Amount of times token exists in passwords needs te be between lower and upper bounds
        lowest, highest, token, password = split_input(num)
        count = password.count(token)
        if(count >= lowest and count <= highest):
            i += 1
    return(i)

def passwordcount2(input):
    i = 0
    for num in input:
        # Count amount of times the password meets the password requirements
        lowest, highest, token, password = split_input(num)
        a = password[lowest-1]
        b = password[highest-1]
        if((a == token) ^ (b == token)):
            i += 1
    return(i)

def main():
    print(passwordcount(get_input()))
    print(passwordcount2(get_input()))
    pass

main()