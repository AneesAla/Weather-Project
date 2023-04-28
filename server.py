import socket
import requests
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9123))
s.listen(5)


while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    message = clientsocket.recv(1024)
    location = message.decode("utf-8")

    location_parts = location.split(",")
    city = location_parts[0]
    state = location_parts[1]

    lat = 0.0
    lon = 0.0

    nominatimAPI = (
        f"https://nominatim.openstreetmap.org/search/{city} {state}?format=json&limit=1"
    )
    nominatimAPIResponse = requests.get(nominatimAPI)

    if nominatimAPIResponse.status_code == 200:
        nominatimData = nominatimAPIResponse.json()
        lat = nominatimData[0]["lat"]
        lon = nominatimData[0]["lon"]

        openweathermapAPI = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=imperial&appid=8cf1d48bb4fb4a8548e95957e464b010"
        openweathermapAPIResponse = requests.get(openweathermapAPI)

        if openweathermapAPIResponse.status_code == 200:
            openweathermapData = openweathermapAPIResponse.json()
            clientsocket.send(
                bytes(
                    json.dumps(openweathermapData["list"][0]["main"]),
                    "utf-8",
                )
            )
