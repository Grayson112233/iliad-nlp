# Variables and functions used by multiple scripts
'''
TEXTS = [
    "george_chapman",
    "alexander_pope",
    "william_cowper",
    "edward_earl_of_derby",
    "theodore_buckley",
    "lang_leaf_myers",
    "samuel_butler",
    "robert_fagels",
]
'''

TEXTS = [
    "alice_in_wonderland",
    "frankenstien",
    "moby_dick",
    "pride_and_prejudice",
    "sherlock_holmes",
]


PUB_DATES = {
    "george_chapman": 1598,
    "alexander_pope": 1715,
    "william_cowper": 1849,
    "edward_earl_of_derby": 1867,
    "theodore_buckley": 1873,
    "lang_leaf_myers": 1891,
    "samuel_butler": 1898,
    "robert_fagels": 1998,
}


def readFile(filename):
    # Parsing function for plaintext texts.
    # Return a list of strings, each word in the text
    file = open(filename)
    words = []
    for line in file:
        line = line.rstrip()
        words += line.split(' ')

    # Make all words lowecase and remove punctuation
    for i in range(len(words)):
        words[i] = words[i].translate({ord(c): None for c in "\",.!'()[]0123456789?;-"}).lower()

    # Remove empty lines
    words = list(filter(("").__ne__, words))
    return words
