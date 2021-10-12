import pandas as pd
from pandas import Series, DataFrame

def babys_quantity():
    data_frame_1980 = pd.read_table('data/yob1880.txt', sep=',', engine='python', names=(['name', 'sex', 'quantity']))
    print(data_frame_1980.groupby('sex').aggregate(sum))
    return data_frame_1980

def total_data_frame(data_frame_1980):
    data_frame_1980['year'] = 1980
    total_data_frame = data_frame_1980
    for year in range(1981, 2011):
        this_data_frame = pd.read_table(f'data/yob{year}.txt', sep=',', engine='python', names=(['name', 'sex', 'quantity']))
        this_data_frame['year'] = year
        total_data_frame = pd.concat([total_data_frame, this_data_frame], ignore_index=True)
    print(total_data_frame)



data_frame_1980 = babys_quantity()
total_data_frame(data_frame_1980)