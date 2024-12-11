#day7 > page0.py

import sys

def p1():
    N = int(sys.stdin.readline())
    s = []

    for _ in range(N):
        r = int(input())
        s.append(r)

    s.sort()

    for i in s:
        print(i)

# p1()

def p2():
    N = int(sys.stdin.readline())
    count = 0

    while N > 0 :
        if N % 5 == 0:
            count += N // 5
            break

        N -= 2
        count += 1

    if N < 0:
        print(-1)
    else:
        print(count)

# p2()

def p3():
    n = int(sys.stdin.readline())
    end = 0
    count = 0
    array = []

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().strip().split())
        array.append([a, b])

    array.sort(key=lambda x : (x[1], x[0]))

    for start_time, end_time in array:
        if end <= start_time:
            count += 1
            end = end_time

    print(count)

# p3()

def p4():
    n = int(sys.stdin.readline())
    count = 0

    while n > 0:
        if n % 5 == 0:
            count += n // 5
            break
        n -= 3
        count += 1

    if n < 0:
        print(-1)
    else:
        print(count)

p4()


