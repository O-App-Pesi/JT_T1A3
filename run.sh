#!/bin/bash

# check if python is installed
python3 -m venv shrinevisit
# check if venv already exists
source shrinevisit/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py