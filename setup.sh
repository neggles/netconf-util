#!/bin/bash

# make venv if not exist
if [ ! -d venv ]; then
    virtualenv -p python3 venv
fi

# set environment variables
export VENV=$(pwd)/venv

# activate venv
source $VENV/bin/activate

# update pip and setuptools
venv/bin/pip install --upgrade pip setuptools

# install local ncclient
venv/bin/pip install -e ./ncclient

# get argparse
