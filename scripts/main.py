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

from scripts import GetLatestModel
from scripts.TrainAndLoggingCallback import TrainAndLoggingCallback
from scripts.WebGame import WebGame
from stable_baselines3 import DQN

env = WebGame()

CHECKPOINT_DIR = '../trains'
LOG_DIR = '../logs'

callback = TrainAndLoggingCallback(check_freq=1000, save_path=CHECKPOINT_DIR)

LATEST_MODEL, NUM = GetLatestModel

if LATEST_MODEL is None:
    model = DQN('CnnPolicy', env, tensorboard_log=LOG_DIR, verbose=1, buffer_size=1200000, learning_starts=1000)
else:
    model = DQN.load(LATEST_MODEL, env)

    model.learn(total_timesteps=100000, callback=callback)
