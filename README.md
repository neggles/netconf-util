netconf-util
===========

Getting Started
---------------

- Clone this repo and CD in

    `git clone https://github.com/neg2led/netconf-util.git && cd netconf-util`

- Run setup.sh to create a venv and install the appropriate modules

    `bash ./setup.sh`

- Run the utility

    `python3 netconf-util.py -d node-ip \[-u user\] \[-p password\] \[--rcs\]`


Only host is mandatory, other options have some sane defaults. Run `python3 netconf-util.py --help` for some info.