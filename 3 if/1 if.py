# 1 task
a = int(input())
if a < 20000:
    print(a)
else:
    print(a - a * 0.13)

# 2 task
a = input()
if a == 'Python':
    print('ДА')
else:
    print('НЕТ')

# 3 task
a, b = int(input()), int(input())
if a > b:
    print(a)
else:
    print(b)

# 4 task
a = input()
if a == a[::-1]:
    print('YES')
else:
    print('NO')

# 5 task
a, b, c = map(int, input().split())
if a + b == c:
    print('YES')
else:
    print('NO')

# 6 task
a, b = input(), input()
if a[::-1] == b:
    print('YES')
else:
    print('NO')

# 7 task
a, b, c = int(input()), int(input()), int(input())
if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')

# 8 task
a = int(input())
if a // 100000 % 10 + a // 10000 % 10 + a // 1000 % 10 == a // 100 % 10 + a // 10 % 10 + a % 10:
    print('YES')
else:
    print('NO')

# 9 task
a = input()

b = input()

x = 'abcdefgh'

if (x.index(a[0]) + int(a[1])) % 2 == (x.index(b[0]) + int(b[1])) % 2:
    print('YES')

else:
    print('NO')

# 10 task
a = int(input())
if a % 2 == 0:
    print(a // 2)
else:
    print(-(a // 2 + 1))
