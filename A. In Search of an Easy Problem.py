n = int(input())
x = sum(int(x) for x in input().split())
if x != 0:
  print('HARD')
else:
  print('EASY')
