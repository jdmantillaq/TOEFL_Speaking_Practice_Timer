import pandas as pd
import random
import threading
import time
from pynput import keyboard
import warnings
from playsound import playsound

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

# Function to display the countdown timer and play sound when time is over


def countdown_timer(seconds, sound_file):
    for remaining in range(seconds, 0, -1):
        print(f"\rTime remaining: {remaining} seconds", end='')
        time.sleep(1)
    print()  # Move to the next line after countdown
    # Play sound when the time is over
    playsound(sound_file)

# Function to handle the question asking process


def ask_question(df):
    global exit_program
    n_questions = len(df)

    while not exit_program:
        idx = random.randint(0, n_questions - 1)
        question = df.iloc[idx, 0]

        # ANSI escape code for yellow
        yellow = '\033[33m'
        reset = '\033[0m'

        print('-' * 150)
        print(f'\t{yellow}Question {idx + 1:03}: {question}{reset}')
        print('-' * 150)
        print('\n')

        user_input = input("\t\tPress 'Enter' to continue with the question.\n"
                           "\t\tWrite 'next' to skip the current question.\n"
                           "\t\tOr press 'Escape' to exit the code: "
                           ).strip().upper()

        if user_input == 'EXIT' or user_input == 'SALIR':
            break

        if user_input == 'NEXT':
            continue

        if user_input == '':
            print('\n\tPrepare your answer.....')
            playsound('level-up.mp3')

            # Start the countdown timers sequentially
            countdown_timer(15, 'level-up.mp3')  # Preparation time

            print('\n\tAnswer the question.....')
            countdown_timer(45, 'level-up.mp3')  # Answer time

# Main function


def main():
    # Start the keyboard listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    try:
        questions_file = 'toefl_speaking_q1.txt'

        # Read the file and create a DataFrame
        with open(questions_file, 'r') as file:
            lines = file.readlines()
        df = pd.DataFrame(lines, columns=['Question'])

        ask_question(df)
    except FileNotFoundError:
        print(f"File {questions_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Stop the listener
        listener.stop()


if __name__ == "__main__":
    main()
