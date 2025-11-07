import itertools
import re

def interpret(formula, assignment):
    s = formula.replace("<->", " == ")
    s = s.replace("->", " <= ")
    s = re.sub(r'~(\w+)', r'(not \1)', s)
    s = re.sub(r'~\(([^)]+)\)', r'(not (\1))', s)
    s = s.replace("^", " and ")
    s = s.replace("v", " or ")
    for sym, val in assignment.items():
        s = re.sub(r'\b' + re.escape(sym) + r'\b', str(val), s)
    return eval(s)

def tt_entails(kb, query, symbols):
    ok = True
    assignments = list(itertools.product([True, False], repeat=len(symbols)))
    print("Truth Table Evaluation:\n")
    header = " | ".join(symbols) + " | KB | Query | KB ⇒ Query"
    print(header)
    print("-" * (len(header) * 2))
    for values in assignments:
        model = dict(zip(symbols, values))
        kb_val = interpret(kb, model)
        q_val = interpret(query, model)
        implies = (not kb_val) or q_val
        if kb_val and not q_val:
            ok = False
        row = " | ".join('T' if v else 'F' for v in values)
        row += f" | {'T' if kb_val else 'F'}  | {'T' if q_val else 'F'}   | {'T' if implies else 'F'}"
        print(row)
    print("\nResult:")
    if ok:
        print("The Knowledge Base entails the Query (KB ⊨ Query)")
    else:
        print("The Knowledge Base does NOT entail the Query (KB ⊭ Query)")

kb = "(Q -> P) ^ (P -> ~Q) ^ (Q v R)"
syms = ["P", "Q", "R"]
qs = ["R", "R -> P", "Q -> R"]

for q in qs:
    print(f"\nEvaluating Query: {q}\n")
    tt_entails(kb, q, syms)
    print("\n" + "=" * 50 + "\n")
