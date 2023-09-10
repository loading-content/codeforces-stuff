s = input()
total = sum(1 for i in s)
upper = sum(1 for i in s if i.isupper())
lower = total - upper
if upper > lower:
  print(s.upper())
else:
  print(s.lower())
