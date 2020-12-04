with open("./input.txt") as f:
    input = f.readlines()
input = [x.strip() for x in input]
input = [ int(x) for x in input ]

# Find the two numbers that add up to 2020 and multiply them by eachother
for firstnumber in input:
    for secondnumber in input:
        if(firstnumber + secondnumber == 2020):
            print(firstnumber*secondnumber)
            exit()
