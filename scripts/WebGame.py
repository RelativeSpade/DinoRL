import numpy as np
from gym import Env
from gym.spaces import Box, Discrete
from mss import mss


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
        self.game_location = {'top': 300, 'left': 0, 'width': 600, 'height': 500}
        self.done_location = {'top': 405, 'left': 630, 'width': 660, 'height': 70}

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
    def render(self):
        pass

    # Get a segment of game to observe
    def get_observation(self):
        # Get screen capture of game
        raw = np.array(self.cap.grab(self.game_location))

        pass

    # Get the "Game Over" text
    def get_done(self):
        pass
