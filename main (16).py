import random
import string
import time
from collections import Counter

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

STOP = {"not", "high"}

def frequencies(texts, stop):
    counts = {}

    for text in texts:
        words = text.lower().translate(
            str.maketrans("", "", string.punctuation)
        ).split()

        for word in words:
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1

    return counts

def top(counts, k):
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]

print("Word Frequencies:", frequencies(calls, STOP))
print("Top Words:", top(frequencies(calls, STOP), 3))

complaints = [
    {"district": "Chennai", "crop": "Rice", "text": "Seeds not received"},
    {"district": "Madurai", "crop": "Wheat", "text": "Fertiliser price high"},
    {"district": "Chennai", "crop": "Rice", "text": "Seeds delayed"},
    {"district": "Salem", "crop": "Cotton", "text": "Water problem"},
    {"district": "Madurai", "crop": "Wheat", "text": "Seeds not received"}
]

districts = {}
crops = {}

for complaint in complaints:
    districts.setdefault(complaint["district"], []).append(complaint["text"])
    crops.setdefault(complaint["crop"], []).append(complaint["text"])

print("District Complaints:", districts)
print("Crop Complaints:", crops)

print("Keys:", list(districts.keys()))
print("Values:", list(districts.values()))
print("Items:", list(districts.items()))

for size in [1000, 10000, 100000]:
    data = [
        random.choice(["seeds", "rice", "water", "fertiliser", "crop", "price"])
        for position in range(size)
    ]

    start = time.perf_counter()
    counts = {}

    for word in data:
        counts[word] = counts.get(word, 0) + 1

    dictionary_time = time.perf_counter() - start

    start = time.perf_counter()
    list_counts = {word: data.count(word) for word in set(data)}
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    counter_counts = Counter(data)
    counter_time = time.perf_counter() - start

    print("Complaints:", size)
    print("Dictionary Time:", dictionary_time)
    print("List Count Time:", list_time)
    print("Counter Time:", counter_time)

print("Empty Text:", frequencies([""], STOP))
print("Case Test:", frequencies(["SEEDS seeds Seeds"], STOP))
print("Punctuation Test:", frequencies(["seeds, rice! seeds."], STOP))