import math

T = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['L1', 'L2'],
    'E': ['L3', 'L4'],
    'F': ['L5', 'L6'],
    'G': ['L7', 'L8'],
    'L1': 10, 'L2': 9, 'L3': 14, 'L4': 18,
    'L5': 5,  'L6': 4, 'L7': 50, 'L8': 3
}

def banner():
    print("\nGame Tree Structure:\n")
    print("                A [MAX]")
    print("              /        \\")
    print("           B [MIN]       C [MIN]")
    print("          /     \\        /     \\")
    print("       D [MAX]  E [MAX]  F [MAX]  G [MAX]")
    print("      /   \\     /   \\     /   \\     /   \\")
    print("    10    9   14   18   5    4   50    3")
    print("\n--------------------------------------------\n")

def ab(node, depth, a, b, maximizing):
    pad = "  " * depth
    if isinstance(T[node], int):
        print(f"{pad}Leaf {node} -> {T[node]}")
        return T[node]

    if maximizing:
        print(f"{pad}MAX {node} @ depth={depth}, α={a}, β={b}")
        best = -math.inf
        for ch in T[node]:
            print(f"{pad}→ visit {ch}")
            val = ab(ch, depth + 1, a, b, False)
            best = max(best, val)
            a = max(a, val)
            print(f"{pad}MAX update {node}: best={best}, α={a}, β={b}")
            if b <= a:
                print(f"{pad}PRUNE at MAX {node} (β={b} ≤ α={a})")
                break
        return best
    else:
        print(f"{pad}MIN {node} @ depth={depth}, α={a}, β={b}")
        best = math.inf
        for ch in T[node]:
            print(f"{pad}→ visit {ch}")
            val = ab(ch, depth + 1, a, b, True)
            best = min(best, val)
            b = min(b, val)
            print(f"{pad}MIN update {node}: best={best}, α={a}, β={b}")
            if b <= a:
                print(f"{pad}PRUNE at MIN {node} (β={b} ≤ α={a})")
                break
        return best

banner()
print("Starting Alpha-Beta Pruning...\n")
ans = ab('A', 0, -math.inf, math.inf, True)
print("\n--------------------------------------------")
print(f"✅ Best achievable value at root (A): {ans}")
print("--------------------------------------------")
