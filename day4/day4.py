import re 

def parse_input(input_file):

  passport_list = []

  with open(input_file) as f:
    entry = {}

    lines = f.readlines()
    last = lines[-1]

    for line in lines:
      pairs = line.split()
      for pair in pairs:
        key = pair.split(":")[0]
        val = pair.split(":")[1]

        entry[key] = val

      if not line.strip():
        passport_list.append(entry)
        entry = {}
      if line == last:
        passport_list.append(entry)

  return passport_list

def part1(passports):
  
  count = 0
  valid_keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']

  for entry in passports:
    is_valid = True
    for key in valid_keys:
      if key not in entry and key != 'cid':
        is_valid = False

    if is_valid:
      count += 1

  return count

def part2(passports):

  count = 0
  valid_keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']

  for entry in passports:
    has_keys = True
    for key in valid_keys:
      if key not in entry and key != 'cid':
        has_keys = False

    if has_keys:
      is_valid = True
      for key, val in entry.items():
        # byr (Birth Year) - four digits; at least 1920 and at most 2002
        if key == 'byr':
          if not 1920 <= int(val) <= 2002:
            is_valid = False
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020
        elif key == 'iyr':
          if not 2010 <= int(val) <= 2020:
            is_valid = False
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        elif key == 'eyr':
          if not 2020 <= int(val) <= 2030:
            is_valid = False

        # hgt (Height) - a number followed by either cm or in:
        #  If cm, the number must be at least 150 and at most 193.
        #  If in, the number must be at least 59 and at most 76.
        # this isn;t it
        elif key == 'hgt':
          re_hgt = re.compile("([0-9]+)([a-zA-Z]+)") 

          if re_hgt.match(val):
            res  = re_hgt.match(val).groups() 
            mag  = int(res[0])
            unit = res[1]

            if unit == "in" and not 59 <= mag <= 76:
              is_valid = False
            if unit == "cm" and not 150 <= mag <= 193:
              is_valid = False
            if unit != 'in' and unit != 'cm':
              is_valid = False
          else:
            is_valid = False

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        # this isn't it
        elif key == 'hcl':
          if val[0] != '#':
            is_valid = False
          if not len(val) == 7:
            is_valid = False
          if not re.match('^[0-9a-fA-F]+$',val[1:]):
            is_valid = False

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth
        elif key == 'ecl':
          if not val in ['amb','blu','brn','gry','grn','hzl','oth']:
            is_valid = False

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        elif key == 'pid':
          if len(val) != 9 or not re.match('^[0-9]+$',val):
            is_valid = False

      if is_valid:
        count += 1

  return count

if __name__ == "__main__":
  passports = parse_input("input.txt")

  answer1 = part1(passports)
  answer2 = part2(passports)

  print(f'Part 1 answer is: {answer1}')
  print(f'Part 2 answer is: {answer2}')
