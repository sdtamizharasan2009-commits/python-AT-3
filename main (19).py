trains = {
    "12631": {
        "name": "Nellai Express",
        "stations": [
            ("Chennai", "20:10", "20:20"),
            ("Tambaram", "20:40", "20:45"),
            ("Villupuram", "22:10", "22:15")
        ],
        "days": {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
    },

    "12632": {
        "name": "Chennai Express",
        "stations": [
            ("Chennai", "21:00", "21:10"),
            ("Tambaram", "21:30", "21:35"),
            ("Madurai", "05:30", "05:40")
        ],
        "days": {"Monday", "Wednesday", "Friday"}
    },

    "12633": {
        "name": "Pandian Express",
        "stations": [
            ("Chennai", "22:00", "22:15"),
            ("Tambaram", "22:35", "22:40"),
            ("Madurai", "06:00", "06:10")
        ],
        "days": {"Tuesday", "Thursday", "Saturday"}
    },

    "12634": {
        "name": "Vaigai Express",
        "stations": [
            ("Chennai", "07:00", "07:10"),
            ("Tambaram", "07:30", "07:35"),
            ("Trichy", "11:00", "11:10")
        ],
        "days": {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
    },

    "12635": {
        "name": "Rockfort Express",
        "stations": [
            ("Chennai", "22:30", "22:40"),
            ("Tambaram", "23:00", "23:05"),
            ("Trichy", "05:00", "05:10")
        ],
        "days": {"Sunday", "Monday", "Wednesday", "Friday"}
    }
}

print("Complete Railway Timetable")

for train_number, details in trains.items():
    print("\nTrain Number:", train_number)
    print("Train Name:", details["name"])
    print("Running Days:", sorted(details["days"]))

    for station, arrival, departure in details["stations"]:
        print(station, arrival, departure)

station_name = input("\nEnter Station Name: ").strip().title()
day_name = input("Enter Day: ").strip().capitalize()

available_trains = []

for train_number, details in trains.items():
    if day_name in details["days"]:
        for station, arrival, departure in details["stations"]:
            if station == station_name:
                available_trains.append(
                    (train_number, details["name"], arrival, departure)
                )

available_trains = sorted(
    available_trains,
    key=lambda train: train[3]
)

print("\nAvailable Trains")

if available_trains:
    for train_number, name, arrival, departure in available_trains:
        print("Train Number:", train_number)
        print("Train Name:", name)
        print("Arrival:", arrival)
        print("Departure:", departure)
else:
    print("No Trains Available")