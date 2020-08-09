import json
from pprint import pprint
from datetime import datetime

import json
with open("./data/forecast_5days_a.json") as json_file: 
    json_data = json.load(json_file)



DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

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

def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    return round(total / num_items, ndigits=1)

#Trying to calculate mean***#
#calculate_mean(63.8, 5)
#print(f"The mean temperature will be {calculate_mean}")
#Trying to calculate mean***

#Dates = [
        #["Friday 19 June 2020", 8.3]

#print(min{min(Dates)})
#]
#minIndex = myList.index(min(myList))
#mylist = key["Temperature"]["Minimum"]
#this is what I last worked on - Thursday night***


#functions are listed above


def print_daily_forecasts(data):
    result = ""
    for key in data["DailyForecasts"]:
        #key == "[DailyForecasts":             #this is a string - good we want to find block line 13 onwards block
        #print(data["DailyForecasts"])
        date = (key["Date"])
        #print(date)
        mintemp_f = (key["Temperature"]["Minimum"]["Value"])
        mintemp = convert_f_to_c(mintemp_f)
        #converting to celcius
        maxtemp_f = (key["Temperature"]["Maximum"]["Value"])
        maxtemp = convert_f_to_c(maxtemp_f)
        #converting to celcius
        

        #print(mintemp,maxtemp)
        result += f"\n-------- {convert_date(date)} --------\n"
        result += f"Minimum Temperature: {format_temperature(mintemp)}\n"
        result += f"Maximum Temperature: {format_temperature(maxtemp)}\n"
        

        day = (key["Day"]["LongPhrase"])
        result += f"Daytime: {day}\n"

        rainday = (key["Day"]["RainProbability"])
        result += f"    Chance of rain:  {rainday}%\n"

        night = (key["Night"]["LongPhrase"])
        result += f"Nighttime: {night}\n"

        rainnight = (key["Night"]["RainProbability"])
        result += f"    Chance of rain:  {rainnight}%\n"

    return result

def process_weather(forecast_file): #these are a function
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """

    import json
    with open(forecast_file) as json_file: 
        json_data = json.load(json_file)

    lowest_temp, highest_temp = 100, 0
    lowest_date, highest_date = "", ""
    high_temps, low_temps = [], []

    days = list(json_data["DailyForecasts"])

    for day in days:
        current_date = convert_date(day["Date"])
        if highest_date == "": highest_date = current_date
        if lowest_date == "": lowest_date = current_date

        min_temp = convert_f_to_c(day["Temperature"]["Minimum"]["Value"])
        max_temp = convert_f_to_c(day["Temperature"]["Maximum"]["Value"])
        
        if min_temp < lowest_temp:
            lowest_temp = min_temp
            lowest_date = current_date

        if max_temp > highest_temp:
            highest_temp = max_temp
            highest_date = current_date
        
        high_temps.append(max_temp)
        low_temps.append(min_temp)

    result = f"{len(low_temps)} Day Overview\n"
    result += f"    The lowest temperature will be {format_temperature(lowest_temp)}, and will occur on {lowest_date}.\n"
    result += f"    The highest temperature will be {format_temperature(highest_temp)}, and will occur on {highest_date}.\n"
    avg_low = calculate_mean(total=sum(low_temps),num_items=len(low_temps))
    result += f"    The average low this week is {format_temperature(avg_low)}.\n"
    avg_high = calculate_mean(total=sum(high_temps),num_items=len(high_temps))
    result += f"    The average high this week is {format_temperature(avg_high)}.\n"

    result += print_daily_forecasts(json_data)

    return result+"\n"


if __name__ == "__main__":
    # pass
    print(process_weather('./data/forecast_5days_a.json'))
    # print_daily_forecasts()
    # print(process_weather("data/forecast_5days_a.json"))