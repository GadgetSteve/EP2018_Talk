#!/usr/bin/env python
#encoding:utf-8
"""
  Author:  Steve Barnes --<gadgetsteve@hotmail.com>
  Purpose: Demo for Europython 2018
  Created: 25/07/2018
"""
import argparse

def parse_arguments():
    """ This parses any supplied arguements."""
    parser = argparse.ArgumentParser(
        prog="EP2018_demo1", usage=None,
        description="Demonstation CLI Program",
        epilog=None,
        add_help=True)
    parser.add_argument("infile", help="One or More Input Files", nargs='+',
                        action='append', type=argparse.FileType('r'))
    parser.add_argument("--reverse", '-r', help="Do things backwards",
                        action="store_true")
    parser.add_argument('--detail', '-l', help='Select the level of detail',
                        type=int, default=3)
    opts = parser.parse_args()
    return opts

def main():
    """ Called on standalone execution."""
    opts = parse_arguments()
    for name, val in opts.__dict__.items():
        print(name, val)

if __name__ == '__main__':
    print("EP2018 Demo1 Started")
    main()
