import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64  


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read yaml file and return
    
    Args:
        path_to_yaml (Path): path to yaml file

    Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox object
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file loaded from {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Yaml file at {path_to_yaml} is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create directories from a list of paths
    
    Args:
        path_to_directories (list): list of paths to directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to True.
    """
    for path in path_to_directories:
        if not os.path.exists(path):
            os.makedirs(path)
            if verbose:
                logger.info(f"Created directory at {path}")

@ensure_annotations
def save_json(path_to_json: Path, content: any):
    """Save json file
    
    Args:
        path_to_json (Path): path to json file
        content (any): content to save
    """
    with open(path_to_json, "w") as json_file:
        json.dump(content, json_file, indent=4)

    logger.info(f"Saved json file at {path_to_json}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load json file
    
    Args:
        path (Path): path to json file
        
    Returns:
            ConfigBox: ConfigBox object
    """
    with open(path) as json_file:
        content = json.load(json_file)

    logger.info(f"Loaded json file from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save binary file
    
    Args:
        data (Any): data to save
        path (Path): path to save
    """
    joblib.dump(data, path)
    logger.info(f"Saved binary file at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load binary file
    
    Args:
        path (Path): path to load
        
    Returns:
            Any: data
    """
    data = joblib.load(path)
    logger.info(f"Loaded binary file from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Get size inKB
    
    Args:
        path (Path): path to file
        
    Returns:
            str: size in KB
    """
    size_in_kb = os.path.getsize(path) / 1024
    return f"~ {size_in_kb} KB"

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as image_file:
        return base64.b64encode(image_file.read())
    
