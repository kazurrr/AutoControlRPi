import json

car_info = {
    "id": 23234,
    "brand": "Mercedes",
    "model": "C class (W203)",
    "lat": 12313,
    "lon": 32465
}

sensors = {
    "speed": 69,
    "rpm": "Mercedes",
    "model": 1247
}

errors = {}

data = {
    "carInfo": car_info,
    "sensors": sensors,
    "errors": errors
}

print json.dumps(data)
