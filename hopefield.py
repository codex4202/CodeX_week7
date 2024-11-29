import numpy as np

class SarahHopfield:
    def __init__(self, sarah_n):  # Fixed '__init__' method
        self.sarah_w = np.zeros((sarah_n, sarah_n))

    def sarah_train(self, sarah_patterns):
        for sarah_p in sarah_patterns:
            self.sarah_w += np.outer(sarah_p, sarah_p)
        np.fill_diagonal(self.sarah_w, 0)  # Set self-connections to 0

    def sarah_recall(self, sarah_p, sarah_iter=100):
        for _ in range(sarah_iter):
            sarah_p = np.sign(self.sarah_w @ sarah_p)  # Update pattern state
            sarah_p[sarah_p == 0] = 1  # Ensure binary outputs
        return sarah_p

    def sarah_test(self, sarah_patterns, sarah_noise=0.1):
        sarah_correct = sum(
            np.array_equal(self.sarah_recall(self.sarah_add_noise(sarah_p, sarah_noise)), sarah_p)
            for sarah_p in sarah_patterns
        )
        return sarah_correct / len(sarah_patterns) * 100  # Return recall accuracy

    @staticmethod
    def sarah_add_noise(sarah_p, sarah_noise):
        sarah_p = sarah_p.copy()  # Avoid modifying the original pattern
        sarah_p[np.random.choice(len(sarah_p), int(sarah_noise * len(sarah_p)), replace=False)] *= -1
        return sarah_p

if __name__ == "__main__":
    sarah_patterns = [np.random.choice([-1, 1], size=100) for _ in range(3)]
    sarah_net = SarahHopfield(100)
    sarah_net.sarah_train(sarah_patterns)
    print(f"Sarah Accuracy: {sarah_net.sarah_test(sarah_patterns):.2f}%")
