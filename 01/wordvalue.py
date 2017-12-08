from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
        words = [w.strip() for w in f.read().splitlines()]
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word = word.upper()
    score = 0
    for letter in word:
        try:
            score += LETTER_SCORES[letter]
        except KeyError:
            continue
    return score

def max_word_value(wordList=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    scores = {word: calc_word_value(word) for word in wordList}
    max_val = max(scores.values())
    for word, score in scores.items():
        if score == max_val:
            return word


if __name__ == "__main__":
    pass # run unittests to validate

