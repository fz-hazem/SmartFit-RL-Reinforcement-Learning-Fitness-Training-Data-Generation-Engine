import random
from src.rl_engine.rewards import compute_reward


class FitnessEnvironment:
    """Environnement Gym-like simulant l'entraînement."""

    def __init__(self, hr_target_range=(130, 160), max_steps=14):
        self.hr_target_range = hr_target_range
        self.max_steps = max_steps
        self.reset()

    def reset(self) -> int:
        self.current_step = 0
        self.state = 1
        return self.state

    def step(self, action: int):
        self.current_step += 1

        if action == 0:  # Easy
            hr_simulated = random.randint(100, 125)
            completion = random.uniform(0.9, 1.0)
            fatigue_delta = -1
        elif action == 1:  # Medium
            hr_simulated = random.randint(126, 155)
            completion = random.uniform(0.75, 0.95)
            fatigue_delta = 0
        else:  # Hard
            hr_simulated = random.randint(156, 185)
            completion = random.uniform(0.50, 0.80)
            fatigue_delta = 1

        reward = compute_reward(completion, hr_simulated, self.hr_target_range)
        self.state = max(0, min(2, self.state + fatigue_delta))
        done = self.current_step >= self.max_steps

        return self.state, reward, done