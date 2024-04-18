from typing import List, Tuple

#!/usr/bin/env python3
def element_length(lst: List[str]) -> List[Tuple[str, int]]:
        return [(i, len(i)) for i in lst]