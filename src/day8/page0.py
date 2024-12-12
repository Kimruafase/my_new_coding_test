# day8 > page0.py

import sys

def p0():
    a, b, c, d, e, f = map(int, sys.stdin.readline().split())

    """
    ax + by = c
    dx + ey = f

    ax = c - by
    dx = f - ey

    (c - by) / a  = (f - ey) / d
    cd - bdy = af - aey
    (ae - bd)y = af - cd
    y = (af - cd) / (ae - bd)
    x = (c - by) / a
      = (c - b((af - cd) / (ae - bd))) / a 
    """
    for i in range(-999, 1000):
        for j in range(-999, 1000):
            if (a * i) + (b * j) == c and (d * i) + (e * j) == f:
                print(i, j)


# p0()

def p1():
    n = int(sys.stdin.readline())

    stack = []

    for _ in range(n):
        command = sys.stdin.readline().strip()

        if command.startswith("push"):
            _, value = command.split()
            stack.append(int(value))
            print(stack)
        elif command == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif command == "size":
            print(len(stack))
        elif command == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif command == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)

# p1()

def p2():
    n = int(sys.stdin.readline())

    queue = []

    for _ in range(n):
        command = sys.stdin.readline().strip()

        if command.startswith("push"):
            _, value = command.split()
            queue.append(value)

        elif command == "pop":
            if queue:
                print(queue.pop(0))
            else:
                print(-1)

        elif command == "size":
            print(len(queue))

        elif command == "empty":
            if queue:
                print(0)
            else:
                print(1)

        elif command == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)

        elif command == "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)

# p2()

def p3():
    n = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().strip().split()))
    pre_sum = 0
    result = 0
    for i in range(len(num) - 1):
        pre_sum += num[i]
        result += num[i + 1] * pre_sum

    print(result)

# p3()

def p4():
    n, m, v = map(int, sys.stdin.readline().split()) # n : 정점, m : 간선, v : 시작 노드

    # 리스트 컴프리헨션을 통해서 1줄에 [0]을 (n + 1)개 만큼 생성하고
    # 반복문을 (n + 1)번 돌려서 n + 1 줄만큼의 2차원 배열 생성
    graph = [[0] * (n + 1) for _ in range(n + 1)]

    # 간선만큼의 입력 받기
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = graph[b][a] = 1

    visited0 = [0] * (n + 1)
    visited1 = visited0.copy()

    def dfs(v):
        visited0[v] = 1
        print(v, end = " ")
        for i in range(1, n + 1):
            if graph[v][i] == 1 and visited0[i] == 0:
                dfs(i)

    def bfs(v):
        queue = [v]
        visited1[v] = 1

        while queue:
            v = queue.pop(0)
            print(v, end=" ")
            for i in range(1, n + 1):
                if graph[v][i] == 1 and visited1[i] == 0:
                    queue.append(i)
                    visited1[i] = 1


    dfs(v)
    print()
    bfs(v)

# p4()

def p5():
    n = int(sys.stdin.readline())
    a, b = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline())

    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)

    result = []

    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    def dfs(v, num):
        num += 1
        visited[v] = 1

        if v == b:
            result.append(num)

        for i in graph[v]:
            if visited[i] == 0:
                dfs(i, num)

    dfs(a, 0)
    if len(result) == 0:
        print(-1)
    else:
        print(result[0] - 1)

# p5()

def p6():
    str = sys.stdin.readline().strip()
    i = 0
    new_str = ""

    while i < len(str):
        if str[i : i + 4] == "XXXX":
            new_str += "AAAA"
            i += 4
        elif str[i : i + 2] == "XX":
            new_str += "BB"
            i += 2
        elif str[i] == "X":
            new_str = -1
            break
        else:
            new_str += str[i]
            i += 1

    print(new_str)

# p6()

def p7():
    n, m = map(int, sys.stdin.readline().split())
    dict = {}

    for i in range(1, n+1):
        pokemon = sys.stdin.readline().rstrip()
        dict[i] = pokemon
        dict[pokemon] = i

    for _ in range(m):
        question = sys.stdin.readline().rstrip()
        if question.isdigit():
            print(dict[int(question)])
        else:
            print(dict[question])

# p7()

"""
방향 없는 그래프가 주어졌을 때, 
연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. 
(1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 
(1 ≤ u, v ≤ N, u ≠ v) 
같은 간선은 한 번만 주어진다.
"""
def p8():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    count = 0

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    def dfs(v):
        visited[v] = 1
        for i in graph[v]:
            if visited[i] == 0:
                dfs(i)

    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i)
            count += 1

    print(count)

# p8()

def p9():
    t = int(sys.stdin.readline())

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = [(x, y)]
        graph[x][y] = 0

        while queue:
            x, y = queue.pop(0)

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = 0

    for _ in range(t):
        n, m, k = map(int, sys.stdin.readline().split())
        graph = [[0] * m for _ in range(n)]
        count = 0

        for _ in range(k):
            x, y = map(int, sys.stdin.readline().split())
            graph[x][y] = 1

        for i in range(n):
            for j in range(m):
                if graph[i][j] == 1:
                    bfs(i, j)
                    count += 1

        print(count)

p9()
