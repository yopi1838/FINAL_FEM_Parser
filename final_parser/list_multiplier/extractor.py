import numpy as np

class multiplier():
    def __init__(self, my_list):
        self.my_list = my_list
    
    def multiply_drift_ratio(self, result):
        result = []
        for x in self.my_list:
            a = x * 2 / 1000 * 100
            result.append(np.round(a,3))
        return result
    
    def multiply_load(self):
        result = []
        for x in self.my_list:
            a = x * 2 / 1000
            result.append(a)
        return result

