import os
from shutil import copyfile


def make_dir_with_templates():
    structure_address = os.path.abspath('my_project')
    for root_dir, dirs, files in os.walk(structure_address):
        for file in files:
            if file.endswith('.html'):
                directory_name = os.path.join('templates', os.path.basename(root_dir))
                if not os.path.exists(directory_name):
                    os.makedirs(directory_name)
                copyfile(os.path.join(root_dir, file), os.path.join(directory_name, file))


make_dir_with_templates()
