import numpy as np
import pytest
from src.rl_engine.agent import QLearningAgent
from src.rl_engine.environment import FitnessEnvironment


def test_agent_initialization():
    agent = QLearningAgent(num_states=3, num_actions=3)
    assert agent.q_table.shape == (3, 3)
    assert agent.epsilon == 1.0


def test_agent_learning_update():
    agent = QLearningAgent(num_states=3, num_actions=3, alpha=0.5, gamma=0.9)
    initial_q = agent.q_table[0, 1]

    # Simulation d'un pas d'apprentissage
    agent.learn(state=0, action=1, reward=10.0, next_state=1)

    # La valeur Q doit avoir augmenté
    assert agent.q_table[0, 1] > initial_q


def test_environment_step():
    env = FitnessEnvironment(max_steps=5)
    state = env.reset()
    assert state == 1

    next_state, reward, done = env.step(action=1)
    assert isinstance(next_state, int)
    assert isinstance(reward, float)
    assert done is False