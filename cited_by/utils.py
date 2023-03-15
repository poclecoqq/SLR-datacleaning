import os 
from pathlib import Path
import pickle


dir_path = os.path.dirname(os.path.realpath(__file__))
output_dir = Path(dir_path)/'res'
output_dir.mkdir(parents=True, exist_ok=True)


def save_to_pkl(obj, f_name):
    with open(output_dir/f_name, 'wb') as f:
        pickle.dump(obj, f)


def load_pkl(f_name):
    with open(output_dir/f_name, 'rb') as f:
        obj = pickle.load(f)
    return obj
