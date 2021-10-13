import pandas as pd
import matplotlib.pyplot as plt


def babys_quantity():
    data_frame_1980 = pd.read_table('data/yob1880.txt', sep=',', engine='python', names=(['name', 'sex', 'quantity']))
    print('Число младенцев каждого пола за 1980 год')
    print(data_frame_1980.groupby('sex').sum().reset_index())
    return data_frame_1980


def total_data_frame(data_frame_1980):
    data_frame_1980['year'] = 1980
    total_data_frame = data_frame_1980
    for year in range(1981, 2011):
        this_data_frame = pd.read_table(f'data/yob{year}.txt', sep=',', engine='python', names=(['name', 'sex', 'quantity']))
        this_data_frame['year'] = year
        total_data_frame = pd.concat([total_data_frame, this_data_frame], ignore_index=True)
    print('Весь дата фрейм')
    print(total_data_frame)
    return total_data_frame


def quantity_for_every_year(total_data_frame):
    quantity_for_every_year = total_data_frame.groupby(['sex', 'year']).sum().reset_index()
    print('Сумма младенцев каждого пола для каждого года')
    print(quantity_for_every_year)

    quantity_for_every_year[quantity_for_every_year['sex'] == 'F'].drop('sex', axis=1).plot(x='year', y='quantity')
    quantity_for_every_year[quantity_for_every_year['sex'] == 'M'].drop('sex', axis=1).plot(x='year', y='quantity')

    plt.show()


def name_proportion(total_data_frame):
    total_quantity = total_data_frame['quantity'].sum()
    quantity_of_name = total_data_frame[['name', 'quantity']].groupby('name').sum().reset_index()
    name_proportion = quantity_of_name
    name_proportion['proportion'] = quantity_of_name['quantity']/total_quantity

    print('Доля данного имени от общего количества')
    print(name_proportion)

data_frame_1980 = babys_quantity()

total_data_frame = total_data_frame(data_frame_1980)

quantity_for_every_year(total_data_frame)

name_proportion(total_data_frame)