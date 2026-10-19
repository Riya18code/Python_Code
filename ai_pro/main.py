from app.analyzer import count
from app.cleaner import normalize

text ="I LOVE    MYSELF SO MUCH  "
normalized_text = normalize(text)
word_count = count(normalized_text)
print("original:",text)
print("normalized:",normalized_text)
print("word count:",word_count)
