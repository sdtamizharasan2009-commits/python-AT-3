import random
import time
import sys

readings = [2, 5, 9, 12, 0, -55, 45, 51, 7, 3, 10, -5]

valid = []
fahrenheit = []

for temperature in readings:
    if -50 <= temperature <= 50:
        valid.append(temperature)
        fahrenheit.append(temperature * 9 / 5 + 32)

print("For Loop Celsius:", valid)
print("For Loop Fahrenheit:", fahrenheit)

valid_comprehension = [
    temperature for temperature in readings
    if -50 <= temperature <= 50
]

fahrenheit_comprehension = [
    temperature * 9 / 5 + 32
    for temperature in valid_comprehension
]

print("Comprehension Celsius:", valid_comprehension)
print("Comprehension Fahrenheit:", fahrenheit_comprehension)

valid_map = list(filter(
    lambda temperature: -50 <= temperature <= 50,
    readings
))

fahrenheit_map = list(map(
    lambda temperature: temperature * 9 / 5 + 32,
    valid_map
))

print("Map Filter Celsius:", valid_map)
print("Map Filter Fahrenheit:", fahrenheit_map)

alarms = [
    (minute, temperature)
    for minute, temperature in enumerate(readings)
    if -50 <= temperature <= 50 and not 2 <= temperature <= 8
]

print("Alarm Minutes:", alarms)

temperature_dict = {
    minute: temperature
    for minute, temperature in enumerate(readings)
    if -50 <= temperature <= 50
}

temperature_set = {
    temperature for temperature in readings
    if -50 <= temperature <= 50
}

print("Dictionary:", temperature_dict)
print("Set:", temperature_set)

for size in [10000, 100000, 1000000]:
    data = [random.randint(-60, 60) for position in range(size)]

    start = time.perf_counter()
    loop_result = []

    for temperature in data:
        if -50 <= temperature <= 50:
            loop_result.append(temperature)

    loop_time = time.perf_counter() - start

    start = time.perf_counter()
    comprehension_result = [
        temperature for temperature in data
        if -50 <= temperature <= 50
    ]

    comprehension_time = time.perf_counter() - start

    start = time.perf_counter()
    map_result = list(filter(
        lambda temperature: -50 <= temperature <= 50,
        data
    ))

    map_time = time.perf_counter() - start

    print("Readings:", size)
    print("Loop Time:", loop_time)
    print("Comprehension Time:", comprehension_time)
    print("Map Filter Time:", map_time)
    print("Same Results:", loop_result == comprehension_result == map_result)

generator = (temperature for temperature in readings if -50 <= temperature <= 50)

print("List Memory:", sys.getsizeof(valid_comprehension))
print("Generator Memory:", sys.getsizeof(generator))

print("All Valid:", [temperature for temperature in [2, 3, 4] if -50 <= temperature <= 50])
print("All Invalid:", [temperature for temperature in [55, 60, -55] if -50 <= temperature <= 50])