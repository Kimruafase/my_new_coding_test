# day6 > page0.py

import sys

def string_find():
    s = sys.stdin.readline()
    i = int(sys.stdin.readline())

    for j, a in enumerate(s):
        if i - 1 == j:
            print(a)

# string_find()

def string_count():
    s = sys.stdin.readline()
    print(len(s) - 1)

string_count()