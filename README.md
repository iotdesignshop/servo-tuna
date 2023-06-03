# servo-tuna
Servo tuning system for HOPE robot

# Setup
This package is designed to run on a Raspberry Pi running Raspbian Jessie. Other versions may work fine, but as you know with Pi stuff, YMMV if you stray off the beaten path. First version was tested on a Pi Zero W, which is a pretty light platform so if you have more horsepower than that, you should be good.

## Python and Virtual Environment Setup
First, create a virtual environment for a Python >= 3.7 interpreter - if you don't know how to do that, consult the Python documentation. (https://docs.python.org/3/library/venv.html) 

With your environment active, run:
```
pip install -r requirements.txt
```

## Adafruit Blinka Setup
Once your environment is ready and packages downloaded, we have provided a script to install Adafruit Blinka and modify Raspbian as needed. If you want all the details, check out the Adafruit documentation. https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

To run our script:

```
chmod +x install-blinka.sh
sudo ./install-blinka.sh
```
