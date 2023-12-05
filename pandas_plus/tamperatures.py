import copy

import matplotlib.pyplot as plt
import pandas as pd


def wheater_plot(year: int, city: str,years_later:int = 10):
    # pd.set_option('display.max_columns', 20)
    data = pd.read_csv("temperature.csv")
    filtered_data = data[data['City'] == city]
    data_10_years_later = filtered_data[filtered_data["year"] == year+years_later].sort_values(by="month")
    filtered_data = filtered_data[filtered_data["year"] == year]
    filtered_data = filtered_data.sort_values(by="month")

    # filtered_by_query = data.query(f'City == "{city}" & year == {year}')

    # print(filtered_by_query)
    temp_celcius = [(item - 32) * (5 / 9) for item in filtered_data.AverageTemperatureFahr]
    temp_celcius_10_year_later = [(item - 32) * (5 / 9) for item in data_10_years_later.AverageTemperatureFahr]

    while len(temp_celcius) < 12:
        temp_celcius.append(-99)

    while len(temp_celcius_10_year_later) < 12:
        temp_celcius_10_year_later.append(-99)

    month = [i for i in range(1, 13)]
    print(temp_celcius)
    print(month)

    plt.plot(month, temp_celcius, color='r', marker='o', label=f'Temperatures for {city} in {year}')
    plt.plot(month,temp_celcius_10_year_later,color='g',marker='*',label=f'Temperatures for {city} in {year+years_later}')
    plt.xlabel("Month number")
    plt.ylabel("Temparature (°C)")
    plt.legend()
    plt.show()


wheater_plot(1970, "Auckland",30)
