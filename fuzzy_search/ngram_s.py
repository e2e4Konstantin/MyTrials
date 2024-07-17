from difflib import SequenceMatcher
from nltk.util import ngrams
import codecs

# needle = "this is the string we want to find"
# hay    = "text text lots of text and more and more this string is the one we wanted to find and here is some more and even more still"




# needle_length  = len(needle.split())
# max_sim_val    = 0
# max_sim_string = u""
# print(int(.2*needle_length))

# for ngram in ngrams(hay.split(), needle_length + int(.2*needle_length)):
    
#     hay_ngram = u" ".join(ngram)
#     print(ngram, hay_ngram)
#     similarity = SM(None, hay_ngram, needle).ratio() 
#     if similarity > max_sim_val:
#         max_sim_val = similarity
#         max_sim_string = hay_ngram

# print (max_sim_val, max_sim_string)


def find_closest_phrase_match(target_phrase: str, text: str) -> tuple[float, str]:
    """Найдите ближайшее совпадение фразы в тексте."""
    needle_length = len(target_phrase.split())
    max_similarity = 0
    closest_match = ""
    
    for ngram in ngrams(text.split(), needle_length + int(.2*needle_length)):
        ngram_phrase = " ".join(ngram)
        similarity = SequenceMatcher(None, ngram_phrase, target_phrase).ratio()
        if similarity > max_similarity:
            max_similarity = similarity
            closest_match = ngram_phrase

    return max_similarity, closest_match

needle = "Основные технико-экономические показатели"
hay    = "Основные технико-экономические показатели объекта"

r = find_closest_phrase_match(needle, hay)
print(r)


needle = "this is the string we want to find"
hay    = "text text lots of text and more and more this string is the one we wanted to find and here is some more and even more still"

r = find_closest_phrase_match(needle, hay)
print(r)

