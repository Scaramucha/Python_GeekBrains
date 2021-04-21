import os
from pathlib import Path


def create_structure():
    with open('config.yaml', 'r', encoding='utf-8')as f:
        project_address = Path.cwd()
        for line in f:
            object_name = line.strip('\n -')
            if line.startswith('-'):
                project_address = project_address.joinpath(object_name)
                if not os.path.exists(project_address):
                    os.mkdir(project_address)
            else:
                object_name = project_address.joinpath(object_name)
                if not os.path.exists(object_name):
                    open(object_name, 'w', encoding='utf-8').close()


create_structure()
