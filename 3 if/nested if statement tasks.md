# 1 task
### В данной задаче необходимо сравнить два целых числа A и B. Они поступают на вход программе отдельно в каждой строке.
### Ваша задача вывести символ "<", если A меньше B, ">", если A больше B и "=", если A=B.
| Sample Input | Sample Output |
|--------------|---------------|
| `5` `9`      | `<`           |
| `2` `1`      | `>`           |
| `7` `7`      | `=`           |
___


# 2 task
### Даны три целых числа, каждое записано в отдельной строке.
### Нужно вывести значение наибольшего из данных чисел
### Примечание: используйте только условный оператор, функцией max пользоваться нельзя
| Sample Input | Sample Output |
|--------------|---------------|
| `5` `7` `21` | `21`          |
___


# 3 task
### На свой день рождения Петя купил красивый и вкусный торт, который имел идеально круглую форму. Петя не знал, сколько гостей придет на его день рождения, поэтому вынужден был разработать алгоритм, согласно которому он сможет быстро разрезать торт на N равных частей. Следует учесть, что разрезы торта можно производить как по радиусу, так и по диаметру.
### Помогите Пете решить эту задачу, определив наименьшее число разрезов торта по заданному числу гостей.
### **Входные данные**
### Программа получает на вход натуральное число N – число гостей, включая самого виновника торжества
### **Выходные данные**
### Выведите минимально возможное число разрезов торта.
| Sample Input | Sample Output |
|--------------|---------------|
| `2`          | `1`           |
| `3`          | `3`           |
___


# 4 task
### В отделе работают 3 сотрудника, которые получают заработную плату в рублях. Требуется определить: на сколько зарплата самого высокооплачиваемого из них отличается от самого низкооплачиваемого.
### **Входные данные**
### Размеры зарплат всех сотрудников вводятся в одну строку через пробел. Каждая заработная плата – это натуральное число, не превышающее 105. И гарантируется ,что все зарплаты различны
### **Выходные данные**
### Необходимо вывести одно целое число — разницу между максимальной и минимальной зарплатой.
### Примечание: функциями min и max пользоваться нельзя, мы же условный оператор изучаем)
| Sample Input       | Sample Output |
|--------------------|---------------|
| `100` `500` `1000` | `900`         |
| `40` `30` `35`     | `10`          |
___


# 5 task
### Маленький Петя очень любит подарки. Его мама подарила ему на день рождения две строки равной длины, состоящие из больших и маленьких букв латинского алфавита. Теперь Петя хочет сравнить эти строки лексикографически. При этом регистр букв значения не имеет, то есть большая буква считается эквивалентной соответствующей маленькой букве. Помогите Пете выполнить сравнение.
### **Входные данные**
### В каждой из первых двух строк записано по одной подаренной строке. Длина строк находится в пределах от 1 до 100 включительно. Гарантируется, что строки имеют одинаковую длину, а также состоят из больших и маленьких букв латинского алфавита.
### **Выходные данные**
### Если первая строка меньше второй, выведите «-1». Если вторая строка меньше первой, выведите «1». Если строки равны, выведите «0». Учтите, что регистр букв не учитывается при сравнении.
| Sample Input         | Sample Output |
|----------------------|---------------|
| `aaaa` `aaaA`        | `0`           |
| `abs` `Abz`          | `-1`          |
| `abcdefg` `AbCdEfF`  | `1`           |
___


# 6 task
## Кнопочные гонки
### Двое решили посоревноваться в набирании текстов на сайте «Кнопочные гонки». Во время соревнования необходимо ввести текст из s символов. Первый участник набирает один символ за v1 миллисекунд и имеет пинг t1 миллисекунд. Второй участник набирает один символ за v2 миллисекунд и имеет пинг t2 миллисекунд.
### При соединении с пингом (задержкой) в t миллисекунд соревнование проходит для участника следующим образом:
### Ровно через t миллисекунд после начала соревнования участник получает текст, который необходимо ввести.
### Сразу после этого он начинает вводить этот текст.
### Ровно через t миллисекунд после того, как он перепечатал весь текст, сайт получает информацию об этом.
### Победителем в соревновании является тот участник, информация об успехе которого пришла раньше. Если информация пришла от обоих участников одновременно, считается, что произошла ничья.
### По данной длине текста и информации об участниках, определите исход игры.
### **Входные данные**
### Первая строка содержит пять целых чисел s, v1, v2, t1, t2 (1 <= s, v<sub>1</sub>, v<sub>2</sub>, t<sub>1</sub>, t<sub>2</sub> <= 1000) — количество символов в тексте, скорость набора текста первым участником, скорость набора текста вторым участником, пинг первого участника и пинг второго участника.
### **Выходные данные**
### Если выиграет первый участник, выведите «First». Если выиграет второй участник, выведите «Second». В случае ничьей выведите «Friendship».
| Sample Input | Sample Output |
|--------------|---------------|
| `5 1 2 1 2`  | `First`       |
| `3 3 1 1 1`  | `Second`      |
| `4 5 3 1 5`  | `Friendship`  |
___


# 7 task
### При игре в "Города" игроки по очереди называют названия городов так, чтобы первая буква каждого нового слова совпадала с последней буквой предыдущего. При этом считают, что если последняя буква предыдущего слова — мягкий знак, то с первой буквой следующего слова надо сравнивать букву, предшествующую мягкому знаку.
### Напишите программу, которая считывает подряд две строки, после чего выводит «Good», если последний символ первой строки совпадает с первым символом второй (с учётом правила про мягкий знак), и «Bad» в противном случае.
| Sample Input         | Sample Output |
|----------------------|---------------|
| `Лондон` `Норильск`  | `Good`        |
| `Тверь` `Роттердам`  | `Good`        |