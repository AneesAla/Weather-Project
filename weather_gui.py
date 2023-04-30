import customtkinter
import socket
import json
import threading

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("400x240")
app.title("Weather App")


def listen_for_messages():
    while True:
        message = s.recv(1024).decode("utf-8")
        weather_data = json.loads(message)
        weather_window = customtkinter.CTkToplevel(app)
        weather_window.geometry("400x240")
        weather_window.title("Weather Information")

        header_label = customtkinter.CTkLabel(
            weather_window,
            text=f"{city_field.get()}, {state_field.get()}",
            font=customtkinter.CTkFont(weight="bold", size=18),
        )
        header_label.pack()

        temp_label = customtkinter.CTkLabel(
            weather_window, text=f"Temperature: {weather_data['temp']}°F"
        )
        temp_label.pack()
        feels_like_label = customtkinter.CTkLabel(
            weather_window, text=f"Feels Like: {weather_data['feels_like']}°F"
        )
        feels_like_label.pack()
        minimum_label = customtkinter.CTkLabel(
             weather_window, text=f"Today's Minimum Recorded: {weather_data['temp_min']}°F"
        )
        minimum_label.pack()

        maximum_label = customtkinter.CTkLabel(
            weather_window, text=f"Today's Maximum Recorded: {weather_data['temp_max']}°F"
        )
        maximum_label.pack()

        humidity_label = customtkinter.CTkLabel(
            weather_window, text=f"Humidity: {weather_data['humidity']}%"
        )
        humidity_label.pack()

        pressure_label = customtkinter.CTkLabel(
            weather_window, text=f"Atmospheric Pressure: {weather_data['pressure']}hPA"
        )
        pressure_label.pack()

        weather_window.after(100, weather_window.lift)
        weather_window.after(200, weather_window.focus)


def submit():
    city = city_field.get()
    state = state_field.get()
    location = f"{city},{state}"
    message = f"{location}".encode("utf-8")
    s.send(message)


city_label = customtkinter.CTkLabel(master=app, text="Enter city name:")
city_label.pack()
city_field = customtkinter.CTkEntry(master=app)
city_field.pack()

state_label = customtkinter.CTkLabel(master=app, text="Enter state name:")
state_label.pack()
state_field = customtkinter.CTkEntry(master=app)
state_field.pack()

submit_button = customtkinter.CTkButton(master=app, text="Submit", command=submit)
submit_button.pack(pady=8)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9123))

listen_thread = threading.Thread(target=listen_for_messages)
listen_thread.daemon = True
listen_thread.start()

app.mainloop()
