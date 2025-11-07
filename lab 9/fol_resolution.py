# -*- coding: utf-8 -*-
from copy import deepcopy

U = {
    'a': "∀x: food(x) → likes(John, x)",
    'b': "food(Apple) ∧ food(Vegetables)",
    'c': "∀x∀y: eats(x, y) ∧ ¬killed(x) → food(y)",
    'd': "eats(Anil, Peanuts) ∧ alive(Anil)",
    'e': "∀x: eats(Anil, x) → eats(Harry, x)",
    'f': "∀x: ¬killed(x) → alive(x)",
    'g': "∀x: alive(x) → ¬killed(x)",
    'h': "likes(John, Peanuts)"
}

print("=== STEP 1: Given FOL Statements ===")
for k, v in U.items():
    print(f"{k}. {v}")

print("\n=== STEP 2: After Removing Implications ===")

S1 = {
    'a': "¬food(x) ∨ likes(John, x)",
    'b1': "food(Apple)",
    'b2': "food(Vegetables)",
    'c': "¬eats(x, y) ∨ killed(x) ∨ food(y)",
    'd1': "eats(Anil, Peanuts)",
    'd2': "alive(Anil)",
    'e': "¬eats(Anil, x) ∨ eats(Harry, x)",
    'f': "killed(x) ∨ alive(x)",
    'g': "¬alive(x) ∨ ¬killed(x)",
    'h': "likes(John, Peanuts)"
}

for k, v in S1.items():
    print(f"{k}. {v}")

print("\n=== STEP 3: Standardized Variables (Dropped Quantifiers) ===")
for k, v in S1.items():
    print(f"{k}. {v}")

print("\n=== STEP 4: Final CNF Clauses ===")

KB_cnf = [
    "¬food(x) ∨ likes(John, x)",
    "food(Apple)",
    "food(Vegetables)",
    "¬eats(y, z) ∨ killed(y) ∨ food(z)",
    "eats(Anil, Peanuts)",
    "alive(Anil)",
    "¬eats(Anil, w) ∨ eats(Harry, w)",
    "killed(g) ∨ alive(g)",
    "¬alive(k) ∨ ¬killed(k)",
    "likes(John, Peanuts)"
]

for i, c in enumerate(KB_cnf, 1):
    print(f"{i}. {c}")

print("\n=== STEP 5: Resolution Proof ===")

proof = [
    ("1", "Negate the Goal", "¬likes(John, Peanuts)"),
    ("2", "Resolve (1) with (¬food(x) ∨ likes(John, x)) using {x/Peanuts}", "¬food(Peanuts)"),
    ("3", "Resolve (2) with (¬eats(y,z) ∨ killed(y) ∨ food(z)) using {z/Peanuts}", "¬eats(y,Peanuts) ∨ killed(y)"),
    ("4", "Resolve (3) with (eats(Anil, Peanuts)) using {y/Anil}", "killed(Anil)"),
    ("5", "Resolve (4) with (¬alive(k) ∨ ¬killed(k)) using {k/Anil}", "¬alive(Anil)"),
    ("6", "Resolve (5) with (alive(Anil))", "⊥ (Contradiction)")
]

for step_id, desc, out in proof:
    print(f"Step {step_id}: {desc}")
    print(f"      ⇒ {out}\n")

print("Contradiction reached ⇒ Therefore, John likes Peanuts is TRUE.\n")
