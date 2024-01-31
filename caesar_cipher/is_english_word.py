
import re
from corpus_loader import word_list, name_list


def count_words(text):

    candidate_words = text.split()

    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            word_count += 1
    return word_count


# for phrase in candidates:
#     word_count = count_words(phrase)
#     percentage = int(word_count / len(phrase.split()) * 100)
#     if percentage > 50:
#         print(phrase, percentage)