import matplotlib.pyplot as plt


def plot_rewards(rewards: list, title: str = "Évolution des Récompenses"):
    """Génère le graphique de convergence de l'agent RL."""
    plt.figure(figsize=(8, 4))
    plt.plot(range(1, len(rewards) + 1), rewards, marker="o", color="#1f77b4")
    plt.title(title)
    plt.xlabel("Épisodes")
    plt.ylabel("Récompense Totale")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()