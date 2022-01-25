# 1 task
a = input().upper()
print(a)

# 2 task
print(input().lower())

# 3 task
s = input()
print(s.count('e') + s.count('E'))

# 4 task
s = input()
s = s.replace('w', '')
s = s.replace('z', '')
print(s)

# 5 task
print(input().find('a'))

# 6 task
print(input().rfind('a'))

# 7 task
print(len(input().split()))

# 8 task
print(','.join(input().split()))

# 9 task
s = input()
new = s.lower().replace('a', '').replace('o', '').replace('y', '').replace('e', '').replace('u', '').replace('i', '')
print('.' + '.'.join(new))
