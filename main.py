import pandas as pd
import matplotlib.pyplot as plt


def babys_quantity():
    data_frame_1880 = pd.read_table('data/yob1880.txt', sep=',', engine='python', names=(['name', 'sex', 'quantity']))
    print('Число младенцев каждого пола за 1880 год')
    print(data_frame_1880.groupby('sex').sum().reset_index())
    return data_frame_1880


def total_data_frame(data_frame_1880):
    data_frame_1880['year'] = 1880
    total_data_frame = data_frame_1880
    for year in range(1881, 2011):
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

    quantity_for_every_year[quantity_for_every_year['sex'] == 'F'].drop('sex', axis=1).plot(x='year', y='quantity', label='Female')
    quantity_for_every_year[quantity_for_every_year['sex'] == 'M'].drop('sex', axis=1).plot(x='year', y='quantity', label='Male')

    plt.show()


def name_proportion(total_data_frame):
    total_quantity = total_data_frame['quantity'].sum()
    quantity_of_name = total_data_frame[['name', 'quantity']].groupby('name').sum().reset_index()
    name_proportion = quantity_of_name
    name_proportion['proportion'] = quantity_of_name['quantity']/total_quantity

    print('Доля данного имени от общего количества')
    print(name_proportion)
    return total_quantity


def jonny_natalie_bob_graphics(total_data_frame, total_quantity):
    total_data_frame_without_sex = total_data_frame.drop('sex', axis=1)

    jonny_data_frame = total_data_frame_without_sex[total_data_frame_without_sex['name'] == 'Jonny'].copy(deep=True)
    natalie_data_frame = total_data_frame_without_sex[total_data_frame_without_sex['name'] == 'Natalie'].copy(deep=True)
    bob_data_frame = total_data_frame_without_sex[total_data_frame_without_sex['name'] == 'Bob'].copy(deep=True)
    michael_data_frame = total_data_frame_without_sex[total_data_frame_without_sex['name'] == 'Michael'].copy(deep=True)


    jonny_data_frame.plot(x='year', y='quantity', label='Jonny quantity')
    natalie_data_frame.plot(x='year', y='quantity', label='Natalie quantity')
    bob_data_frame.plot(x='year', y='quantity', label='Bob quantity')
    michael_data_frame.plot(x='year', y='quantity', label='Bob quantity')

    jonny_data_frame['proportion'] = jonny_data_frame['quantity']/total_quantity
    natalie_data_frame['proportion'] = natalie_data_frame['quantity']/total_quantity
    bob_data_frame['proportion'] = bob_data_frame['quantity']/total_quantity
    michael_data_frame['proportion'] = michael_data_frame['quantity']/total_quantity

    jonny_data_frame.drop('quantity', axis=1).plot(x='year', y='proportion', label='Jonny proportion')
    natalie_data_frame.drop('quantity', axis=1).plot(x='year', y='proportion', label='Natalie proportion')
    bob_data_frame.drop('quantity', axis=1).plot(x='year', y='proportion', label='Bob proportion')
    michael_data_frame.drop('quantity', axis=1).plot(x='year', y='proportion', label='My proportion')
    plt.show()

    return total_data_frame_without_sex


def popular_names(total_data_frames_without_sex):
    print('Самые популярные имена по годам')
    print(total_data_frames_without_sex.loc[total_data_frames_without_sex.groupby('year')['quantity'].idxmax()])


data_frame_1880 = babys_quantity()

total_data_frame = total_data_frame(data_frame_1880)

quantity_for_every_year(total_data_frame)

total_quantity = name_proportion(total_data_frame)

total_data_frame_without_sex = jonny_natalie_bob_graphics(total_data_frame, total_quantity)

popular_names(total_data_frame_without_sex)