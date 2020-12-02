def parse_input(file):
  data = [[]]
  with open(file) as f:
    for line in f:
      data.append(line.strip().split(" "))

  return data

def part1(data):
  count = 0
  for d in data:
    if not d:
      continue

    min_occ = int(d[0].split("-")[0])
    max_occ = int(d[0].split("-")[1])
   
    c = d[2].count(d[1].strip(':'))

    if c <= max_occ and c >= min_occ:
      count += 1

  return count

def part2(data):
  count = 0
  for d in data:
    if not d:
      continue

    pos1 = int(d[0].split("-")[0])
    pos2 = int(d[0].split("-")[1])

    c = d[1].strip(':')

    if (d[2][pos1-1] == c or d[2][pos2-1] == c) and d[2][pos1-1] != d[2][pos2-1]:
      count +=1

  return count

if __name__ == "__main__":

  test_data = parse_input("test_data.txt")
  data      = parse_input("input.txt")

  assert(part1(test_data) == 2)

  answer1 = part1(data)
  print("Answer 1 is: " + str(answer1))


  assert(part2(test_data) == 1)

  answer2 = part2(data)
  print("Answer 2 is: " + str(answer2))
