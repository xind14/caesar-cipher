import re
from caesar_cipher.corpus_loader import word_list, name_list
# from corpus_loader import word_list, name_list


def count_words(text):
    """
    Counts the number of valid English words in a given text.

    The function uses a list of English words and names loaded from the corpus_loader module.
    It removes non-alphabetic characters from each candidate word and checks if the resulting word
    or its lowercase version is present in the word_list or name_list.

    Args:
        text (str): The text in which words are counted.

    Returns:
        int: The count of valid English words.
    """
    candidate_words = text.split()

    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            word_count += 1
    return word_count
