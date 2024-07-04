# MSS (Multiple Screen Shots) for Screen Capture
from mss import mss
# Sending commands
import pydirectinput
# Image Recognition
import cv2
# Process game over screen
import pytesseract
import numpy as np
from matplotlib import pyplot as plt
import time
from gym import Env
from gym.spaces import Box, Discrete

from scripts.WebGame import WebGame

env = WebGame()

for episode in range(10):
    obs = env.reset()
    done = False
    total_reward = 0

    while not done:
        obs, reward, done, info = env.step(env.action_space.sample())
        total_reward += reward
    print("Episode {}: Total Reward: {}".format(episode, total_reward))
