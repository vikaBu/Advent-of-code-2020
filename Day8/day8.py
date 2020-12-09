def get_input():
    with open("./inputday8.txt") as f:
        return f.read().split("\n")

def part1(instructions):
    return runprogram(instructions)

def runprogram(instructions, change = -1):
    pointer = 0
    accumulator = 0
    previous_pointers = []
    success = True
    while True and pointer < len(instructions):
        if pointer in previous_pointers:
            success = False
            break
        else:
            previous_pointers.append(pointer)

        operation, argument = instructions[pointer].split(" ")
        argument = int(argument)

        if pointer == change:
            if operation == "nop":
                operation = "jmp"
            if operation == "jmp":
                operation = "nop"

        if operation == "nop":
            pointer += 1
        if operation == "jmp":
            pointer += argument
        if operation == "acc":
            accumulator += argument
            pointer += 1
    return accumulator, success
#_______________________________________________________
def part2(instructions):
    for i in range(len(instructions)):
        if "jmp" in instructions[i]:
            accumulator, success = runprogram(instructions, i)
            if success:
                return accumulator, success
        if "nop" in instructions[i]:
            accumulator, success = runprogram(instructions, i)
            if success:
                return accumulator, success


def main():
    input = get_input()
    print(part1(input))
    print(part2(input))

main()
