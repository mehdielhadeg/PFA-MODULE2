import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("new.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://employees-fd-default-rtdb.firebaseio.com"
})

ref = db.reference('Employees')

data = {
    "321654":
        {
            "firstname": "Murtaza Hassan",
            "lastname": "Robotics",
            "entry_date": "2020-12-11 00:00:00",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "firstname": "emily",
            "lastname": "kroft",
            "entry_date": "2020-12-11 00:00:00",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "firstname": "elon",
            "lastname": "musk",
            "entry_date": "2020-12-11 00:00:00",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "123456":
        {
            "firstname": "mehdi",
            "lastname": "elhadeg",
            "entry_date": "2020-12-11 00:00:00",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)
