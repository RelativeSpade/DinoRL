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
done, done_cap = env.get_done()

print(done)
plt.imshow(done_cap)
plt.show()
