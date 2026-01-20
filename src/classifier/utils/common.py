import os
from box.exceptions import BoxValueError
import yaml
from src.classifier import logger
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
import base64
from box import ConfigBox
import pickle
import numpy as np

# this file is to read the yaml file proper and can be used in a docker string
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns it as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Returns:
        ConfigBox: The content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
        
# to create data ingestion to create directories
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    create list of directories

    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): ignore if multiple dirs is to be created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            # assuming you have a logger set up, otherwise print
            print(f"created directory at: {path}")

# evaluation metrics to store that json file we need this
@ensure_annotations
def save_json(self, path_to_json: Path, data: dict) -> None:
    """
    Saves a dictionary to a JSON file.

    Args:
        path_to_json (Path): The path to the JSON file.
        data (dict): The dictionary to save.
    """
    with open(path_to_json, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        logger.info(f"json file: {path_to_json} saved successfully")
    return None

# to load a json file
@ensure_annotations
def load_json(self, path_to_json: Path) -> dict:
    """
    Loads a dictionary from a JSON file.

    Args: 
        path_to_json (Path): The path to the JSON file.

    Returns:
        dict: The dictionary loaded from the JSON file.
    """
    with open(path_to_json, 'r') as json_file:
        data = json.load(json_file)
        logger.info(f"json file: {path_to_json} loaded successfully")
        return data

# to save a numpy array
@ensure_annotations
def save_numpy(self, path_to_numpy: Path, data: np.ndarray) -> None:
    """
    Saves a numpy array to a numpy file.

    Args:
        path_to_numpy (Path): The path to the numpy file.
        data (np.ndarray): The numpy array to save.
    """
    np.save(path_to_numpy, data)
    logger.info(f"numpy file: {path_to_numpy} saved successfully")

# to load a numpy array
@ensure_annotations
def load_numpy(self, path_to_numpy: Path) -> np.ndarray:
    """
    Loads a numpy array from a numpy file.

    Args:
        path_to_numpy (Path): The path to the numpy file.

    Returns:
        np.ndarray: The numpy array loaded from the numpy file.
    """
    data = np.load(path_to_numpy)
    logger.info(f"numpy file: {path_to_numpy} loaded successfully")
    return data

# to save a pickle file
@ensure_annotations
def save_pickle(self, path_to_pickle: Path, data: Any) -> None:
    """
    Saves a pickle file.

    Args:
        path_to_pickle (Path): The path to the pickle file.
        data (Any): The data to save.
    """
    with open(path_to_pickle, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)
        logger.info(f"pickle file: {path_to_pickle} saved successfully")

# to load a pickle file
@ensure_annotations
def load_pickle(self, path_to_pickle: Path) -> Any:
    """
    Loads a pickle file.

    Args:
        path_to_pickle (Path): The path to the pickle file.

    Returns:
        Any: The data loaded from the pickle file.
    """
    with open(path_to_pickle, 'rb') as pickle_file:
        data = pickle.load(pickle_file)
        logger.info(f"pickle file: {path_to_pickle} loaded successfully")
        return data

# to save a joblib file
@ensure_annotations
def save_joblib(self, path_to_joblib: Path, data: Any) -> None:
    """
    Saves a joblib file.

    Args:
        path_to_joblib (Path): The path to the joblib file.
        data (Any): The data to save.
    """
    joblib.dump(data, path_to_joblib)
    logger.info(f"joblib file: {path_to_joblib} saved successfully")

# to load a joblib file
@ensure_annotations
def load_joblib(self, path_to_joblib: Path) -> Any:
    """
    Loads a joblib file.

    Args:
        path_to_joblib (Path): The path to the joblib file.

    Returns:
        Any: The data loaded from the joblib file.
    """
    data = joblib.load(path_to_joblib)
    logger.info(f"joblib file: {path_to_joblib} loaded successfully")
    return data

# to encode an image
def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

# to decode the image.
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Gets the size of a file.    
    Args:
        path (Path): The path to the file.
    Returns:
        str: The size of the file in MB.
    """
    size_in_kb = os.path.getsize(path)
    return f"{round(size_in_kb / 1024, 2)} KB"
