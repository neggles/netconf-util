#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Andrew Powers-Holmes"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import RbsNetconf


def main(args):
    """ Main entry point of the app """
    if args.verbose > 0:
        print(args)
        pass

    # Override port to 2022 for RCS
    if args.rcs:
        args.port = 2022

    nodeInstance = RbsNetconf.Node(host=str(args.hostname),
                                   username=str(args.username),
                                   port=int(args.port),
                                   password=str(args.password),
                                   keyfile=str(args.sshkey),
                                   device_params=None,
                                   hostkey_verify=False,
                                   look_for_keys=args.look_for_keys,
                                   allow_agent=args.allow_agent)

    # do get-config action
    if args.action == 'get-config':
        try:
            config = nodeInstance.get_config()
            print("Config retrieved")
            with open(str(args.outfile + '.xml'), "w") as f:
                print("Saving config data to %s.xml" % str(args.outfile))
                f.write(config.data_xml)

            with open(str(args.outfile + '_raw.xml'), "w") as f:
                print("Saving raw response to %s_raw.xml" % str(args.outfile))
                f.write(config._raw)

            if args.verbose >= 3:
                with open(str(args.outfile + '_debug.xml'), "w") as f:
                    print("Saving debug dump to %s_debug.xml" % str(args.outfile))
                    f.write(str(vars(config)))
            pass
        except:
            print("Something went wrong, sorry...")
            pass


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser(
        description="basic netconf client scripts for ericsson RBSes",
        epilog=
        "Currently supported actions are 'get-config' and 'set-config' because this is very new."
    )

    parser.add_argument("-d", "--host", required=True, dest="hostname")

    parser.add_argument("-u", "--user", default="oam", dest="username")

    parser.add_argument("-p", "--password")

    parser.add_argument("-a",
                        "--action",
                        default="get-config",
                        help="netconf action to execute")

    parser.add_argument("-P",
                        "--port",
                        default=830,
                        type=int,
                        help="SSH port for netconf xml-rpc")

    parser.add_argument("-s", "--sshkey", help="SSH private key path")

    parser.add_argument("-n",
                        "--no-agent",
                        action="store_false",
                        dest="allow_agent",
                        default=True,
                        help="Do not use ssh-agent to authenticate")

    parser.add_argument("-k",
                        "--no-user-keys",
                        action="store_false",
                        dest="look_for_keys",
                        default=True,
                        help="Do not look for keys in ~/.ssh/")

    parser.add_argument("-i",
                        "--infile",
                        default="config-in",
                        help="Path to input file for set-config")

    parser.add_argument("-o",
                        "--outfile",
                        default="config-out",
                        help="Path to output file for get-config")

    parser.add_argument("-r",
                        "--rcs",
                        action="store_true",
                        default=False,
                        help="Convenient way to override port to 2022")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument("-v",
                        "--verbose",
                        action="count",
                        default=0,
                        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
