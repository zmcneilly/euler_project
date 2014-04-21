#!/bin/bash

rm -Rf ../*/env/
virtualenv env
env/bin/pip install -r requirements.txt
rm helpers.py
rm structures.py
ln -s ../default/helpers.py ./
ln -s ../default/structures.py ./
