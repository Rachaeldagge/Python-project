import json
import plotly.express as px
import pandas as pd
from datetime import datetime

import json
with open("./data/forecast_5days_a.json") as json_file: 
    json_data = json.load(json_file)


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    C = round((temp_in_farenheit-32)*5/9,1)
    return C


def graph_min_max(json_data):
    days, min_temps, high_temps = [], [], []

    for day in list(json_data["DailyForecasts"]):
        current_date = convert_date(day["Date"])

        min_temp = convert_f_to_c(day["Temperature"]["Minimum"]["Value"])
        max_temp = convert_f_to_c(day["Temperature"]["Maximum"]["Value"])

        high_temps.append(max_temp)
        min_temps.append(min_temp)

        days.append(current_date)


    df = pd.DataFrame(
        data=list(zip(min_temps, high_temps)), 
        index=days)
    fig = px.line(df)
    fig.show()

def graph_real_feel(json_data):
    days, min_temps, min_rf_temps, min_rf_shade_temps = [], [], [], []

    for day in list(json_data["DailyForecasts"]):
        current_date = convert_date(day["Date"])

        min_temp = convert_f_to_c(day["Temperature"]["Minimum"]["Value"])
        min_rf_temp = convert_f_to_c(day["RealFeelTemperature"]["Minimum"]["Value"])
        min_shade_temp = convert_f_to_c(day["RealFeelTemperatureShade"]["Minimum"]["Value"])
        
        min_temps.append(min_temp)
        min_rf_temps.append(min_rf_temp)
        min_rf_shade_temps.append(min_shade_temp)

        days.append(current_date)

    print(days, min_temps, min_rf_temps, min_rf_shade_temps, sep='\n****\n')

    df = pd.DataFrame(
        data=list(zip(min_temps, min_rf_temps, min_rf_shade_temps)), 
        index=days)
    fig = px.line(df)
    fig.show()

if __name__ == "__main__":
    graph_min_max(json_data)
    graph_real_feel(json_data)

