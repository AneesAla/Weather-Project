import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9123))
s.listen(5)


while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome Weather App By Anees Alawmleh!\nThis app allows you to find the weather for a city of your choice!", "utf-8")) # sending info the client

    # Receive the location and date range from the client
    message = clientsocket.recv(1024)
    location, date_range = message.decode("utf-8").split(";")

    # Split the location into separate parts
    location_parts = location.split(",")
    country = location_parts[0]
    state = location_parts[1] if len(location_parts) > 2 else ""
    city = location_parts[-1]

    # Split the date range into separate start and end dates
    start_date, end_date = date_range.split(",")


    print(country, state, city, start_date, end_date)