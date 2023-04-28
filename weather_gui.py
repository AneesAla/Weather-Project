import tkinter as tk
import socket
import json
import threading


class WeatherGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.setup_networking()

    def create_widgets(self):
        self.city_label = tk.Label(self, text="Enter city name:")
        self.city_label.pack()
        self.city_field = tk.Entry(self)
        self.city_field.pack()

        self.state_label = tk.Label(self, text="Enter state name:")
        self.state_label.pack()
        self.state_field = tk.Entry(self)
        self.state_field.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        city = self.city_field.get()
        state = self.state_field.get()
        location = f"{city},{state}"
        message = f"{location}".encode("utf-8")
        self.s.send(message)

    def setup_networking(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((socket.gethostname(), 9123))

        self.listen_thread = threading.Thread(target=self.listen_for_messages)
        self.listen_thread.daemon = True
        self.listen_thread.start()

    def listen_for_messages(self):
        while True:
            message = self.s.recv(1024).decode("utf-8")
            self.update_gui(json.loads(message))

    def update_gui(self, weather_data):
        weather_window = tk.Toplevel(self)
        weather_window.title("Weather Information")

        temp_label = tk.Label(
            weather_window, text=f"Temperature: {weather_data['temp']} F"
        )
        temp_label.pack()
        feels_like = tk.Label(
            weather_window, text=f"Feels Like: {weather_data['feels_like']}"
        )
        feels_like.pack()
        sea_level_label = tk.Label(
            weather_window, text=f"Sea Level: {weather_data['sea_level']}"
        )
        sea_level_label.pack()
        humidity_label = tk.Label(
            weather_window, text=f"Humidity: {weather_data['humidity']}"
        )
        humidity_label.pack()
