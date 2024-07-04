from gym import Env


class WebGame(Env):
    # Setup the environment
    def __init__(self):
        pass

    # Called to do something in the game
    def step(self, action):
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
