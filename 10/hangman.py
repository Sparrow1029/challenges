from string import ascii_lowercase
import sys, os

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
# PLACEHOLDER = '_'


class Hangman(object):
    """Main game class"""

    def __init__(self, word):
        """Storing correct guess values as dict of 0 - 1 switches.
        self.hidden displays current part of word player has guessed."""
        self.word = word
        self.guessed = []
        self.wrong = 0
        self.right = {x.lower(): 0 for x in set(filter(lambda x: x.lower() in
                                                    ascii_lowercase, word))}
        self.hidden = [c if c.lower() not in ascii_lowercase else '_' for c in word]

    def guess(self):
        """Handles player input and returns their guess."""
        while True:
            letter = input('Guess: ')
            try:
                int(letter)
                print("Letters only please.")
                continue
            except ValueError:
                pass
            if len(letter) > 1:
                print('One at a time, hoss.')
                continue
            elif not len(letter):
                print('Please enter a guess.')
                continue
            elif letter.lower() not in ascii_lowercase:
                print("Letters only please.")
                continue
            elif letter.lower() in self.guessed:
                print("Already guessed that one.")
                continue
            break
        self.guessed.append(letter.lower())
        return letter.lower()

    def display(self):
        """Function to handle displaying current game state."""
        print(HANG_GRAPHICS[self.wrong])
        print('\nPrevious guesses: {}\n'.format(
            ' '.join([s.upper() for s in self.guessed])))
        print(''.join(self.hidden), end="\n\n")

    def update_hidden(self, letter):
        """Helper function to update what part of word is displayed."""
        word = self.word
        letter = letter.lower()
        for i in range(len(word)):
            if word[i].lower() == letter:
                self.hidden[i] = word[i]

    def chk(self, letter):
        """Check correctness of guess."""
        c = letter.lower()
        if c in self.right.keys():
            self.right[c] = 1
            self.update_hidden(letter)
        else:
            self.wrong += 1

    def win(self):
        """Test for win state."""
        if all(x == 1 for x in self.right.values()):
            return True
        return False

    def lose(self):
        """Test for losing state."""
        if self.wrong >= ALLOWED_GUESSES-1:
            return True
        return False


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()

    game = Hangman(word)  # Instantiate game class

    # init main game loop
    while True:
        os.system('clear')
        # print(word)
        # print(game.right)
        game.display()
        letter = game.guess()
        game.chk(letter)
        if game.win():
            os.system('clear')
            game.display()
            sys.exit("YOU WIN! Your neck is saved.")
        elif game.lose():
            os.system('clear')
            game.display()
            sys.exit("ACK! You Died. Better luck next life, pardner.")
        else:
            continue
