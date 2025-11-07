def is_var(x):
    return isinstance(x, str) and x.islower()

def is_const(x):
    return isinstance(x, str) and x[:1].isupper()

def occurs_in(v, expr, subst):
    if v == expr:
        return True
    if isinstance(expr, list):
        return any(occurs_in(v, part, subst) for part in expr)
    if expr in subst:
        return occurs_in(v, subst[expr], subst)
    return False

def mgu(a, b, subst=None, depth=0):
    pad = "  " * depth
    if subst is None:
        print(pad + "No substitution available. Fail.")
        return None

    print(pad + f"Unify {a} with {b} | subst={subst}")

    if a == b:
        print(pad + "Same terms. Keep subst.")
        return subst

    if is_var(a):
        return bind_var(a, b, subst, depth)

    if is_var(b):
        return bind_var(b, a, subst, depth)

    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            print(pad + "Arity mismatch. Fail.")
            return None
        for u, v in zip(a, b):
            subst = mgu(u, v, subst, depth + 1)
            if subst is None:
                print(pad + "Element unification failed.")
                return None
        return subst

    print(pad + "Incompatible atoms/structures. Fail.")
    return None

def bind_var(v, x, subst, depth):
    pad = "  " * depth
    if v in subst:
        print(pad + f"{v} already mapped; unify {subst[v]} with {x}")
        return mgu(subst[v], x, subst, depth + 1)
    if is_var(x) and x in subst:
        print(pad + f"{x} already mapped; unify {v} with {subst[x]}")
        return mgu(v, subst[x], subst, depth + 1)
    if occurs_in(v, x, subst):
        print(pad + f"Occurs-check: {v} in {x}. Fail.")
        return None
    print(pad + f"Extend: {v} -> {x}")
    subst[v] = x
    return subst

expr1 = ['f', 'X', ['g', 'Y']]
expr2 = ['f', 'a', ['g', 'b']]

print("Starting Unification:\n")
result = mgu(expr1, expr2, subst={})
print("\nFinal Unification Result:", result)
