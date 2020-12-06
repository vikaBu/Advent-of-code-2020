def format_passport_input(input_string):
    passport = {}
    lines = [line.strip() for line in input_string.strip().split("\n") if line.strip()]

    for line in lines:
        for part in line.split(" "):
            key, value = part.split(":")
            passport[key] = value

    return passport

def make_list_of_passports(input_string):
    return [format_passport_input(part) for part in input_string.split("\n\n") if part.strip()]

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def check_validity(passport, fields = fields):
    return all(field in passport for field in fields)

with open('input.txt') as f:
    list_of_passports = make_list_of_passports(f.read())
    print(sum(check_validity(passport) for passport in list_of_passports))