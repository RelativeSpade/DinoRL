import time

import numpy as np
from stable_baselines3 import DQN

from scripts.GetLatestModel import get_latest_model
from scripts.WebGame import WebGame

CHECKPOINT_DIR = '../trains'

LATEST_MODEL, NUM = get_latest_model(CHECKPOINT_DIR)

env = WebGame()

model = DQN.load(LATEST_MODEL, env)
total_reward = 0
for episodes in range(10):
    obs = env.reset()
    done = False
    while not done:
        action, _ = model.predict(obs)

        if isinstance(action, np.ndarray):
            action = action.item()

        obs, reward, done, info = env.step(action)
        time.sleep(0.05)
        total_reward += reward
    print('Total Reward for episode {} is {}'.format(episodes, total_reward))
    print('Mean: {}'.format(total_reward / (episodes + 1)))
    time.sleep(2)
