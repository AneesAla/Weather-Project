import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9123))
msg = s.recv(1024)
print(msg.decode("utf-8"))

state = input("Please input the state: ")
city = input("Please enter the city: ")

location = f"{city},{state}"

message = f"{location}".encode("utf-8")
s.send(message)

msg = s.recv(1024)
data = json.loads(msg.decode("utf-8"))

print("Temp: " + str(data["temp"]))
print("Feels Like: " + str(data["feels_like"]))
print("Sea Level: " + str(data["sea_level"]))
print("Humidity: " + str(data["humidity"]))
