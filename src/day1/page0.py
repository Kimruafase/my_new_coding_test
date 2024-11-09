# day1 > page0.py - 입출력과 사칙연산1

######
def summary():
    A, B = map(int, input().split(" "))

    if 0 >= A:
        return
    if B >= 10:
        return

    print(A + B)

# summary()

def subtract():
    A, B = map(int, input().split(" "))

    if 0 >= A:
        return
    if B >= 10:
        return

    print(A - B)

# subtract()


def multiple():
    A, B = map(int, input().split(" "))

    if 0 >= A:
        return
    if B >= 10:
        return

    print(A * B)

# multiple()

def divide():
    A, B = map(int, input().split(" "))

    if 0 >= A:
        return
    if B > 10:
        return

    print(A / B)

# divide()

def operation():
    A, B = map(int, input().split(" "))

    if 0 >= A:
        return
    if B >= 10:
        return

    print(A + B)
    print(A - B)
    print(A * B)
    print(A // B)
    print(A % B)

# operation()