import os
import configparser

def read_config(config_file="config.ini"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, config_file)
    config = configparser.ConfigParser()
    config.read(config_path)
    return config