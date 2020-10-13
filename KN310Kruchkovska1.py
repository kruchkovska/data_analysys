import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


def scatter(date_column, second_column):
    plt.figure(facecolor='#78a5a3')
    plt.scatter(date_column, second_column, edgecolor='#523634')
    plt.legend([second_column.name])
    plt.title(f'{date_column.name} - {second_column.name}')
    plt.show()


def pie(X):
    labels = np.unique(X)
    sizes = [X[X == x].shape[0] for x in labels]
    v = sorted(zip(labels, sizes), key=lambda x: x[-1])
    labels = [k[0] for k in v]
    sizes = [k[1] for k in v]
    labels = ['Others'] + labels[-3:]
    sizes = [sum(sizes[:-3])] + sizes[-3:]
    plt.figure(facecolor='#ddc5a2', edgecolor='#523634')
    plt.pie(sizes, labels=labels)
    plt.show()


def linear(date_column, second_column):
    plt.figure(facecolor='#78a5a3', edgecolor='#523634')
    plt.plot(date_column, second_column, color='#ce5a57')
    plt.legend([second_column.name])
    plt.xlabel(date_column.name)
    plt.ylabel(second_column.name)
    plt.title(f'{date_column.name} - {second_column.name}')
    plt.show()


def vizualize():
    print('Choose what type of diagram you want:\n'+
          '1_________linear\n'+
          '2____________pie\n'+
          '3________scatter\n'+
          '666_________exit')
    n = int(input())
# Pressure, Temperature, Humidity, Dew Point, Wind Speed, Wind, Condition, Wind Gust
    print('What value do you want to see in your diagram?')
    value = input()
    if n == 1:
        linear(date_frame['Date/Time'], date_frame[value])
    elif n == 2:
        pie(date_frame[value])
    elif n == 3:
        scatter(date_frame['Date/Time'], date_frame[value])
        exit()
    elif n == 666:
        exit()
    else:
        print('You have entered wrong value.')
        vizualize()


def num(string, numb):
    numbers = []
    for n in range(len(string)):
        numbers.append(int(str(string[n])[:numb]))
    return numbers


def str_float(string):
    string1 = string.str.replace(',', '.')
    string2 = pd.to_numeric(string1)
    return string2


def date(str_date):
    correct = []
    for i in range(len(str_date)):
        temp_date = datetime.strptime(str_date[i], '%d.%b').strftime('%d.%m.2019')
        correct.append(temp_date)
    return correct


def time(str_time):
    str_time = pd.to_datetime(str_time).apply(lambda x: x.strftime(r'%H:%M:%S'))
    return str_time


def parse(df):
    df['Date'] = df['day/month'].replace(to_replace=list(df['day/month']), value=date(list(df['day/month'])))
    df['Time'] = pd.to_datetime(df['Time']).apply(lambda x: x.strftime(r'%H:%M'))
    df['Date/Time'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], infer_datetime_format=True)
    df['Wind Gust'] = num(list(df['Wind Gust']), -4)
    df['Pressure'] = list(str_float(df['Pressure']))
    df['Humidity'] = list(num(df['Humidity'], -1))
    df['Wind Speed'] = list(num(df['Wind Speed'], -4))
    df['Time'] = list(time(df['Time']))
    return df


date_frame = pd.read_csv('DATABASE.csv', sep=';')

parse(date_frame)
date_frame = date_frame.sort_values(by='Date/Time')
vizualize()
