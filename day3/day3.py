import numpy

def load_input(filename):
  
  grid = []

  with open(filename) as f:
    for line in f:
      row = []
      for ch in line.strip():
        row.append(ch)
      grid.append(row)

  return grid

def compute_collisions(xstep,ystep):
  grid = load_input("input.txt")
  count = 0
  x = 0
  y = 0

  rows = len(grid)
  cols = len(grid[0])

  while(y < rows):
    x = x % cols

    if(grid[y][x] == '#'):
      count += 1

    x += xstep
    y += ystep

  return count

if __name__ == "__main__":

  print(compute_collisions(3,1))

  print(numpy.prod(list(map(lambda x: compute_collisions(*x), [(1,1),(3,1),(5,1),(7,1),(1,2)]))))
