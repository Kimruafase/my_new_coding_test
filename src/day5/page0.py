# day5 > page0.py

import sys

def max_find():
    s = []
    index = 0
    for i in range(0, 9):
        a = int(sys.stdin.readline())
        s.append(a)
    a0 = s[0]
    for i, a in enumerate(s):
        if a0 <= a:
            a0 = a
            index = i + 1
    print(a0)
    print(index)

# max_find()

def shoot_ball():
    n, m = map(int, sys.stdin.readline().split())
    basket = [0 for i in range(n)]
    for _ in range(m):
        i, j, k = map(int, sys.stdin.readline().split())
        for a in range(i - 1, j):
            basket[a] = k

    print(*basket)

# shoot_ball()

def change_basket_num():
    n, m = map(int, sys.stdin.readline().split())
    basket = [i + 1 for i in range(n)]
    b = 0

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        b = basket[i - 1]
        basket[i - 1] = basket[j - 1]
        basket[j - 1] = b

    print(*basket)

# change_basket_num()

def find_num():
    call_num = []
    non_call_num = []
    check_num = [i + 1 for i in range(30)]


    for i in range(28):
        num = int(sys.stdin.readline())
        call_num.append(num)

    for num in check_num:
        if num not in call_num:
            non_call_num.append(num)

    for i in range(len(non_call_num)):
        j = len(non_call_num) - i
        for k in range(1, j):
            if non_call_num[k - 1] >= non_call_num[k]:
                n = non_call_num[k - 1]
                non_call_num[k - 1] = non_call_num[k]
                non_call_num[k] = n

    for num in non_call_num:
        print(num)

# find_num()

def find_mod():
    mod_result = []
    find_same_value = []
    for i in range(10):
        a = int(sys.stdin.readline())
        mod_result.append(a % 42)

    for i in mod_result:
        if i not in find_same_value:
            find_same_value.append(i)
    print(len(find_same_value))

# find_mod()

def print_desc():
    n, m = map(int, sys.stdin.readline().split())
    basket = [i + 1 for i in range(n)]
    print(basket)
    desc = []
    for i in range(m):
        i, j = map(int, sys.stdin.readline().split())
        for a in range(j - 1, i - 2, -1):
            print(a)
            desc.append(basket[a])
            print(desc)

        for b, c in enumerate(range(i - 1, j)):
            print(b)
            basket[c] = desc[b]
            print(basket)

        desc = []

    print(*basket)

# print_desc()

def test_avg_new():
    n = int(sys.stdin.readline())
    result = list(map(int, sys.stdin.readline().split()))
    max_value = result[0]
    new_result = []
    sum = 0
    for i in result:
        if max_value <= i:
            max_value = i

    for i in result:
        new_result.append((i / max_value) * 100)

    for i in new_result:
        sum += i

    print(sum / len(new_result))

test_avg_new()