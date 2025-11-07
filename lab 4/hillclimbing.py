import random

def display(board):
    n = len(board)
    for i in range(n):
        print(" ".join("Q" if board[i] == j else "." for j in range(n)))
    print()

def conflicts(board):
    n = len(board)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                count += 1
    return count

def best_move(board):
    n = len(board)
    best = list(board)
    best_val = conflicts(board)
    for r in range(n):
        for c in range(n):
            if board[r] != c:
                temp = list(board)
                temp[r] = c
                val = conflicts(temp)
                if val < best_val:
                    best_val = val
                    best = temp
    return best, best_val

def hill_climb(n):
    state = [random.randint(0, n - 1) for _ in range(n)]
    cost = conflicts(state)
    print("Initial Board:")
    display(state)
    print(f"Initial Cost: {cost}\n")
    step = 1
    while True:
        nxt, nxt_cost = best_move(state)
        print(f"Step {step}:")
        print("Current Board:")
        display(state)
        print(f"Current Cost: {cost}")
        print(f"Best Neighbor Cost: {nxt_cost}\n")
        if nxt_cost >= cost:
            break
        state, cost = nxt, nxt_cost
        step += 1
    print("Final Board:")
    display(state)
    print(f"Final Cost: {cost}")
    if cost == 0:
        print("Goal State Reached!")
    else:
        print("Stuck in Local Minimum!")

hill_climb(4)
