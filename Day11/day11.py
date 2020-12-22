
seats = {
    i + j * 1j: False
    for i, line in enumerate(open('inputday11.txt').read().splitlines())
    for j, c in enumerate(line)
    if c == 'L'
}


def occupied(seat):
    return sum(
        seats.get(seat + d, 0)
        for d
        in [-1-1j, -1j, 1-1j, -1, 1, -1+1j, 1j, 1+1j]
    )


while seats != (seats := {
        k: occupied(k) == 0 or (occupied(k) < 4 and v)
        for k, v
        in seats.items()
    }): pass

print(sum(seats.values()))
