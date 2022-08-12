from os import system
from os import path

def call_ui():
    if path.exists('build/release/ui.exe'):
        system(path.abspath('build/release/ui.exe'))
    elif path.exists('ui/build/release/ui.exe'):
        system(path.abspath('ui/build/release/ui.exe'))
    else:
        print('Path not exists')