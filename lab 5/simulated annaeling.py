import random
import math

def show_board(queens):
    size = len(queens)
    for r in range(size):
        row = ["Q" if queens[r] == c else "." for c in range(size)]
        print(" ".join(row))
    print()

def conflicts(queens):
    size = len(queens)
    conflict_count = 0
    for r1 in range(size):
        for r2 in range(r1 + 1, size):
            same_col = queens[r1] == queens[r2]
            same_diag = abs(queens[r1] - queens[r2]) == abs(r1 - r2)
            if same_col or same_diag:
                conflict_count += 1
    return conflict_count

def get_random_neighbor(queens):
    size = len(queens)
    new_board = queens[:]
    row = random.randrange(size)
    col = random.randrange(size)
    new_board[row] = col
    return new_board

def anneal(n, start_temp=100, cooling=0.95, min_temp=1):
    current = [random.randrange(n) for _ in range(n)]
    energy = conflicts(current)
    temp = start_temp
    iteration = 1

    print("Initial Configuration:")
    show_board(current)
    print(f"Initial Conflicts: {energy}\n")

    while temp > min_temp and energy > 0:
        candidate = get_random_neighbor(current)
        next_energy = conflicts(candidate)
        delta = next_energy - energy

        if delta < 0 or random.random() < math.exp(-delta / temp):
            current = candidate
            energy = next_energy

        print(f"Iteration {iteration}: Temp={temp:.2f}, Conflicts={energy}")
        temp *= cooling
        iteration += 1

    print("\nFinal Configuration:")
    show_board(current)
    print(f"Final Conflicts: {energy}")

    if energy == 0:
        print("✅ Solution Found!")
    else:
        print("⚠️ Stopped before finding a solution.")

anneal(8)
