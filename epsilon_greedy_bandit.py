import numpy as np

class BinaryBanditProblem:
    def __init__(self, prob_A, prob_B, epsilon, total_steps):
        self.prob_A = prob_A
        self.prob_B = prob_B
        self.epsilon = epsilon
        self.total_steps = total_steps
        self.Q = [0, 0]
        self.N = [0, 0]
        self.rewards = []

    def get_reward(self, action):
        if action == 1:
            return 1 if np.random.rand() < self.prob_A else 0
        else:
            return 1 if np.random.rand() < self.prob_B else 0

    def select_action(self):
        if np.random.rand() < self.epsilon:
            return np.random.choice([1, 2])  
        else:
            return np.argmax(self.Q) + 1  

    def update(self, action, reward):
        index = action - 1 
        self.N[index] += 1
        self.Q[index] = self.Q[index] + (1 / self.N[index]) * (reward - self.Q[index])

    def run(self):
        for t in range(self.total_steps):
            action = self.select_action()
            reward = self.get_reward(action)
            self.rewards.append(reward)
            self.update(action, reward)

    def print_results(self):
        print(f"Estimated value for action 1 (A): {self.Q[0]:.3f}")
        print(f"Estimated value for action 2 (B): {self.Q[1]:.3f}")

prob_A = float(input("Enter the reward probability for action 1 (0 to 1): "))
prob_B = float(input("Enter the reward probability for action 2 (0 to 1): "))
epsilon = float(input("Enter the exploration rate (epsilon, 0 to 1): "))
total_steps = int(input("Enter the total number of steps: "))

binary_bandit = BinaryBanditProblem(prob_A=prob_A, prob_B=prob_B, epsilon=epsilon, total_steps=total_steps)
binary_bandit.run()
binary_bandit.print_results()
