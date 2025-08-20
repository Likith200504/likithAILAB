import random

environment = {
    "A": random.choice(["Clean", "Dirty"]),
    "B": random.choice(["Clean", "Dirty"])
}

def simple_reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"

def goal_based_agent(env):
    actions = []
    for location in ["A", "B"]:
        if env[location] == "Dirty":
            actions.append((location, "toClean"))
            env[location] = "Clean"
    return actions


def run_simulation():
    print("Initial Environment:", environment)

    location = random.choice(["A", "B"])
    action = simple_reflex_agent(location, environment[location])
    print(f"Reflex Agent at {location} sees {environment[location]} -> Action: {action}")

    actions = goal_based_agent(environment.copy())
    print("Goal-Based Agent Actions:", actions)

run_simulation()
