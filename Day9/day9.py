from itertools import combinations
#itertools.combinations(iterable, r)
#This tool returns the  length subsequences of elements from the input iterable.
#Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

with open("inputday9.txt") as f:
    numbers = [int(x) for x in f]

preamble = 25
for i in range(len(numbers)-preamble):
    n = numbers[i+preamble]
    for a, b in combinations(numbers[i:i+preamble], 2):
        if a+b == n:
            break
    else:
        print(n)
        break

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        elements = numbers[i:j]
        if sum(elements) == n:
            print(min(elements)+max(elements))
            break
    else:
        continue
    break