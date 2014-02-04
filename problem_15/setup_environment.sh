#!/bin/bash

virtualenv env
env/bin/pip install -r requirements.txt
rm helpers.py
ln -s ../default/helpers.py ./
