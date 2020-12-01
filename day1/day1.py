data = []

with open("input.txt") as input_data:
  for entry in input_data:
    data.append(int(entry.strip()))

# part 1
for i in range(len(data)):
  for j in range(i,len(data)):
    if data[i]+data[j] == 2020:
      print(data[i]*data[j])

# part 2
for i in range(len(data)):
  for j in range(i,len(data)):
    for k in range(j,len(data)):
      if data[i]+data[j]+data[k] == 2020:
        print(data[i]*data[j]*data[k])
