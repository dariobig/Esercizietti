import spacy
import re 

EMPTY = ''
word_chars = re.compile('[^a-zA-Z]+')
def fix_word(word: str, min_len: int = 5) -> str:
    if word[0].isupper():
        return EMPTY
    if len(word) < min_len:
        return EMPTY
    return word_chars.sub(EMPTY, word)

nlp = spacy.load('it_core_news_sm')
print(nlp.vocab)

words = [word for word in (fix_word(word) for word in nlp.vocab.strings if len(word) == 5) if len(word) == 5]

for word in words:
    replaced = word_chars.sub('', word)
    print(replaced)
print(words[:10])