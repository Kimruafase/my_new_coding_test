# day02 > page0.py - 조건문

def comparison():
    A, B = map(int, input().split())

    if A > B:
        print(">")
    elif A < B:
        print("<")
    elif A == B:
        print("==")

# comparison()

def test_grade():
    a = int(input())

    if a >= 90:
        print("A")
    elif a >= 80:
        print("B")
    elif a >= 70:
        print("C")
    elif a >= 60:
        print("D")
    else:
        print("F")

# test_grade()

def leaf_year():
    year = int(input())

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("1")
    else:
        print("0")

# leaf_year()

def quadrant():
    x = int(input())
    y = int(input())

    if x > 0 and y > 0:
        print("1")
    elif x > 0 and y < 0:
        print("4")
    elif x < 0 and y < 0:
        print("3")
    else:
        print("2")

# quadrant()

def alarm():
    hour, min = map(int, input().split())

    if hour == 0 and min < 45:
        hour = 23
    elif min < 45:
        hour -= 1

    if min < 45:
        min += 15
    elif min >= 45:
        min -= 45

    print(f'{hour} {min}')


# alarm()

def oven_time_cal():
    hour, min = map(int, input().split())
    end_time = int(input())

    if min + end_time >= 60:
        if hour + ((min + end_time) // 60) >= 24:
            hour = ((min + end_time) // 60) - 24 + hour
        else:
            hour += ((min + end_time) // 60)
        min = (min + end_time) % 60
    else:
        min = min + end_time

    print(f'{hour} {min}')

# oven_time_cal()

def three_dice():
    a, b, c = map(int, input().split())

    if a == b == c:
        print(10000 + a * 1000)
    elif a == b:
        print(1000 + a * 100)
    elif b == c:
        print(1000 + b * 100)
    elif c == a:
        print(1000 + a * 100)
    else:
        if a > b:
            print(a * 100)
        elif b > c:
            print(b * 100)
        else:
            print(c * 100)

three_dice()