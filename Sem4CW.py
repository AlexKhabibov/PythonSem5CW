# Задача 1
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
# = 0, a1
# = 1, ak
# = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def fib(n):
#     if n in (0, 1):
#         return 1
#     else:
#         return fib (n-1) + fib(n-2)
# print (fib(7))
    

# Вариант 2
# def fibonacci(a):
# if a in (1, 2):
# return 1
# return fibonacci(a - 1) + fibonacci(a - 2)
# print(fibonacci(int(input("Введите число: "))))

# Вариант препода Славы:
# def fib(n):
#     if n in [0, 1]:
#         return 1
#     return fib (n-1) + fib (n-2)
# print (fib(7))

# Задача 2

# n = list(map(int, input().split()))

# def hacker(n):
#     maxx = max(n)
#     minn = min(n)
#     for i in range(len(n)):
#         if n[i] == maxx:
#             n[i] = minn
#     return n
# print (*hacker(n))            

# Задача 3
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def check_div(n):
#     if n < 4:
#         return 'YES'
    
#     for i in range (2, n//2 + 1):
#         if n % i == 0:
#             return 'NO'
#     return 'YES'

# n = int(input())
# print(check_div(n))

# Вариант 2
# def prost (n):
# count = 0
# for i in range(2,n):
# if n%i==0:
# count+=1

# return count == 0

# a = int(input())

# print(prost(a))

# Можно избавиться от else
# def prost(n):
# if n > 10:
# return 'qqqqq'
# else:
# return 'wwwww'

# def prost(n):
# if n > 10:
# return 'qqqqq'
# return 'wwwww'

# Задача 4
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def sort_f(n):
#     s = input()
#     if n != 1:
#         sort_f(n -1)
#     print(s, end=' ')

# n = int(input())
# sort_f(n)

# Вариант 2:
# def func(n):
#     number = input()
#     if n == 1:
#         return number
#     return func(n - 1) + " " + number


# print(func(2))