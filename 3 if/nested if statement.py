# 1 task
a, b = int(input()), int(input())
if a < b:
    print('<')
if a > b:
    print('>')
if a == b:
    print('=')

# 2 task
a, b, c = int(input()), int(input()), int(input())
if a > b and a > c:
    print(a)
else:
    if b > a and b > c:
        print(b)
    else:
        print(c)

# 3 task
a = int(input())
if a == 1:
    print(0)
else:
    if a % 2 == 0:
        print(a // 2)
    else:
        print(a)

# 4 task
a, b, c = map(int, input().split())
zmax, zmin = a, b
if a > b and a > c:
    zmax = a
else:
    if b > a and b > c:
        zmax = b
    else:
        zmax = c

if a < b and a < c:
    zmin = a
else:
    if b < a and b < c:
        zmin = b
    else:
        zmin = c
print(zmax - zmin)

# 5 task
a, b = input().lower(), input().lower()
if a == b:
    print(0)
else:
    if a < b:
        print(-1)
    else:
        print(1)

# 6 task
s, v1, v2, t1, t2 = map(int, input().split())
T1 = s * v1 + 2 * t1
T2 = s * v2 + 2 * t2
if T1 < T2:
    print('First')
else:
    if T1 > T2:
        print('Second')
    else:
        print('Friendship')

# 7 task
a, b = input().lower(), input().lower()
if a[-1] == 'ь':
    a = a[-2]
    if a == b[0]:
        print('Good')
    else:
        print('Bad')

else:
    if a[-1] == b[0]:
        print('Good')
    else:
        print('Bad')
