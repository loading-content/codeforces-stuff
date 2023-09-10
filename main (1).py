s = input()
a_count = s.count('a')
letters = 0
for i in s:
    letters += 1

letters_no_a = letters - a_count
if a_count > letters_no_a:
    print(letters)
else:
    a_count -= 1
    for i in range(a_count, letters_no_a):
        letters -= 1
    print(letters)