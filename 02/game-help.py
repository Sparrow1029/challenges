#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random
import shelve
import sys

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7

class ValidWords():
    """Class to handle finding possible words in DICTIONARY & scores."""
    def __init__(self, letters):
        self.draw = letters
        self.valid = self.get_possible_dict_words()

    def _get_permutations_draw(self):
        """Helper for get_possible_dict_words to get all permutations of draw letters.
        Hint: use itertools.permutations"""
        for i in range(1, 8):
            yield from list(itertools.permutations(self.draw, i))  # >= 3.3
        # draw = self.draw
        # permutations = []
        # for i in range(2, len(draw)+1):
        #     tmp_list = list(itertools.permutations(draw, i))
        #     words = list(map(lambda y: ''.join([i for i in y]), tmp_list))
        #     permutations += words
        # return permutations

    def get_possible_dict_words(self):
        """Get all possible words from draw which are valid dictionary words.
        Use the _get_permutations_draw helper and DICTIONARY constant"""
        permutations = [''.join(word).lower() for word in self._get_permutations_draw()]
        return set(permutations) & set(DICTIONARY)
        # draw = self.draw
        # permutations = self._get_permutations_draw()
        # for word in permutations:
        #     if word.lower() in DICTIONARY:
        #         self.valid.append(word)


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return random.sample(POUCH, NUM_LETTERS)

def input_word(draw):
    while True:
        word = input('Form a valid word: ').upper()
        try:
            return _validation(word, draw)
        except ValueError as e:
            print(e)
            continue

def _validation(word, draw):
    # thanks Durmus
    for char in word.upper():
        if char in draw:
            draw.remove(char)
        else:
            raise ValueError("{} is not a valid word!".format(word))
    if not word.lower() in DICTIONARY:
        raise ValueError('Not a valid dictionary word, try again')
    return word


#def input_word(draw):
#    """Ask player for a word and validate against draw.
#    Use _validation(word, draw) helper."""
#    while True:
#        player_word = input("Form a valid word: ")
#        if _validation(player_word, draw):
#            break
#        else:
#            print("Not a valid word. Try again.")
#            continue
#    return player_word
#
#
#
#def _validation(word, draw):
#    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
#    for letter in word.upper():
#        if letter not in draw:
#            return False
#    if word.lower() not in DICTIONARY:
#        return False
#    return True


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
    score_file = shelve.open('highscore.db', 'c')
    if not score_file['high_score']:
        score_file['high_score'] = 0
    print("\nCurrent HIGH SCORE: {}\n".format(score_file['high_score']))
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    # Use the ValidWords class to create list of potential words
    valid_words = ValidWords(draw)
    # valid_words.get_possible_dict_words()

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = valid_words.valid

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word.upper(), max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))
    if game_score > int(score_file['high_score']):
        print("\nNEW HIGH SCORE!!\n")
        score_file['high_score'] = game_score
    else:
        pass
    reset = input('Reset high score? y/n: ')
    if 'y' in reset.lower():
        score_file['high_score'] = 0
        print("High score reset to 0.")
    else:
        pass
    score_file.close()

    again = input('\nTry again? ')
    if again.lower().startswith('y'):
        main()
    else:
        print("Thanks for playing. Goodbye.")
        sys.exit(0)

if __name__ == "__main__":
    main()
