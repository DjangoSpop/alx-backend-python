from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    zoomed_in: Tuple[int, ...] = tuple(
        item
        for item in lst
        for _ in range(factor)
    )
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
print(zoom_2x)  # Output: (12, 12, 72, 72, 91, 91)

zoom_3x = zoom_array(array, 3)
print(zoom_3x)  # Output: (12, 12, 12, 72, 72, 72, 91, 91, 91)
