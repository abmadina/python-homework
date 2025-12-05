1. def modify_string(txt):
    result = []
    count = 0
    i = 0
    while i < len(txt):
        result.append(txt[i])
        count += 1
        if count == 3:
            # если символ — гласная или уже стоит "_", переносим вставку
            if txt[i] in "aeiou" or (i+1 < len(txt) and txt[i+1] == "_"):
                result.append(txt[i+1])
                i += 1
            if i != len(txt) - 1:  # не добавляем "_" в конце
                result.append("_")
            count = 0
        i += 1
    return "".join(result)

print(modify_string("hello"))       # hel_lo
print(modify_string("assalom"))     # ass_alom
print(modify_string("abcabcabcdeabcdefabcdefg"))  # abc_abcab_cdeabcd_efabcdef_g

2. n = int(input())
for i in range(n):
    print(i**2)

3. i = 1
while i <= 10:
    print(i)
    i += 1
  
  Exercise 2: Паттерн
  for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

Exercise 3: Сумма чисел
num = int(input("Enter number: "))
print("Sum is:", sum(range(1, num+1)))

Exercise 4: Таблица умножения
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n * i)

Exercise 5: Отбор чисел из списка
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num % 5 == 0 and num <= 150:
        print(num)

Exercise 6: Количество цифр
num = 75869
print(len(str(num)))  # 5

Exercise 7: Обратный паттерн
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

Exercise 8: Список в обратном порядке
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)

Exercise 9: От -10 до -1
for i in range(-10, 0):
    print(i)

Exercise 10: Done после цикла
for i in range(5):
    print(i)
print("Done!")

Exercise 11: Простые числа в диапазоне
start, end = 25, 50
for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

Exercise 12: Фибоначчи

n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a+b

Exercise 13: Факториал
num = 5
fact = 1
for i in range(1, num+1):
    fact *= i
print(f"{num}! = {fact}")

4. Return Uncommon Elements of Lists

def uncommon_elements(list1, list2):
    result = []
    for x in list1:
        if x not in list2:
            result.append(x)
    for y in list2:
        if y not in list1:
            result.append(y)
    return result

print(uncommon_elements([1, 1, 2], [2, 3, 4]))          # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))          # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]
