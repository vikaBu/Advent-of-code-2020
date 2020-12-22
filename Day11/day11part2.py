

seats = {
    i + j*1j: False
    for i, line in enumerate(open('inputday11.txt').read().splitlines())
    for j, c in enumerate(line)
    if c == 'L'
}

def neighbors(seat):
    ns = []
    for d in [-1 - 1j, -1j, 1 - 1j, -1, 1, -1 + 1j, 1j, 1 + 1j]:
        for i in range(1, 100):
            if seat + d * i in seats:
                ns.append(seat + d * i)
                break
    return ns


def occupied(seat):
    return sum(seats[n] for n in neighbors(seat))


while seats != (seats := {
        k: occupied(k) == 0 or (occupied(k) < 5 and v)
        for k, v
        in seats.items()
    }): pass

print(sum(seats.values()))
