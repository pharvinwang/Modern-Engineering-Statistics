import pandas as pd
import numpy as np

def load_csv(file_path):
    return pd.read_csv(file_path)

def generate_example_data(case='rainfall', n=25):
    np.random.seed(42)
    if case=='rainfall':
        return np.random.normal(120,25,n)
    elif case=='displacement':
        return np.random.normal(3.0,0.5,n)
    elif case=='quality':
        return np.random.binomial(1,0.92,n)
