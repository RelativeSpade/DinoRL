import time

import cv2
import numpy as np
import pydirectinput
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
        self.done_location = {'top': 350, 'left': 2550, 'width': 660, 'height': 70}

    # Called to do something in the game
    def step(self, action: int):
        # Action key - 0 = JUMP, 1 = DOWN, 2 = NOOP
        action_map = {
            0: 'SPACE',
            1: 'DOWN',
            2: 'NOOP'
        }

        if action != 2:
            pydirectinput.press(action_map[action])

        # Checking whether game is done
        done, done_cap = self.get_done()
        # Get next observation
        new_observation = self.get_observation()
        # Reward - we get a point for every frame we're alive
        reward = 1
        info = {}

        return new_observation, reward, done, info

    # Restart the game
    def reset(self):
        time.sleep(1)
        pydirectinput.click(2130, 150)
        pydirectinput.press('SPACE')
        return self.get_observation()

    # Closes the game
    def close(self):
        cv2.destroyAllWindows()

    # Visualize the Game
    def render(self, **kwargs):
        frame = np.array(self.cap.grab(self.game_location))

        cv2.imshow('Game', frame)

        time.sleep(0.01)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.close()

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
