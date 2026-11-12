import time

ai_elective = {
    "192311001", "192311004", "192311007", "192311009"
}

iot_elective = {
    "192311002", "192311004", "192311009", "192311010"
}

all_students = {
    f"1923110{i:02d}" for i in range(1, 11)
}

both = ai_elective & iot_elective

exactly_one = ai_elective ^ iot_elective

neither = all_students - (ai_elective | iot_elective)

print("clash :", sorted(both))
print("exactly one:", sorted(exactly_one))
print("neither :", sorted(neither))

print("Union:", ai_elective | iot_elective)
print("Intersection:", ai_elective & iot_elective)
print("Difference:", ai_elective - iot_elective)
print("Symmetric Difference:", ai_elective ^ iot_elective)

both_method = ai_elective.intersection(iot_elective)
exactly_one_method = ai_elective.symmetric_difference(iot_elective)
neither_method = all_students.difference(ai_elective.union(iot_elective))

print("Using Methods:")
print(sorted(both_method))
print(sorted(exactly_one_method))
print(sorted(neither_method))

for size in [10000, 100000, 1000000]:
    numbers = list(range(size))
    number_set = set(numbers)

    start = time.perf_counter()
    result = size - 1 in numbers
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    result = size - 1 in number_set
    set_time = time.perf_counter() - start

    print("Students:", size)
    print("List Search Time:", list_time)
    print("Set Search Time:", set_time)

list_one = [1, 2, 3, 4, 5]
list_two = [3, 4, 5, 6, 7]

start = time.perf_counter()
common_nested = []

for first in list_one:
    for second in list_two:
        if first == second:
            common_nested.append(first)

print("Nested Loop:", common_nested)
print("Nested Loop Time:", time.perf_counter() - start)

start = time.perf_counter()
common_set = set(list_one) & set(list_two)

print("Set Intersection:", sorted(common_set))
print("Set Time:", time.perf_counter() - start)

print("Empty Electives:", set() & set())
print("Identical Electives:", sorted(ai_elective & ai_elective))