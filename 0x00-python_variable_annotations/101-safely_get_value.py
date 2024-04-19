#!/usr/bin/env python3
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """_summary_

    Args:
        dct (Mapping[Any, Any]): _description_
        key (Any): _description_
        default (Union[T, None], optional): _description_. Defaults to None.

    Returns:
        Union[Any, T]: _description_
    """    
    if key in dct:
        return dct[key]
    else:
        return default
    