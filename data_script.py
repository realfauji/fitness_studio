from datetime import datetime, timedelta
import json


data = [
    {
        "id": 1,
        "name": "Yoga",
        "instructor": "Raj",
        "datetime": str(datetime.now() + timedelta(days=1)),
        "slots": 5
    },
    {
        "id": 2,
        "name": "Zumba",
        "instructor": "Akash",
        "datetime": str(datetime.now() + timedelta(days=2)),
        "slots": 10
    },
    {
        "id": 3,
        "name": "Strength Training",
        "instructor": "Vishal",
        "datetime": str(datetime.now() + timedelta(days=3)),
        "slots": 10
    },
    {
        "id": 4,
        "name": "HIIT",
        "instructor": "Bharat",
        "datetime": str(datetime.now() + timedelta(days=2)),
        "slots": 15
    },
    {
        "id": 5,
        "name": "Cardio",
        "instructor": "Satendra",
        "datetime": str(datetime.now() + timedelta(days=1)),
        "slots": 20
    }
]

with open("data/classes.json", "w") as f:
    json.dump(data, f, indent=4)
