from re import match

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

def is_valid2(passport):
    checks = [
        1920 <= int(passport.get('byr', -1)) <= 2002,
        2010 <= int(passport.get('iyr', -1)) <= 2020,
        2020 <= int(passport.get('eyr', -1)) <= 2030,
        is_valid_height(passport.get('hgt', '')),
        match(r"^#[0-9a-f]{6}$", passport.get('hcl', '')),
        passport.get('ecl') in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        match(r"^[0-9]{9}$", passport.get('pid', ''))
    ]

    return all(checks)

def is_valid_height(height):
    if height.endswith('cm'):
        try:
            return 150 <= int(height[:-2]) <= 193
        except:
            return False
    elif height.endswith("in"):
        try:
            return 59 <= int(height[:-2]) <= 76 
        except:
            return False
    return False

with open('input.txt') as f:
    list_of_passports = make_list_of_passports(f.read())
    print(sum(is_valid2(passport) for passport in list_of_passports))
