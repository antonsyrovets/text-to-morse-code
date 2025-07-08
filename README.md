# Text to Morse Code Translator

A simple command-line tool written in Python for encoding text into Morse code and decoding Morse code back into original text. This project was built for practice of publishing a project online.

## Features

- Encodes / decodes latin characters (a - z), numbers (0 - 9) and basic punctuation to / from Internation Morse Code

- Automatic detection wheather text or Morse code was entered for translation

- Handles Morse code character separation with `' '` and word separation with `' / '`

- Pure Python3 without external dependencies

## Setup & Installation

To run this project, you'll need Python 3 to be installed on your system ([download python](https://www.python.org/downloads/)).

1. Open Terminal (MacOS/Linux) or Command Promt (Windows), clone the repository and navigate to its directory.

```bash
git clone https://github.com/antonsyrovets/text-to-morse-code.git
cd text-to-morse-code
```

2. (Optional but recommended) Create and activate a Python virtual environment:

```bash
# For MacOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

## Usage

Run the `main.py` script from your terminal:

```bash
python3 main.py
```

You will be greated by the program's interface and prompted to enter either the text or the Morse code for translation. The script will automatically detect whether you want to decode or encode.

Example:

```bash
Welcome to CLI Morse Code Translator!
.-- . .-.. -.-. --- -- .

Type text or Morse code using '.', '-', spaces between letters and ' / ' between words. Then hit 'Enter' for translation:

How do you do?

The morse code translation is ('#' indicates untranslatable character):

.... --- .-- / -.. --- / -.-- --- ..- / -.. --- ..--..

Continue translating? [y / n] y

Type text or Morse code using '.', '-', spaces between letters and ' / ' between words. Then hit 'Enter' for translation:

.... --- .-- / -.. --- / -.-- --- ..- / -.. --- ..--..

The original text is ('#' indicates untranslatable character):

HOW DO YOU DO?

Continue translating? [y / n] n
Quiting the program...
```

## License

This pjocet is licensed under the MIT License. See `LICENSE` file for details.
