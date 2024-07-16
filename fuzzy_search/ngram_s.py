from difflib import SequenceMatcher as SM
from nltk.util import ngrams
import codecs

needle = "this is the string we want to find"
hay    = "text text lots of text and more and more this string is the one we wanted to find and here is some more and even more still"

needle_length  = len(needle.split())
max_sim_val    = 0
max_sim_string = u""
print(int(.2*needle_length))

for ngram in ngrams(hay.split(), needle_length + int(.2*needle_length)):
    
    hay_ngram = u" ".join(ngram)
    print(ngram, hay_ngram)
    similarity = SM(None, hay_ngram, needle).ratio() 
    if similarity > max_sim_val:
        max_sim_val = similarity
        max_sim_string = hay_ngram

print (max_sim_val, max_sim_string)