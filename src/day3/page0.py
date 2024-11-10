# day3 > page0.py - 반복문
import sys


def input_auto_multiple():
    N = int(input())

    for i in range(1, 10):
        print(f'{N} * {i} = {N * i}')

# input_auto_multiple()

def print_A_plus_B():
    N = int(input())

    for i in range(0, N):
        A, B = map(int, input().split())
        print(A + B)

# print_A_plus_B()

def cal_sum():
    n = int(input())
    summ = 0
    for i in range(1, n+1):
        summ += i
    print(summ)

# cal_sum()

def cal_receipt():
    price = int(input())
    sum = 0
    n = int(input())

    for i in range(0, n):
        a, b = map(int, input().split())
        sum += a * b

    if price == sum:
        print("Yes")
    else:
        print("No")

# cal_receipt()

def print_long_int():
    n = int(input())
    m = ""
    for i in range(0, n // 4):
        m += "long "

    print(f'{m}int')

# print_long_int()

def fast_a_plus_b():
    t = int(input())

    for i in range(0, t):
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)

# fast_a_plus_b()

def print_case_a_plus_b():
    n = int(input())

    for i in range(0, n):
        a, b = map(int, sys.stdin.readline().split())
        print(f'Case #{i+1}: {a + b}')

# print_case_a_plus_b()

def print_case2_a_plus_b():
    n = int(input())

    for i in range(0, n):
        a, b = map(int, sys.stdin.readline().split())
        print(f'Case #{i + 1}: {a} + {b} = {a + b}')

# print_case2_a_plus_b()

def print_star0():
    n = int(input())
    star = ""
    for i in range(0, n):
        star += "*"
        print(star)

# print_star0()

def print_star1():
    n = int(input())
    star = ""
    blank = ""
    for i in range(0, n):
        star += "*"
        for j in range(n - i, 1, -1):
            blank += " "
        print(f'{blank}{star}')
        blank = ""

# print_star1()

def print_while_a_plus_b():
    while(True):
        a, b = map(int, sys.stdin.readline().split())
        if a == 0 and b == 0:
            break
        print(a + b)

# print_while_a_plus_b()

def print_while_eof_a_plus_b():

    while(True):
        tmp = sys.stdin.readline().strip()
        if not tmp:
            break
        a, b  = map(int, tmp.split())
        print(a + b)

print_while_eof_a_plus_b()
