#!/bin/bash

python3 -m venv shrinevisit
source shrinevisit/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py