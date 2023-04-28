import tkinter as tk
from weather_gui import WeatherGUI

root = tk.Tk()
app = WeatherGUI(master=root)
app.mainloop()
