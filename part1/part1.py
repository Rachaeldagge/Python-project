import json
from datetime import datetime

import json
with open("/Users/rachaeldagge/Desktop/python-project-starter/part1/data/forecast_5days_a.json") as json_file: 
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
    return total, num_items


def process_weather(forecast_file): #these are a function
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    #return Minimum Temperature (mintemp) 
    pass

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))

#This is what I last worked on Thursday night***

lowtemp = [8.3, 10.6, 14.4, 14.4, 10.6]
lowesttemp = min(lowtemp)
print(f"The lowest temperature will be {format_temperature(lowesttemp)} and will occur on \n")
   
hightemp = [17.8, 19.4, 22.2, 22.2, 18.9]
highesttemp = max(hightemp)
print(f"The highest temperature will be {format_temperature(highesttemp)} and will occur on \n")


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


for key in json_data["DailyForecasts"]:
    #key == "[DailyForecasts":             #this is a string - good we want to find block line 13 onwards block
    #print(data["DailyForecasts"])
    date = (key["Date"])
    #print(date)
    mintemp = (key["Temperature"]["Minimum"]["Value"])
    mintemp_f = convert_f_to_c(mintemp)
    #converting to celcius
    maxtemp = (key["Temperature"]["Maximum"]["Value"])
    maxtemp_f = convert_f_to_c(maxtemp)
    #converting to celcius
    

    #print(mintemp,maxtemp)
    print(f"--------{convert_date(date)}--------")
    print(f"Minimum Temperature: {format_temperature(mintemp)}")
    print(f"Maximum Temperature: {format_temperature(maxtemp)}")
    
    day = (key["Day"]["LongPhrase"])
    print(f"Daytime: {day}")

    rainday = (key["Day"]["RainProbability"])
    print(f"    Chance of rain: {rainday}%")

    night = (key["Night"]["LongPhrase"])
    print(f"Nighttime: {night}")

    rainnight = (key["Night"]["RainProbability"])
    print(f"    Chance of rain: {rainnight}%\n")

    #min(iterable, *[key[mintemp], defult])
   
   
   
    #mintemp_avg = calculate_mean(mintemp)
    #print(int(mintemp_avg)

    #print(process_weather(mintemp))
    #print(process_weather(maxtemp))
    #print(f"Minimum Temperature:")

    

""" Key 1 is headline[0]. Key 2 is daily forecast[1]. 
There are 5 dictionaries (main items) inside the Daily forecast list. 
DailyForecast List has 15 keys (incl date, sun, epochDate)
Date is the first of the 15 keys - therefore position 0: date[0]
Date is a key with a value
date [0]
sun [2]
temperature [4]

"""


