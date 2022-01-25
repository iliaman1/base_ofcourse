# 1 task
mas = input().split()
# Вот здесь разместите свой код
mas.reverse()
# Конец вашего кода
print(*mas)

# 2 task
a = list(map(int, input().split()))
print(a.count(999))

# 3 task
a = list(input().upper())
a = '-'.join(a)
a = a.replace('- -',' ')
print(a)

# 4 task
print('\n'.join(list(map(str, input().split()))))

# 5 task
a = list(map(str, input().split()))
print(f'{a[2]} {a[0][0]}.{a[1][0]}.')
