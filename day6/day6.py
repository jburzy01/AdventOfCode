import collections

def parse_input(input_file):
  customs_data = []
  with open(input_file) as f:
    party_responses = []
    party_size = 0

    for line in f:
      if line.strip():
        for response in line.strip():
          party_responses.append(response)
        party_size += 1
      else:
        customs_data.append((party_size,party_responses.copy()))
        party_responses.clear()
        party_size = 0

    customs_data.append((party_size,party_responses.copy()))

  return customs_data

def part1(customs_data):

  count = 0
  for entry in customs_data:
    count += len(set(entry[1]))

  return count

def part2(customs_data):

  count = 0
  for entry in customs_data:
    count += len([item for item, freq in collections.Counter(entry[1]).items() if freq == entry[0]])

  return count

if __name__ == "__main__":
  customs_data = parse_input("input.txt")
  test_data = parse_input("test.txt")

  assert(part1(test_data) == 11)
  assert(part2(test_data) == 6)

  answer1 = part1(customs_data)
  answer2 = part2(customs_data)
  print(f"The answer to part one is: {answer1}")
  print(f"The answer to part two is: {answer2}")

