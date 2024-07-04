import cv2
import numpy as np
from gym import Env
from gym.spaces import Box, Discrete
from mss import mss
from pytesseract import pytesseract
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class WebGame(Env):
    # Setup the environment
    def __init__(self):
        # Subclass
        super().__init__()
        # Setup spaces
        self.observation_space = Box(low=0, high=255, shape=(1, 83, 100), dtype=np.uint8)
        self.action_space = Discrete(3)
        # Define extraction parameters
        self.cap = mss()
        self.game_location = {'top': 300, 'left': 1920, 'width': 600, 'height': 500}
        self.done_location = {'top': 355, 'left': 2550, 'width': 660, 'height': 70}

    # Called to do something in the game
    def step(self, action):
        # Action key - 0 = JUMP, 1 = DOWN, 2 = NOOP
        pass

    # Restart the game
    def reset(self):
        pass

    # Closes the game
    def close(self):
        pass

    # Visualize the Game
    def render(self, **kwargs):
        pass

    # Get a segment of game to observe
    def get_observation(self):
        # Get screen capture of game
        raw = np.array(self.cap.grab(self.game_location))[:, :, :3].astype(np.uint8)
        # Grayscale
        gray = cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY)
        # Resize
        resized = cv2.resize(gray, (100, 83))
        # Add channels first
        channel = np.reshape(resized, (1, 83, 100))
        return channel

    # Get the "Game Over" text
    def get_done(self):
        # Get done screen
        done_cap = np.array(self.cap.grab(self.done_location))[:, :, :3].astype(np.uint8)
        # Valid done text
        done_strings = ['GAME', 'GAHE']

        done = False
        res = pytesseract.image_to_string(done_cap)[:4]
        if res in done_strings:
            done = True

        return done, done_cap
