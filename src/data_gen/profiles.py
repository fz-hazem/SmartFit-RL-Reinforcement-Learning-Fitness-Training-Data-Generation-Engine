import random

FITNESS_LEVELS = ["beginner", "intermediate", "athlete"]
GOALS = ["weight_loss", "muscle_gain", "endurance", "general_fitness"]


def generate_user_profile(user_id: int) -> dict:
    """Génère un profil démographique et physiologique."""
    age = random.randint(18, 60)
    fitness_level = random.choice(FITNESS_LEVELS)

    if fitness_level == "athlete":
        resting_hr = random.randint(50, 60)
    elif fitness_level == "intermediate":
        resting_hr = random.randint(61, 72)
    else:
        resting_hr = random.randint(73, 85)

    return {
        "user_id": user_id,
        "age": age,
        "sex": random.choice(["M", "F"]),
        "weight_kg": round(random.uniform(50.0, 95.0), 1),
        "fitness_level": fitness_level,
        "resting_hr": resting_hr,
        "max_hr": 220 - age,
        "goal": random.choice(GOALS),
    }