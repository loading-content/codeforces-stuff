x = int(input())
steps_taken = 0
while x > 0:
  if x >= 5:
    x -= 5
    steps_taken += 1
  elif x >= 4:
    x -= 4
    steps_taken += 1
  elif x >= 3:
    x -= 3
    steps_taken += 1
  elif x >= 2:
    x -= 2
    steps_taken += 1
  elif x >= 1:
    x -= 1
    steps_taken += 1
print(steps_taken)