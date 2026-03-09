import tkinter as tk
import requests


# -----------------------
# Pollution logic
# -----------------------

def classify_air_quality(temp, wind):

    pollution_index = (temp * 2) + wind

    if pollution_index <= 50:
        category = "Good"
    elif pollution_index <= 100:
        category = "Moderate"
    elif pollution_index <= 200:
        category = "Unhealthy"
    else:
        category = "Hazardous"

    return pollution_index, category


# -----------------------
# Weather function
# -----------------------

def get_weather():

    city = city_entry.get().strip()

    if city == "":
        result_label.config(text="Enter a city name")
        return

    try:

        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()

        if "results" not in geo_data:
            result_label.config(text="City not found")
            return

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]
        city_name = geo_data["results"][0]["name"]

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        temp = weather_data["current_weather"]["temperature"]
        wind = weather_data["current_weather"]["windspeed"]

        pollution_value, pollution_category = classify_air_quality(temp, wind)

        result_text = f"""
City: {city_name}

Temperature: {temp} °C
Wind Speed: {wind} km/h

Pollution Index: {pollution_value:.1f}
Air Quality: {pollution_category}
"""

        result_label.config(text=result_text)

    except:
        result_label.config(text="Error fetching weather data")


# -----------------------
# GUI
# -----------------------

root = tk.Tk()
root.title("Weather & Pollution Checker")
root.geometry("520x420")
root.resizable(False, False)


# Load background image
bg = tk.PhotoImage(file="weather.png")

# Main background
background = tk.Label(root, image=bg)
background.place(x=0, y=0, relwidth=1, relheight=1)


# Wrapper frame
wrapper = tk.Frame(root, width=380, height=260)
wrapper.place(relx=0.5, rely=0.5, anchor="center")

# Wrapper background image
wrapper_bg = tk.Label(wrapper, image=bg)
wrapper_bg.place(x=0, y=0, relwidth=1, relheight=1)


# Title
title = tk.Label(
    wrapper,
    text="Weather & Air Quality",
    font=("Arial",18,"bold"),
    fg="black"
)
title.pack(pady=10)


# City label
city_label = tk.Label(
    wrapper,
    text="Enter City Name",
    fg="black"
)
city_label.pack()


# Entry
city_entry = tk.Entry(
    wrapper,
    font=("Arial",11),
    width=25
)
city_entry.pack(pady=8)


# Button
check_button = tk.Button(
    wrapper,
    text="Check Weather",
    command=get_weather
)
check_button.pack(pady=10)


# Result
result_label = tk.Label(
    wrapper,
    text="",
    fg="black",
    justify="center",
    font=("Arial",11)
)
result_label.pack(pady=10)


root.mainloop()