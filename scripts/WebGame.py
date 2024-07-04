import numpy as np
from gym import Env
from gym.spaces import Box, Discrete


class WebGame(Env):
    # Setup the environment
    def __init__(self):
        # Subclass
        super().__init__()
        # Setup spaces
        self.observation_space = Box(low=0, high=255, shape=(1, 83, 100), dtype=np.uint8)
        self.action_space = Discrete(3)

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
        pass

    # Get the "Game Over" text
    def get_done(self):
        pass
