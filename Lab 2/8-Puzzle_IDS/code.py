goal = [[1,2,3],[4,5,6],[7,8,0]]
moves = [(-1,0),(1,0),(0,-1),(0,1)]

def find_zero(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return i, j

def neighbors(s):
    x, y = find_zero(s)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            ns = [r[:] for r in s]
            ns[x][y], ns[nx][ny] = ns[nx][ny], ns[x][y]
            yield ns

def dls(s, depth, visited):
    if s == goal:
        return [s]
    if depth == 0:
        return None
    visited.add(str(s))
    for n in neighbors(s):
        if str(n) not in visited:
            path = dls(n, depth - 1, visited)
            if path:
                return [s] + path
    return None

def ids(start, limit=20):
    for d in range(limit + 1):
        path = dls(start, d, set())
        if path:
            return path
    return None

# Example
start = [[1,2,3],[4,0,6],[7,5,8]]
sol = ids(start)
if sol:
    print("Solved in", len(sol) - 1, "moves")
    for step in sol:
        for r in step:
            print(r)
        print("----")
else:
    print("No solution")
