import copy
import sys
import time

rows, cols = 3, 4

bad = [[0] * cols] * rows
bad[0][1] = 7

good = [[0 for column in range(cols)] for row in range(rows)]
good[0][1] = 7

print("bad :", bad)
print("good:", good)

print(bad[0] is bad[1], good[0] is good[1])

stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar",
    (13.0674, 80.2376): "Guindy"
}

print(stops[(13.0418, 80.2341)])

try:
    stops[[13.0418, 80.2341]] = "Chennai"
except TypeError:
    print("Lists cannot be dictionary keys")

print("\nTuple Unpacking:")

for coordinates, name in stops.items():
    latitude, longitude = coordinates
    print(name, latitude, longitude)

original = [[10, 20], [30, 40]]

alias = original
shallow = copy.copy(original)
slicing = original[:]
deep = copy.deepcopy(original)

original[0][0] = 100

print("Original:", original)
print("Alias:", alias)
print("Shallow Copy:", shallow)
print("Slicing Copy:", slicing)
print("Deep Copy:", deep)

print("Identity:", original is alias)
print("Identity:", original is shallow)

numbers = list(range(1000000))
tuple_numbers = tuple(numbers)

print("List Memory:", sys.getsizeof(numbers))
print("Tuple Memory:", sys.getsizeof(tuple_numbers))

start = time.perf_counter()
test_list = list(range(1000000))
print("List Creation Time:", time.perf_counter() - start)

start = time.perf_counter()
test_tuple = tuple(range(1000000))
print("Tuple Creation Time:", time.perf_counter() - start)

start = time.perf_counter()
print("List Index:", test_list[500000])
print("List Indexing Time:", time.perf_counter() - start)

start = time.perf_counter()
print("Tuple Index:", test_tuple[500000])
print("Tuple Indexing Time:", time.perf_counter() - start)

mixed = ([10, 20], 30)
mixed[0][0] = 100

print("List Inside Tuple:", mixed)