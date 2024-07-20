# close existing app if it is running
killall custom-timer

rm -rf build dist

python app/setup.py py2app

open dist/custom-timer.app