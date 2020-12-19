#!/usr/bin/env python3
import sys
import os
import warnings
from ncclient import manager
warnings.simplefilter("ignore", DeprecationWarning)


class Node:

    _device_params_fixed = {'name': 'ericsson', 'with_ns': False}

    def __init__(self,
                 host,
                 port,
                 username,
                 password=None,
                 keyfile=None,
                 device_params=None,
                 hostkey_verify=False,
                 look_for_keys=True,
                 allow_agent=True):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._keyfile = keyfile
        self._device_params = device_params
        self._hostkey_verify = hostkey_verify
        self._look_for_keys = look_for_keys
        self._allow_agent = allow_agent

    def enable_nc_prefix(self):
        self._device_params.update({'with_ns': True})

    def disable_nc_prefix(self):
        self._device_params.update({'with_ns': False})

    def connect(self):
        # if instance was passed device_params
        if self._device_params is not None:
            # copy them
            device_params = self._device_params.copy()
            # and force overwrite with fixed ones from the class
            device_params.update(Node._device_params_fixed)
        else:
            # otherwise just use the name
            device_params = Node._device_params_fixed

        # instantiate an ncclient manager object
        return manager.connect(host=self._host,
                               port=self._port,
                               username=self._username,
                               password=self._password,
                               device_params=device_params,
                               hostkey_verify=self._hostkey_verify,
                               look_for_keys=self._look_for_keys,
                               allow_agent=self._allow_agent)

    def get_config(self):
        with self.connect() as mgr:
            ret = mgr.get_config(source="running")
            return ret
