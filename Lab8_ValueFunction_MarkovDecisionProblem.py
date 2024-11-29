import numpy as np

grid = [
    ["S", " ", " ", " "],
    [" ", "W", " ", " "],
    [" ", " ", " ", "+"],
    [" ", " ", " ", "-"],
]

terminal_states = {(3, 3): -1, (2, 3): 1}

gamma = 0.9
theta = 1e-4

action_prob = {"intended": 0.8, "perpendicular": 0.1}

actions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

v = None  
pi = None  

def get_next_state(r, c, action):
    dr, dc = actions[action]
    new_r, new_c = r + dr, c + dc
    if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] != "W":
        return new_r, new_c
    return r, c

def value_iteration(r_s):
    global v, pi 
    
    rows, cols = len(grid), len(grid[0])
    v = np.zeros((rows, cols)) 
    
    iteration = 0
    while True:
        delta = 0
        new_v = np.copy(v)
        iteration += 1
        for r in range(rows):
            for c in range(cols):
                if (r, c) in terminal_states:
                    new_v[r, c] = terminal_states[(r, c)]
                    continue
                action_values = []
                for action in actions:

                    intended_state = get_next_state(r, c, action)
                    left_state = get_next_state(r, c, list(actions.keys())[(list(actions.keys()).index(action) + 1) % 4])
                    right_state = get_next_state(r, c, list(actions.keys())[(list(actions.keys()).index(action) - 1) % 4])

                    value = (
                        action_prob["intended"] * v[intended_state] +
                        action_prob["perpendicular"] * v[left_state] +
                        action_prob["perpendicular"] * v[right_state]
                    )
                    action_values.append(r_s + gamma * value)
                new_v[r, c] = max(action_values)  
                delta = max(delta, abs(new_v[r, c] - v[r, c]))
        v = new_v
        if delta < theta:  
            break
    
    pi = np.full((rows, cols), None)
    for r in range(rows):
        for c in range(cols):
            if (r, c) in terminal_states:
                pi[r, c] = None
                continue
            action_values = {}
            for action in actions:
                intended_state = get_next_state(r, c, action)
                left_state = get_next_state(r, c, list(actions.keys())[(list(actions.keys()).index(action) + 1) % 4])
                right_state = get_next_state(r, c, list(actions.keys())[(list(actions.keys()).index(action) - 1) % 4])
                value = (
                    action_prob["intended"] * v[intended_state] +
                    action_prob["perpendicular"] * v[left_state] +
                    action_prob["perpendicular"] * v[right_state]
                )
                action_values[action] = r_s + gamma * value
            pi[r, c] = max(action_values, key=action_values.get) 
    return v, pi, iteration


while True:
    try:
        reward_input = input("\nEnter reward value for non-terminal states (or type 'exit' to quit): ")
        if reward_input.lower() == "exit":
            print("Exiting the program.")
            break

        reward = float(reward_input)

        print(f"\nResults for r(s) = {reward}:\n")

        v, pi, iterations = value_iteration(reward)

        print("Optimal Value Function:")
        print(np.round(v, 2))

        print("\nOptimal Policy:")
        for row in pi:
            print(row)

    except ValueError:
        print("Invalid input! Please enter a valid numeric reward or type 'exit'.")


# Where:----------------->>>>>>>>>>>>>
# grid: The grid representing the environment (start 'S', walls 'W', terminal states)
# terminal_states: The dictionary storing terminal state positions and their rewards
# gamma: Discount factor (0.9)
# theta: Convergence threshold for value iteration (1e-4)
# action_prob: Probabilities for intended and perpendicular actions
# actions: Directions of movement (up, down, left, right)
# v: Value function (stores the value of each state)
# pi: Policy (stores the optimal action for each state)