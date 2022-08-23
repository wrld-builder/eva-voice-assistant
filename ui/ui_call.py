from os import system
from os import path

def call_ui():
    if path.exists('build/ui.exe'):
        system(path.abspath('build/ui.exe'))
    elif path.exists('ui/build/ui.exe'):
        system(path.abspath('ui/build/ui.exe'))
    else:
        print('Path build/ui.exe and ui/build/ui.exe not exists')