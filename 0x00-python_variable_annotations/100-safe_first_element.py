# The types of the elements of the input are not know
#!/usr/bin/env python3
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
