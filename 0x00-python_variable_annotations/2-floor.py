#!/usr/bin/env python3
def floor(n: float) -> float:
    """_summary_

    Args:
        n (float): _description_

    Returns:
        float: _description_
    """    
    return n // 1 if n >= 0 else -(-n // 1)
