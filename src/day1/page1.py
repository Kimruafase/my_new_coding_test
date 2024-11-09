# day1 > page1.py
####

def surprise_print():
    id = input()
    if len(id) > 50:
        return
    print(f"{id}??!")

# surprise_print()

def year_cal_budda():
    year = int(input())
    print(f'{year-543}')

# year_cal_budda()

def A_B_C():
    A, B, C = map(int, input().split())

    print((A + B) % C)
    print(((A % C) + (B % C)) % C)
    print((A * B) % C)
    print(((A % C) * (B % C)) % C)

# A_B_C()

def self_multiple():
    A = int(input())
    B = input()
    print(f'{A * int(B[2])}')
    print(f'{A * int(B[1])}')
    print(f'{A * int(B[0])}')
    print(f'{A * int(B)}')

# self_multiple()

def three_add():
    A, B, C = map(int, input().split())

    print(A + B + C)

# three_add()

def cat():
    print("\    /\\")
    print(" )  ( ')")
    print("(  /  )")
    print(" \\(__)|")

# cat()

def dog():
    print("|\\_/|")
    print("|q p|   /}")
    print("( 0 )\"\"\"\\")
    print("|\"^\"`    |")
    print("||_/=\\\\__|")

# dog()