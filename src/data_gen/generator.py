import os
import random
from datetime import datetime, timedelta
from src.data_gen.metrics import calculate_session_metrics
from src.data_gen.profiles import generate_user_profile
from src.utils.io import save_json


def generate_dataset(
    num_users: int = 5, days: int = 30, output_dir: str = "data"
):
    """Orchestrateur de la génération de données JSON."""
    start_date = datetime(2026, 1, 1)

    for uid in range(1, num_users + 1):
        profile = generate_user_profile(uid)
        history = []

        workout_prob = {
            "beginner": 0.45,
            "intermediate": 0.65,
            "athlete": 0.85,
        }[profile["fitness_level"]]

        for d in range(days):
            date_str = (start_date + timedelta(days=d)).strftime("%Y-%m-%d")

            if random.random() <= workout_prob:
                metrics = calculate_session_metrics(profile)
                session = {"date": date_str, "completed": True, **metrics}
            else:
                session = {
                    "date": date_str,
                    "completed": False,
                    "duration_min": 0,
                    "avg_hr": profile["resting_hr"],
                    "reps_completed": 0,
                    "form_errors": 0,
                    "calories_burned": 0,
                    "met": 1.0,
                }
            history.append(session)

        filepath = os.path.join(output_dir, f"user_{uid}_data.json")
        save_json({"profile": profile, "history": history}, filepath)

    print(f"✅ {num_users} fichiers utilisateurs sauvegardés dans '{output_dir}/'.")