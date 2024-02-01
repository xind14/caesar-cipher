"""
This code block sets up NLTK (Natural Language Toolkit) and downloads the "words" and "names" corpora
from the NLTK library. These corpora are used to check whether a given word is a valid English word
or a common name.
"""

import ssl
import nltk

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()