from collections import defaultdict
#The Python defaultdict type behaves almost exactly like a regular Python dictionary,
#  but if you try to access or modify a missing key, then defaultdict will automatically 
# create the key and generate a default value for it. This makes defaultdict a valuable option
#  for handling missing keys in dictionaries.
bags = defaultdict(set)

for line in open('day7input.txt'):
    words = line.split()
    for i in range(5, len(words), 4):
        bags[words[i] + words[i+1]].add(words[0] + words[1])

# set builds an unordered collection of unique elements.
gold = set(bags['shinygold'])
while len(gold) != len(gold := gold | set.union(*[bags[bag] for bag in gold])): pass
print(len(gold))

#part 2
#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def cost(bag):
    return 1 + sum(
        num * cost(name) if name in bags else 1
        for num, name
        in bags[bag]
    )

bags = {
    words[0] + words[1]: [
        (int(words[i]), words[i+1] + words[i+2])
        for i
        in range(4, len(words), 4)
        if words[i] != 'no'
    ]
    for words
    in [line.split() for line in open('day7input.txt')]
}

print(cost('shinygold') - 1)