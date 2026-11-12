import random
import time

readings = [random.randint(0, 50) for day in range(365)]

print("Weekly Totals:")
weekly_totals = []

for week in range(0, len(readings), 7):
    total = sum(readings[week:week + 7])
    weekly_totals.append(total)
    print("Week", len(weekly_totals), ":", total)

print("Wettest Week:", weekly_totals.index(max(weekly_totals)) + 1)
print("Driest Week:", weekly_totals.index(min(weekly_totals)) + 1)

print("Maximum Rainfall:", max(readings))
print("Maximum Position:", readings.index(max(readings)) + 1)

print("Minimum Rainfall:", min(readings))
print("Minimum Position:", readings.index(min(readings)) + 1)

def naive_average(data):
    averages = []

    for position in range(len(data) - 6):
        averages.append(sum(data[position:position + 7]) / 7)

    return averages

def running_average(data):
    averages = []

    if len(data) < 7:
        return averages

    total = sum(data[:7])
    averages.append(total / 7)

    for position in range(7, len(data)):
        total += data[position] - data[position - 7]
        averages.append(total / 7)

    return averages

print("7-Day Moving Average:", running_average(readings))
print("Dry Days:", [day + 1 for day, rain in enumerate(readings) if rain == 0])

print("Readings[7:14]:", readings[7:14])
print("Readings[-7:]:", readings[-7:])
print("Readings[::7]:", readings[::7])

for size in [365, 36500, 365000]:
    data = [random.randint(0, 50) for day in range(size)]

    start = time.perf_counter()
    naive_average(data)
    naive_time = time.perf_counter() - start

    start = time.perf_counter()
    running_average(data)
    running_time = time.perf_counter() - start

    print("Readings:", size)
    print("Naive Time:", naive_time)
    print("Running Sum Time:", running_time)

print("Empty List:", running_average([]))
print("Short List:", running_average([2, 4, 6, 8]))