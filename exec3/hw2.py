from collections import Counter

text = 'hello world hello python'
counter = Counter(text.split())
word_count_dict = dict(counter)

most_common_word, freq = counter.most_common(1)[0]
print(most_common_word)