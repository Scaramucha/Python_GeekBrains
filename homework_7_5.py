import os
from pathlib import Path


def size_statistic():
    full_statistic = {}
    statistic_object = os.path.join(Path.cwd(), 'some_data')
    with os.scandir(statistic_object) as items:
        for item in items:
            if item.is_file():
                size = item.stat().st_size
                key = 10 ** len(str(size))
                extensions_flag = item.name.index('.')
                extensions = item.name[extensions_flag:]
                if key not in full_statistic.keys():
                    full_statistic[key] = [1, [extensions]]
                elif key in full_statistic.keys():
                    full_statistic[key][0] += 1
                    if extensions not in full_statistic[key][1]:
                        full_statistic[key][1].append(extensions)
    full_statistic_finish_version = {}
    for key_value in full_statistic.keys():
        full_statistic_finish_version[key_value] = tuple(full_statistic[key_value])

    return (full_statistic_finish_version)


with open('test.json', 'w', encoding='utf-8') as file:
    for key, value in size_statistic().items():
        file.write(f'\n{key}: {value}')
