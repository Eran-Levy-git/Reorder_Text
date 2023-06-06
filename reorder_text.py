import string
import sys


def reorder_text(text):
    """reorders a given English text alphabetically according to the English version of the Hebrew alphabet. It
    removes all punctuation marks from the text before sorting it and returns the reordered text as a string"""
    text_without_punctuation = text.translate(str.maketrans('', '', string.punctuation))
    if not text_without_punctuation.isascii():
        return "You didn't enter a valid English text, Please try again."
    hebrew_alphabet = ['a', 'b', 'g', 'd', 'h', 'v', 'z', 'j', 't', 'y', 'k', 'l', 'm', 'n', 's', 'i', 'p', 'x', 'q',
                       'r', 'w', 'u', 'c', 'e', 'f', 'o']
    words = text_without_punctuation.split()
    sorted_words = sorted(words, key=lambda word: [hebrew_alphabet.index(letter.lower()) for letter in word])
    return ' '.join(sorted_words)


def main(sys_argv):
    """this function is for running the program from the command line"""
    text_input = sys_argv[1]
    num_of_args = len(sys_argv)
    return text_input, num_of_args


if __name__ == '__main__':
    TEXT_INPUT, NUM_OF_ARGS = main(sys.argv)
    RIGHT_NUM_OF_AGRS = 2
    ERROR_MSG = "Wrong number of parameters. The correct usage is: reorder_text.py <text_input> "
    if NUM_OF_ARGS != RIGHT_NUM_OF_AGRS:
        print(ERROR_MSG)
    else:
        print(reorder_text(TEXT_INPUT))
