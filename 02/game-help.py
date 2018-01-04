#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7

class ValidWords():
    """Class to handle finding possible words in DICTIONARY & scores."""
    def __init__(self, letters):
        self.draw = letters
        self.valid = []

# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
    def _get_permutations_draw(self):
        """Helper for get_possible_dict_words to get all permutations of draw letters.
        Hint: use itertools.permutations"""
        draw = self.draw
        permutations = []
        for i in range(2, len(draw)+1):
            tmp_list = list(itertools.permutations(draw, i))
            words = list(map(lambda y: ''.join([i for i in y]), tmp_list))
            permutations += words
        return permutations

    def get_possible_dict_words(self):
        """Get all possible words from draw which are valid dictionary words.
        Use the _get_permutations_draw helper and DICTIONARY constant"""
        draw = self.draw
        permutations = self._get_permutations_draw()
        for word in permutations:
            if word.lower() in DICTIONARY:
                self.valid.append(word)


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    tiles = []
    for _ in range(NUM_LETTERS):
        tiles.append(POUCH[random.randint(0, len(POUCH))])
    return tiles



def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    while True:
        player_word = input("Type a word using your letters: ")
        if _validation(player_word, draw):
            break
        else:
            print("Not a valid word. Try again.")
            continue
    return player_word



def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    for letter in word.upper():
        if letter not in draw:
            return False
    if word.lower() not in DICTIONARY:
        return False
    return True


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)



# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    # Use the ValidWords class to create list of potential words
    valid_words = ValidWords(draw)
    valid_words.get_possible_dict_words()

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = valid_words.valid

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
