import xml.etree.ElementTree as ET
from collections import Counter

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87

xmlTree = ET.parse(RSS_FEED)

def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    elemList = []
    for elem in xmlTree.iter():
        fixed = elem.tag.replace(" ", "-")
        elemList.append(fixed)
    return elemList

def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    c = Counter(tags)
    return c.most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""



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
