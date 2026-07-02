from collections import deque


def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    memo = [[0] * m for _ in range(n)]

    answer = n * m

    def get_border():
        visited = [[0] * m for _ in range(n)]
        q = deque()

        for y in range(n):
            for x in range(m):
                if (y == 0 or x == 0 or y == n - 1 or x == m - 1) and memo[y][x] == 1:
                    visited[y][x] = 1
                    q.append((y, x))

            dy = [-1, 1, 0, 0]
            dx = [0, 0, -1, 1]

            while q:
                cy, cx = q.popleft()
                for i in range(4):
                    ny, nx = dy[i] + cy, dx[i] + cx
                    if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
                    if memo[ny][nx] != 1: continue
                    if visited[ny][nx] == 1: continue

                    visited[ny][nx] = 1
                    q.append((ny, nx))

        return visited

    def is_border(board, y, x):
        if y == 0 or x == 0 or y == n - 1 or x == m - 1:
            return True

        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        for i in range(4):
            ny, nx = dy[i] + y, dx[i] + x
            if board[ny][nx] == 1:
                return True

        return False

    for request in requests:
        if len(request) == 2:
            delete_w = request[0]
            for y in range(n):
                for x in range(m):
                    if memo[y][x] == 1: continue
                    if storage[y][x] == delete_w:
                        memo[y][x] = 1
                        answer -= 1

        else:
            board = get_border()
            for y in range(n):
                for x in range(m):
                    if board[y][x] == 1: continue
                    if not is_border(board, y, x): continue
                    if storage[y][x] == request:
                        memo[y][x] = 1
                        answer -= 1

    return answer
