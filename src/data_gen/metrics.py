import random
import numpy as np


def calculate_session_metrics(profile: dict) -> dict:
    """Calcule le MET, la FC moyenne et les calories brûlées pour une session."""
    duration_min = random.randint(25, 60)
    hr_target = profile["resting_hr"] + 0.6 * (
        profile["max_hr"] - profile["resting_hr"]
    )
    avg_hr = int(np.random.normal(hr_target, scale=8))
    avg_hr = min(max(avg_hr, profile["resting_hr"] + 15), profile["max_hr"])

    met = round(random.uniform(4.0, 9.0), 1)
    calories = round(
        (met * 3.5 * profile["weight_kg"] / 200) * duration_min, 1
    )

    return {
        "duration_min": duration_min,
        "avg_hr": avg_hr,
        "reps_completed": random.randint(40, 120),
        "form_errors": random.randint(0, 5),
        "calories_burned": calories,
        "met": met,
    }