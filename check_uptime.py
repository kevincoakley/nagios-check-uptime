#!/usr/bin/env python

import argparse
import sys


def get_uptime(uptime_file="/proc/uptime"):
    """
    Get uptime from /proc/uptime
    :param uptime_file: path to /proc/uptime
    :return: uptime in seconds
    """
    with open(uptime_file, "r") as f:
        uptime_seconds = float(f.readline().split()[0])
        return uptime_seconds


def parse_arguments(args):
    """
    Parse Commandline Arguments
    :param args: *args positional arguments
    :return: Commandline arguments parsed by argparse
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--min-days",
        metavar="min_days",
        dest="min_days",
        help="Alert if uptime is less than this value",
        type=int,
        default=0,
    )

    parser.add_argument(
        "--max-days",
        metavar="max_days",
        dest="max_days",
        help="Alert if uptime is greater than this value",
        type=int,
        default=365,
    )

    return parser.parse_args(args)


def main():
    """
    script main
    :return: exit code
    """
    exit_code = 0
    exit_message = "OK - No Errors"
    error_message = ""

    args = parse_arguments(sys.argv[1:])

    uptime_seconds = get_uptime()

    uptime_days = uptime_seconds / 60 / 60 / 24

    if uptime_days < args.min_days:
        exit_code = 1
        error_message = "Uptime is less than {} days".format(args.min_days)

    if uptime_days > args.max_days:
        exit_code = 1
        error_message = "Uptime is greater than {} days".format(args.max_days)

    if exit_code == 1:
        exit_message = "WARNING - %s" % error_message

    print(exit_message)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
