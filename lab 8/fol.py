# -*- coding: utf-8 -*-
from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt

KB = [
    {"if": ["American(p)", "Weapon(q)", "Sells(p, q, r)", "Hostile(r)"], "then": "Criminal(p)"},
    {"if": ["Missile(x)"], "then": "Weapon(x)"},
    {"if": ["Enemy(x, America)"], "then": "Hostile(x)"},
    {"if": ["Missile(x)", "Owns(A, x)"], "then": "Sells(Robert, x, A)"},
    {"fact": "American(Robert)"},
    {"fact": "Enemy(A, America)"},
    {"fact": "Missile(T1)"},
    {"fact": "Owns(A, T1)"}
]

goal = "Criminal(Robert)"

def split_pred(s):
    name, rest = s.split("(", 1)
    args = rest[:-1].split(",")
    return name.strip(), [a.strip() for a in args]

def sym_is_var(t):
    return t[0].islower()

def match_terms(a, b, theta=None):
    if theta is None:
        theta = {}
    p1, args1 = split_pred(a)
    p2, args2 = split_pred(b)
    if p1 != p2 or len(args1) != len(args2):
        return None
    for u, v in zip(args1, args2):
        if u == v:
            continue
        if sym_is_var(u):
            theta[u] = v
        elif sym_is_var(v):
            theta[v] = u
        else:
            return None
    return theta

def apply(subst, atom):
    name, args = split_pred(atom)
    out = []
    for a in args:
        while a in subst:
            a = subst[a]
        out.append(a)
    return f"{name}({', '.join(out)})"

def fc_prove(kb, q):
    facts = {e["fact"] for e in kb if "fact" in e}
    rules = [e for e in kb if "if" in e]
    edges = []

    print("Known facts:")
    for f in facts:
        print(" ", f)
    print()

    changed = True
    while changed:
        changed = False
        for rule in rules:
            prem = rule["if"]
            concl = rule["then"]
            sigma_list = [{}]
            for lit in prem:
                next_sigma = []
                for sig in sigma_list:
                    lit_inst = apply(sig, lit)
                    for f in facts:
                        m = match_terms(lit_inst, f, deepcopy(sig))
                        if m is not None:
                            next_sigma.append(m)
                sigma_list = next_sigma
                if not sigma_list:
                    break
            for sig in sigma_list:
                new_fact = apply(sig, concl)
                if new_fact not in facts:
                    print(f"Derived: {new_fact}")
                    facts.add(new_fact)
                    changed = True
                    for lit in prem:
                        edges.append((apply(sig, lit), new_fact))
                    if match_terms(new_fact, q):
                        print("\nGoal satisfied:", q)
                        draw_inference(edges, q)
                        return True

    print("\nGoal not provable.")
    draw_inference(edges, q)
    return False

def draw_inference(edge_list, target):
    G = nx.DiGraph()
    G.add_edges_from(edge_list)
    plt.figure(figsize=(12, 7))
    pos = nx.spring_layout(G, seed=42)
    colors = ["lightgreen" if n == target else "lightblue" for n in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=2200,
            font_size=10, font_weight="bold", arrows=True, arrowstyle="-|>", arrowsize=12)
    plt.title("Forward Chaining Inference Graph", fontsize=14, fontweight="bold")
    plt.show()

print("\n--- Forward Chaining (FOL-FC-ASK) ---\n")
fc_prove(KB, goal)
