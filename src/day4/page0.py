# day5 > page0.py - 1차원 배열
import sys


def count_int():
    n = int(input())
    count = 0
    numbers = list(map(int, input().split()))

    v = int(input())
    for i in numbers:
        if i == v:
            count += 1
    print(count)

# count_int()

def comparison_num():
    n, x = map(int, sys.stdin.readline().split())
    s = []
    a = list(map(int, sys.stdin.readline().split()))

    for i in a:
        if x > i:
            s.append(i)

    print(*s)

# comparison_num()

def max_min_search():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    x = a[0]
    s = []

    for i in a:
        if x > i:
            x = i
    s.append(x)

    for i in a:
        if x < i:
            x = i
    s.append(x)

    print(*s)

# max_min_search()



            # 20 10 35 30 7
            # 1 -> 20
            # 2 -> 20
            # 3 -> 35
            # 4 -> 35
            # 5 -> 35