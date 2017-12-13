from collections import Counter

word_count = Counter()

with open("she.txt", "r+") as file:
    word_count.update((word for word in file.read().split()))

for word, count in word_count.most_common():
    print word, count
