# TOEFL Speaking Practice Timer

This script provides a simple tool for practicing the first type of questions of the TOEFL speaking section, the **Independent Task**. It randomly selects questions from a file, prompts the user to answer, and uses a countdown timer to manage preparation and answering time. The script also supports key commands for skipping questions and exiting the program.


## Question One – Independent Speaking
TOEFL Speaking question 1 is the independent TOEFL speaking question.  It’s also called the “personal choice” question.  You’ll give your opinion on a subject likely related to school, work or some other part of life.

This question asks if you agree or disagree with a given statement.  That might look like this:

* “State whether you agree or disagree with the following statement. Then explain your reasons using specific details in your argument. Teachers should assign daily homework to students.”

Sometimes, the question requires you to pick between two opposing options.  In that case, it will look something like this:

* “There are many different approaches to academic studies, and all of them have specific benefits. Do you prefer to study for tests in a group, or to study alone? Include details and examples to support your explanation.”

Lastly, you might get a question that refers to a hypothetical situation.  These questions are rare.  They look like this:

* “Some companies have rules that forbid employees from using personal cell phones during working hours. Do you think this is a good idea? Why or why not? Use specific reasons and examples to support your answer.”


## Features

-   Randomly selects TOEFL speaking questions from a file.
-   Displays a countdown timer for preparation and answering.
-   Plays a sound to indicate when time is up.
-   Supports user commands for skipping questions and exiting the program.

## Requirements

-   Python 3.x
-   `pandas` library
-   `playsound` library
-   `pynput` library

You can install the required libraries using pip:

Copy code

`pip install pandas playsound pynput` 

## Files

-   `toefl_speaking_q1.txt`: Text file containing TOEFL speaking questions, one per line.
-   `level-up.mp3`: Sound file played when the timer ends.

## Usage

1.  **Prepare your files**:
    
    -   Ensure `toefl_speaking_q1.txt` contains your TOEFL speaking questions, one per line.
    -   Place the `level-up.mp3` sound file in the same directory as the script.
2.  **Run the script**:
    
    Copy code
    
    `python toelf_practice.py` 
    
3.  **Interact with the script**:
    
    -   **Press `Enter`** to start the preparation timer (15 seconds) and then the answering timer (45 seconds).
    -   **Type `NEXT`** to skip to the next question.
    -   **Type `EXIT` or `SALIR`** to exit the script.
    -   **Press `Escape`** to exit the script immediately.

## Code Explanation

### Key Functions

-   **`on_press(key)`**: Detects key presses. Exits the program when the `Escape` key is pressed.
    
-   **`countdown_timer(seconds, sound_file)`**: Displays a countdown timer for the specified number of seconds. Plays a sound when the time is up.
    
-   **`ask_question(df)`**: Handles the question asking process. Manages user inputs, displays questions, and triggers timers.
    
-   **`main()`**: Initializes the keyboard listener, reads questions from the file, and starts the question-asking process.
    

## Troubleshooting

-   **FileNotFoundError**: Ensure that `toefl_speaking_q1.txt` is present in the same directory as the script.
-   **ModuleNotFoundError**: Install the required libraries using pip.
-   **Sound issues**: Ensure `level-up.mp3` is present in the same directory and is accessible.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
