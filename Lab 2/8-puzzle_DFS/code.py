goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

moves = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    x, y = find_zero(state)
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def dfs(state, visited):
    if state == goal:
        return [state]

    visited.add(str(state))

    for neighbor in get_neighbors(state):
        if str(neighbor) not in visited:
            path = dfs(neighbor, visited)
            if path:
                return [state] + path
    return None

# Example
start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

solution = dfs(start, set())

if solution:
    print("Solution found in", len(solution) - 1, "moves:")
    for step in solution:
        for row in step:
            print(row)
        print("----")
else:
    print("No solution found")
