import xml.etree.ElementTree as ET
from collections import Counter
from difflib import SequenceMatcher
import re
from itertools import product

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
IDENTICAL = 1.0
REPLACE_CHARS = str.maketrans('-', ' ')

root = ET.parse(RSS_FEED).getroot()

def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    tags = [e.text for e in root.iter('category')]
    return [tag.translate(REPLACE_CHARS) for tag in tags]

def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    tags = set(tags)
    for pair in product(tags, tags):
        if pair [0][0] != pair[1][0]:
            continue
        pair = tuple(sorted(pair))
        similarity = SequenceMatcher(None, *pair).ratio()
        if SIMILAR < similarity < IDENTICAL:
            yield pair


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
