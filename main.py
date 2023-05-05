import csv
from datetime import datetime

import matplotlib.pyplot as plt

def zwroc_klucz(dictionary, string):
    for key, value in dictionary.items():
        if value == string:
            return key

def zwroc_date_tmax_tmin(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        first_row = next(reader)
        dictionary = {}
        for index, item in enumerate(first_row):
            dictionary.update({index: item})

        tmax = zwroc_klucz(dictionary, 'TMAX')
        tmin = zwroc_klucz(dictionary, 'TMIN')
        date_key = zwroc_klucz(dictionary, 'DATE')


        highs, lows , dates= [], [], []
        for row in reader:
            date = datetime.strptime(row[date_key], '%Y-%m-%d')
            try:
                high = int(row[tmax])
                low = int(row[tmin])
            except ValueError:
                print(f'Brak danych dla {date}')
            else:
                highs.append(high)
                lows.append(low)
                dates.append(date)
        return dates, highs, lows

def wyswietl_roznice_temperatur(dates, temperatures1, temperatures2):
    plt.style.use('seaborn-v0_8-white')
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures1, c='red', alpha=0.5)
    ax.plot(dates, temperatures2, c='blue', alpha=0.5)
    ax.fill_between(dates, temperatures1, temperatures2, facecolor='blue', alpha=0.2)
    ax.set_title('Roznica temperatur', fontsize=24)
    ax.set_xlabel('', fontsize=16)
    ax.set_ylabel('Temperatura [F]', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.set_ylim([15, 135])

filename = r'data\death_valley_2021_simple.csv'
dates1, highs1, lows1 = zwroc_date_tmax_tmin(filename)

filename = r'data\sitka_weather_2021_simple.csv'
dates2, highs2, lows2 = zwroc_date_tmax_tmin(filename)

wyswietl_roznice_temperatur(dates1, highs1, highs2)
wyswietl_roznice_temperatur(dates1, lows1, lows2)
wyswietl_roznice_temperatur(dates1, highs1, lows1)
plt.show()