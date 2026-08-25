def compute_reward(
    completion_rate: float, hr_simulated: int, hr_target_range: tuple
) -> float:
    """Calcule la récompense (Reward) accordée à l'agent RL."""
    reward = completion_rate * 10.0
    min_hr, max_hr = hr_target_range

    if min_hr <= hr_simulated <= max_hr:
        reward += 5.0
    elif hr_simulated > max_hr:
        reward -= 4.0
    else:
        reward -= 2.0

    return reward