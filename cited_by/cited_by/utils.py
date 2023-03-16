import os
from pathlib import Path
import pickle
import yaml

dir_path = os.path.dirname(os.path.realpath(__file__))
input_dir = Path(dir_path)/'in'
output_dir = Path(dir_path)/'out'
output_dir.mkdir(parents=True, exist_ok=True)


def save_to_pkl(obj, f_name):
    with open(output_dir/f_name, 'wb') as f:
        pickle.dump(obj, f)


def load_pkl(f_name):
    with open(output_dir/f_name, 'rb') as f:
        obj = pickle.load(f)
    return obj


def save_to_yaml(obj, f_name):
    with open(output_dir/f_name, 'w') as f:
        yaml.dump(obj, f, width=1000)


def load_yaml(f_name):
    with open(input_dir/f_name, 'r') as f:
        res = yaml.load(f)
    return res
