import numpy as np


class QLearningAgent:
    """Classe représentant l'agent RL fonctionnant par Q-Learning."""

    def __init__(
        self,
        num_states=3,
        num_actions=3,
        alpha=0.1,
        gamma=0.95,
        epsilon=1.0,
        epsilon_decay=0.95,
    ):
        self.num_actions = num_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.q_table = np.zeros((num_states, num_actions))

    def choose_action(self, state: int) -> int:
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.randint(0, self.num_actions)
        return int(np.argmax(self.q_table[state]))

    def learn(
        self, state: int, action: int, reward: float, next_state: int
    ) -> None:
        best_next = np.argmax(self.q_table[next_state])
        td_target = reward + self.gamma * self.q_table[next_state][best_next]
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.alpha * td_error

    def decay_epsilon(self) -> None:
        self.epsilon = max(0.01, self.epsilon * self.epsilon_decay)