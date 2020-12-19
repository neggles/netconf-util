netconf-util
===========

This is just a little python script thing to make handling Ericsson RBS/pRBS netconf XML get/set more convenient.
It supports using ssh-agent installed keys

Getting Started
---------------

- Clone this repo and CD in

    `git clone https://github.com/neg2led/netconf-util.git && cd netconf-util`

- Run setup.sh to create a venv and install the appropriate modules

    `bash ./setup.sh`

- For pRBS nodes: Start ssh-agent if it's not running, and add your key/cert:

    `eval "$(ssh-agent -s)" && ssh-add ~/path/to/id_file_and_cert`

- Run the utility

    `python3 netconf-util.py -d node-ip \[-u user\] \[-p password\] \[--rcs\]`


Only host is mandatory, other options have some sane defaults. Run `python3 netconf-util.py --help` for some info.