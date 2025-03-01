# QuizMyWords

A Python-based word quiz application that helps you test and strengthen your vocabulary using custom word lists. QuizMyWords supports various quiz types, provides optional hints during quizzes, and takes CSV files as input, making it easy to personalize your learning experience. At the end of each quiz, you receive a final grade based on your performance.


## Features

* Multiple Quiz Types:
  * Flashcards
  * Typing Quiz (one word per time)
  * Repeated Typing Quiz (until the correct answer)
  * Multiple Choice Quiz (repeated until correct)
* Custom Word Lists: Provide your own words in CSV format.
* Immediate Feedback: See results right after answering.
* Final Score: Get a clear overview of your performance at the end.


## How the quiz works:

1. Place your word list CSV files in the src/data folder.
2. Start the program and choose a word list.
3. Choose which language you want to practice (e.g. from English to Spanish or from Spanish to English)
3. Select a quiz type
4. Answer the questions and get instant feedback.
5. Receive hints when needed.
6. See your final score when the quiz ends.
6. Choose the next quiz if you want to.


## CSV Format Example

```
English,Dutch
hello,hallo
book,boek
cat,kat
```

## Setup & Installation

1. Clone this repository:

```
git clone https://github.com/yourusername/QuizMyWords.git
cd QuizMyWords
```

2. Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate    # For Windows
```

3. Install dependencies:

```
pip install -r requirements.txt
```


## Usage

Run the program from the command line:

```
python src/main.py
```
Follow the on-screen instructions to select a word list and quiz type.


## Folder Structure

```
QuizMyWords/
|-- src/
|   |-- data/              # Word list CSV files
|   |-- quizzes/           # Code for all quizzes
|   |-- utils/             # Helper functions
|   |-- main.py            # Program entry point
|-- README.md
|-- requirements.txt
```


## Future Plans

Note: Not everything described in this README has been added yet.
Addtitional to finishing everything describes in this README I'll add:

1. Add a graphical user interface (GUI)
2. Implement high scores and session logs
3. Support more file formats like XLSX
4. Difficult-words list (all words that you've made mistakes on in the last 30 days)
