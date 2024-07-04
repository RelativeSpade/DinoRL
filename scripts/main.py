import pygetwindow as gw
from stable_baselines3 import DQN
from GetLatestModel import get_latest_model
from scripts.TrainAndLoggingCallback import TrainAndLoggingCallback
from scripts.WebGame import WebGame


def is_dino_tab_active():
    active_window = gw.getActiveWindow()
    if active_window:
        return 'chrome://dino/' in active_window.title
    return False


if is_dino_tab_active():
    print(f'Dino is open')
    env = WebGame()

    CHECKPOINT_DIR = '../trains'
    LOG_DIR = '../logs'

    callback = TrainAndLoggingCallback(check_freq=1000, save_path=CHECKPOINT_DIR)

    LATEST_MODEL, NUM = get_latest_model(CHECKPOINT_DIR)

    if LATEST_MODEL is None:
        model = DQN('CnnPolicy', env, tensorboard_log=LOG_DIR, verbose=1, buffer_size=1200000, learning_starts=1000)
    else:
        model = DQN.load(LATEST_MODEL, env)

    model.learn(total_timesteps=100000, callback=callback)
else:
    print(f'Dino is not open')
