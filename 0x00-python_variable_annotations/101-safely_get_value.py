#!/usr/bin/env python3
from typing import Dict, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Dict[str, T], key: str, default: T = None) -> T:
    """_summary_

    Args:
        dct (Dict[str, T]): _description_
        key (str): _description_
        default (T, optional): _description_. Defaults to None.

    Returns:
        T: _description_
    """    
    if key in dct:
        return dct[key]
    else:
        return default
