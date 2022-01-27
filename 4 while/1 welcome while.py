# 1 task
i = 1000
while i < 2001:
    print(i)
    i += 1

# 2 task
i = 6785
while i >= 195:
    print(i)
    i -= 5

# 3 task
a, b = map(int, input().split())
count = 0
while a <= b:
    count += 1
    a *= 3
    b *= 2
print(count)

# 4 task
numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6,
           6, 1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9,
           2, 4, 7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4,
           8, 1, 5, 7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5,
           6, 9, 1, 1, 3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2,
           4, 1, 7, 4, 9, 9, 4, 9, 6, 9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0]
# здесь должен быть ваш код
while 4 in numbers:
    numbers.remove(4)
# здесь должен быть ваш код
print(*numbers)

# 5 task
a = input()
while len(a) >= 1:
    print(a)
    a = a[1:-1]

# 6 task
a = int(input())
st = 1
while st ** 2 <= a:
    print(st ** 2)
    st += 1

# 7 task
a, b = map(int, input().split())
d = 1
while a <= b:
    a = a + a * 0.15
    d += 1
print(d)

# 8 task
a, b = map(int, input().split())
den = 0
while a > 0:
    a -= 1
    den += 1
    if den % b == 0:
        a += 1
print(den)

# 9 task
a, b = map(int, input().split())
time = 0
while a > 0:
    a -= 1
    time += 1
    if time % b == 0:
        a += 1
print(time)

# 10 task
a = int(input())
import math

stepen = -1
i = 2
chislo = 0
while math.pow(i, stepen) < a:
    stepen += 1
    chislo = math.pow(i, stepen)

if chislo == a:
    print(stepen)
else:
    print('НЕТ')

# 11 task
a = int(input())
fc = int(str(a)[0])
while fc != 1 and a < 1000000000:
    a = fc * a
    fc = int(str(a)[0])
print(a)
