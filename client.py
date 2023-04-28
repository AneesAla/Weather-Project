import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9123))
msg = s.recv(1024) # receive a message of 1024 char buffer
print(msg.decode("utf-8"))
state = ""

# prompt the user to input where and when they want the weather for
country = input("Enter the name of a country (Please spell out the Full name of the country): ")
if country == "United States" or country ==  "united states":
    state = input("Please input the state: ")
city = input("Please enter the city you would like to get the weather for: ")
startDate = input("Please input the start date (mm/dd/yyyy): ")
endDate = input("Please enter the end date (mm/dd/yyyy): ")

# Combine the country, state (if applicable), and city into a single string
location = f"{country},{state},{city}" if state else f"{country},{city}"

# Combine the start and end dates into a single string
date_range = f"{startDate},{endDate}"

# Send the location and date range to the server
message = f"{location};{date_range}".encode("utf-8")
s.send(message)