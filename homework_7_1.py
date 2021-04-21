import os

dir_path = os.path.join('my_project', 'settings', '../main_app', '../admin_app', '../auth_app')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
