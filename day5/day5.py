import math

def parse_input(input_file):
  seat_data = []
  with open(input_file) as f:
    for line in f:
      seat_data.append(line.strip())
  return seat_data

def get_row(binary_data):
  low  = 0
  high = 127
  for partition in binary_data:
    if partition == 'F':
      high = low + math.floor((high-low)/2)
    if partition == 'B':
      low = low + math.ceil((high-low)/2 )

  assert(low == high)
  return low

def get_col(binary_data):
  low  = 0
  high = 7
  for partition in binary_data:
    if partition == 'L':
      high = low + math.floor((high-low)/2)
    if partition == 'R':
      low = low + math.ceil((high-low)/2)

  assert(low == high)
  return low

def part1(seat_data):
  highest = 0
  for entry in seat_data:
    rows = entry[:7]
    cols = entry[7:]
    row, col = get_row(rows), get_col(cols)
    ID = row*8 + col
    if ID > highest:
      highest = ID
  return highest

def part2(seat_data):

  seat_IDs = []
  for entry in seat_data:
    rows = entry[:7]
    cols = entry[7:]
    row, col = get_row(rows), get_col(cols)
    ID = row*8 + col
    seat_IDs.append(ID)

  seat_IDs.sort()

  for row in range(1,127):
    for col in range(0,8):
      ID = row*8 + col
      if ID not in seat_IDs and seat_IDs[0] < ID < seat_IDs[-1]:
        return ID

if __name__ == "__main__":
  seat_data = parse_input("input.txt")

  assert(get_row('BFFFBBF')==70)
  assert(get_col('RRR')==7)

  answer1 = part1(seat_data)
  answer2 = part2(seat_data)
  print(f'The answer to part one is: {answer1}')
  print(f'The answer to part two is: {answer2}')

