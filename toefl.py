#%%
import time
from playsound import playsound
import warnings

# Mute all warnings
warnings.filterwarnings("ignore")


def countdown_timer(seconds, sound_file='level-up.mp3', intro_time=None):
    # ANSI escape code for yellow
    reset = '\033[0m'
    orange = '\033[38;2;255;165;0m'
    # Countdown loop
    for i, remaining in enumerate(range(seconds, 0, -1)):
        minutes, sec = divmod(remaining, 60)
        time_str = f'{minutes:02}:{sec:02}'
        time_str = f'{time_str} min' if minutes else f'{time_str} sec'
        if intro_time is not None and intro_time == i:
            print(f"\r{orange}Time remaining: {time_str}{reset}", end='')
        else:
            print(f"\rTime remaining: {time_str}", end='')
        time.sleep(1)
    print()  # Move to the next line after countdown
    # Play sound when the time is over
    playsound(sound_file)