from src.data_gen.generator import generate_dataset
from src.rl_engine.agent import QLearningAgent
from src.rl_engine.environment import FitnessEnvironment
from src.utils.visualization import plot_rewards


def main():
    print("🚀 --- Lancement de Fitness-RL-Project ---")

    # 1. Génération de Données
    generate_dataset(num_users=3, days=30, output_dir="data")

    # 2. Entraînement de l'Agent RL
    env = FitnessEnvironment()
    agent = QLearningAgent()

    episodes = 50
    rewards_history = []

    for ep in range(episodes):
        state = env.reset()
        total_reward = 0
        done = False

        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.learn(state, action, reward, next_state)
            state = next_state
            total_reward += reward

        agent.decay_epsilon()
        rewards_history.append(total_reward)

    print("✅ Entraînement de l'Agent réussi.")
    print("\nQ-Table finale :")
    print(agent.q_table.round(2))

    # 3. Visualisation
    plot_rewards(rewards_history)


if __name__ == "__main__":
    main()