import os
from pathlib import Path
from collections import Counter


def size_():
    keys = []
    statistic_object = os.path.join(Path.cwd(), 'some_data')
    with os.scandir(statistic_object) as items:
        for item in items:
            if item.is_file():
                size = item.stat().st_size
                key = 10 ** len(str(size))
                keys.append(key)
    statistic = dict(Counter(keys))
    print(statistic)


size_statistic()
