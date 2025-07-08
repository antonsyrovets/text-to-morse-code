"""
Module containing International Morse Code dictionaries: one for text encoding
and one for Morse code decoding.

Variables:
    morse_dict (dict[str, str]): encoding dictionary
    rev_morse_dic (dict[str, str]): decoding dictionary
"""

MORSE_DICT: dict[str, str] = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",

    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",

    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    '"': ".-..-.",
    "=": "-...-",
    "+": ".-.-.",
    "@": ".--.-.",

    " ": "/",
}

REV_MORSE_DIC: dict[str, str] = {v: k for k, v in MORSE_DICT.items()}
