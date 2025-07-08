#!usr/bin/env python3

"""Text To Morse Code Translator

This script provides the CLI interface for encoding the text into Morse code
and for decoding the Morse code back to the original text.

This file can also be imported as a module and contains the following functions:

    * encode - encodes the text string into Morse code
    * decode - decodes the Morse code string into original text
    * main - the main function of the script
"""

from data import morse_dict, rev_morse_dic


def encode(text: str) -> str:
    """
    Converts a passed-in text string into Morse code using following convention:
    
    '.' = dot
    '-' = dash
    ' ' = space between two letters
    ' / ' = space between two words

    If a character can not be translated, it is encoded as '#'.

    Parameters:
        text (str): text to encode

    Returns:
        str: a string of the Morse-encoded text
    """

    morse: list[str] = [morse_dict.get(letter.lower(), "#") for letter in text]
    return " ".join(morse)

def decode(morse: str) -> str:
    """
    Translates a Morse code string back to original text. Morse code string
    must consist of:

    '.' = dot
    '-' = dash
    ' ' = space between two letters
    ' / ' = space between two words

    Unknown sequence of dots and dashes is decoded as '#'.

    Parameters:
        morse (str): text to decode

    Returns:
        str: decoded original text
    """

    morse_letters: list[str] = morse.split(" ")
    og: list[str] = [rev_morse_dic.get(ml, "#").upper() for ml in morse_letters]
    return "".join(og)

def main() -> None:
    """
    The main function of the script, providing the CLI interface for the
    text-to-Morse-code translation.
    """

    print("\nWelcome to CLI Morse Code Translator!")
    print(".-- . .-.. -.-. --- -- .")
    cont: bool = True
    while cont:
        inp_txt: str = input(("\nType text or Morse code using '.', '-', "
                              "spaces between letters and ' / ' between words. "
                              "Then hit 'Enter' for translation:\n\n"))
        
        if set(inp_txt).issubset(set(".- /#")):
            result: str = decode(inp_txt)
            print(("\nThe original text is ('#' indicates untranslatable "
                   "character):\n"))
        else:
            result: str = encode(inp_txt)
            print(("\nThe morse code translation is "
                   "('#' indicates untranslatable character):\n"))

        print(result)
        corr_inp: bool = False
        while not corr_inp:
            yes_no: str = input("\nContinue translating? [y / n] ").lower()
            if yes_no != "y" and yes_no != "n":
                print("\nPlease answer with 'y' or 'n' and hit 'Enter'.")
            else:
                corr_inp = True
        
        if yes_no == "n":
            print("Quiting the program...\n")
            cont = False

if __name__ == "__main__":
    main()
