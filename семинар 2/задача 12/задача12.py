# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и 
# их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

x, y = int(input("Введите число -> ")), int(input("Введите число -> "))


for i in range(x + y):
    for j in range(x + y):
        if i + j == x and i * j == y:
            print(i, j)
            break