import pandas as pd
import random
from pynput import keyboard
import warnings
from playsound import playsound
from toefl import countdown_timer


# Mute all warnings
warnings.filterwarnings("ignore")

# Global variable to control program exit
exit_program = False

# Function to detect ESC key press


def on_press(key):
    global exit_program
    if key == keyboard.Key.esc:
        exit_program = True
        return False  # Stop listener


# Function to handle the question asking process
def ask_question():
    global exit_program
    while not exit_program:
        # ANSI escape code for yellow
        yellow = '\033[33m'
        orange = '\033[38;2;255;165;0m'
        reset = '\033[0m'

        print('-' * 100)
        print(f'{yellow}Prepate your exercise...{reset}'.center(100))
        print('-' * 100)
        print('\n')

        user_input = input(
            "\t\tPress 'Enter' to continue answering the question.\n"
            "\t\tOr press 'Escape' and finish with 'Enter' to exit the code: "
        ).strip().upper()

        if user_input == 'EXIT' or user_input == 'SALIR':
            break

        if user_input == '':
            print()
            print(f'{yellow}Read the announcement{reset}'.center(100, '.'))
            playsound('level-up.mp3')

            # Start the countdown timers sequentially
            countdown_timer(45)  # Preparation time

            print()
            print(f'{orange}Play the sound track{reset}'.center(100, '*'))

            u_input = input(
                "\t\tWhen you are done, press 'Enter' to continue answering "
                "the question.\n"
            )

            print(f'{yellow}Prepare your answer{reset}'.center(100, '.'))
            playsound('level-up.mp3')

            # Start the countdown timers sequentially
            countdown_timer(30)  # Preparation time

            print()
            print(f'{yellow}Answer the question{reset}'.center(100, '.'))
            countdown_timer(60, intro_time=15)  # Answer time

# Main function


def main():
    # Start the keyboard listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    try:
        ask_question()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Stop the listener
        listener.stop()


if __name__ == "__main__":
    main()
