from setuptools import setup

APP = ['app/main.py']
APP_NAME = "custom-timer" 
DATA_FILES = []
OPTIONS = {
    # resolve error: https://github.com/jaredks/rumps/issues/208#issuecomment-1817662981
    'argv_emulation': False,
    'packages': ['Quartz', 'psutil', 'sqlite3'],
    'includes': ['subprocess'],
    'excludes': ['Tkinter'],
    'iconfile': 'AppIcon/icon.png',
}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)