#readfile and returns a copy of the string in which all chars have been stripped from the beginning and the end of the string
with open("./input.txt") as f:
    input = f.readlines()
input = [x.strip() for x in input]
input = [ int(x) for x in input ]

# Find the three entries that add up to 2020 and multiply them by eachother
for firstnumber in input:
    for secondnumber in input:
        for thirdnumber in input:
            if(firstnumber + secondnumber + thirdnumber == 2020):
                print(firstnumber*secondnumber*thirdnumber)
                exit()