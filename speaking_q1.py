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
def ask_question(df):
    global exit_program
    n_questions = len(df)
    
    idx_list = []

    while not exit_program:
        idx = random.randint(0, n_questions - 1)
        if idx in idx_list:
            continue
        idx_list.append(idx)
        question = df.iloc[idx, 0]

        # ANSI escape code for yellow
        yellow = '\033[33m'
        reset = '\033[0m'
        

        print('-' * 100)
        print(f'{yellow}Question {idx + 1:03}: {question}{reset}')
        print('-' * 100)
        print('\n')

        user_input = input(
            "\t\tPress 'Enter' to continue answering the question.\n"
            "\t\tWrite 'n' and finish with 'Enter' to skip the current question.\n"
            "\t\tOr press 'Escape' and finish with 'Enter' to exit the code: "
                           ).strip().upper()

        if user_input == 'EXIT' or user_input == 'SALIR':
            break

        if user_input == 'NEXT' or user_input == 'N':
            continue

        if user_input == '':
            print()
            print(f'{yellow}Prepare your answer{reset}'.center(100, '.'))
            playsound('level-up.mp3')

            # Start the countdown timers sequentially
            countdown_timer(15)  # Preparation time

            print()
            print(f'{yellow}Answer the question{reset}'.center(100, '.'))
            countdown_timer(45, intro_time=10)  # Answer time

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
