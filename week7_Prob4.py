import numpy as np
import matplotlib.pyplot as plt

class nonStatBandit:
    def __init__(self, k=10):
        self.k = k
        self.q_true = np.zeros(k)
        self.q_estimates = np.zeros(k)
        self.action_counts = np.zeros(k)
        self.epsilon = 0.1
        self.alpha = 0.1  # Step-size parameter for non-stationary rewards

    def get_reward(self, action):
        # Simulate non-stationary rewards by changing the true reward
        self.q_true += np.random.normal(0, 0.01, self.k)
        reward = np.random.normal(self.q_true[action], 1)
        return reward

    def select_action(self):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.k)
        else:
            return np.argmax(self.q_estimates)

    def update_estimates(self, action, reward):
        # Exponentially weighted average for non-stationary rewards
        self.q_estimates[action] += self.alpha * (reward - self.q_estimates[action])

    def run(self, steps):
        rewards = np.zeros(steps)
        for step in range(steps):
            action = self.select_action()
            reward = self.get_reward(action)
            self.update_estimates(action, reward)
            rewards[step] = reward
        return rewards

# Simulation setup
steps = 10000
bandit = nonStatBandit()
rewards = bandit.run(steps)

# Plotting results
plt.plot(np.cumsum(rewards) / (np.arange(steps) + 1))
plt.xlabel('Steps')
plt.ylabel('Average Reward')
plt.title('Modified Epsilon-Greedy Agent in Non-Stationary Bandit Problem')
plt.show()
