from collections import Counter
from operator import sub
#The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python.

with open('day10input.txt') as f:
    data = [0] + sorted(int(x) for x in f)
    data.append(data[-1] + 3)

diffs = map(sub, data[1:], data)
count = Counter(diffs)
print(count[1] * count[3])
#__________________________ pt2
paths = [0] * (len(data) - 1) + [1]
for i in range(len(data) - 2, -1, -1):
    for j in range(i + 1, i + 4):
        if j < len(data) and data[j] - 3 <= data[i]:
            paths[i] += paths[j]
print(paths[0])