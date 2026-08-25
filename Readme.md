# 🏋️‍♂️ SmartFit-RL: Reinforcement Learning Fitness Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Q--Learning-green.svg)]()
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-orange.svg)](https://peps.python.org/pep-0008/)
[![Tests](https://img.shields.io/badge/Tests-Pytest-yellow.svg)](https://docs.pytest.org/)

**SmartFit-RL** est un moteur d'optimisation d'entraînements sportifs basé sur le **Reinforcement Learning (RL)**. Il combine un pipeline de **génération de données synthétiques (Data Engineering)** avec un **agent Q-Learning** capable d'ajuster dynamiquement l'intensité des séances d'entraînement selon la réponse physiologique de l'utilisateur (fréquence cardiaque, fatigue, complétion).

---

## 🎯 Utilité et Objectifs du Projet

- **🤖 Personal Trainer Virtuel :** Adaptation dynamique de la difficulté des exercices pour maximiser les gains sans surentraînement.
- **🛡️ Sécurité & Santé :** Intégration d'une fonction de récompense (*Reward Function*) pénalisant les zones de fréquence cardiaque à risque.
- **📊 Données Synthétiques (RGPD-compliant) :** Simulation de profils sportifs et d'historiques complets sans dépendre de données médicales réelles confidentielles.
- **🏗️ Architecture Modulaire :** Séparation nette entre Data Engineering, Environnement Gym-like, Agent RL et Tests.

---

## 📂 Architecture du Projet

```text
fitness-rl-project/
├── data/                         
├── notebooks/                    
│   └── 01_fitness_agent.ipynb
├── src/                          
│   ├── data_gen/                 
│   │   ├── generator.py
│   │   ├── metrics.py
│   │   └── profiles.py
│   ├── rl_engine/               
│   │   ├── agent.py
│   │   ├── environment.py
│   │   └── rewards.py
│   └── utils/                   
│       ├── io.py
│       └── visualization.py
├── tests/                        
│   ├── test_agent.py
│   └── test_data_gen.py
├── .gitignore
├── main.py                       
├── README.md                     
└── requirements.txt              