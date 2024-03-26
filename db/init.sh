#!/bin/bash
# run script as sudo inside postgresql container

apk add python3 py3-pip;
pip install -r app/requirements.txt;
python3 app/init_db.py;
