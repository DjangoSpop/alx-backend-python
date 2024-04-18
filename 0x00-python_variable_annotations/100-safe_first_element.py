# The types of the elements of the input are not know
#!/usr/bin/env python3
def safe_first_element(lst):
    """_summary_

    Args:
        lst (_type_): _description_

    Returns:
        _type_: _description_
    """    
    if lst:
        return lst[0]
    else:
        return None
