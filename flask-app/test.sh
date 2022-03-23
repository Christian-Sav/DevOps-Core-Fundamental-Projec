#! /bin/bash
sudo apt update && sudo apt -y install python3 python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install wheel
python setup.py bdist_wheel
python3 -m pytest --cov=Project --cov-report=html
