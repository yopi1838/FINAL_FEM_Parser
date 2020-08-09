from stress_extractor import stress_extractor, file_read
from tqdm import tqdm, trange
import csv, os, sys
step = int(input('Steps to observe: '))
stress_input = input('Pick the stress to observe: ')
upper_limit = input('Set upper limit for elements: ')
ul_int = int(upper_limit)
lower_limit = input('Set lower limit for elements: ')
try:
    data = file_read.file_read()
    for i in trange(100, desc="foo", bar_format="{l_bar}{bar:10}{r_bar}{bar:-10b}"):
        r = stress_extractor.parse_csv(data, stress_input, upper_limit=upper_limit, lower_limit=lower_limit)
    stress_extractor.write_list_to_file(step, 'extracted/%s_%d_el%d.csv' %(stress_input,step, ul_int), r)
except Exception as e:
    print(e)