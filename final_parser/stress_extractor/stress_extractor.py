import pandas as pd
import numpy as np
import csv
pd.options.mode.chained_assignment = None

def split(dfm, chunk_size, length):
    indices = index_marks(length, chunk_size)
    return np.split(dfm, indices)

def index_marks(nrows, chunk_size):
    return range(1 * chunk_size, (nrows // chunk_size + 1) * chunk_size, chunk_size)

def write_list_to_file(steps, filename, datalist):
        i = steps - 21
        with open(filename, 'w') as f:
            datas = np.array(datalist[i])
            for data in datas:
                f.write(str(data))
                f.write('\n')
            

def parse_csv(dataframe, stress_input, upper_limit, lower_limit):
    df = pd.read_csv(dataframe)
    stress_elements = df['Unnamed: 1']
    stress_id = df['Unnamed: 2']
    max_stress_id = df['Unnamed: 3']
    mid_stress_id = df['Unnamed: 4']
    min_stress_id = df['Unnamed: 5']
    tautetar_id = df['Unnamed: 6']
    shear_stress_id = df['Unnamed: 7']
    taurz_values = df['Unnamed: 8']
    df_object = pd.concat([stress_elements, stress_id, 
    max_stress_id, mid_stress_id, 
    min_stress_id, tautetar_id, shear_stress_id, taurz_values], axis=1)
    df_object.columns=['Element_number', 'id','Sxx', 'Syy', 'Szz','Txy', 'Tyz', 'Txz']
    ###Take only stress list
    stress_list = df_object[(df_object['id'] == 'Psg=')]
    stress_list['Element_number'] = stress_list['Element_number'].astype(int)
    ###Split the stress_list into 24
    stress_list_xx = stress_list[(stress_list['Element_number'] < int(upper_limit)) & (stress_list['Element_number'] > int(lower_limit))]
    length = df.shape[0]
    stress_inquiry = stress_list_xx[stress_input]
    stress_split = split(stress_inquiry, 24, length)
    return stress_split
