#!/usr/bin/env python3
"""
Author : k2 <k2@localhost>
Date   : 2022-06-20
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input Text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.text

    jumper = {'1':'9', '2':'8', '3':'7', 
            '4':'6', '5':'0', '6':'4', 
            '7':'3', '8':'2', '9':'1', '0':'5'}

    capture = ''
    for char in str_arg:
        capture += jumper.get(char) if char in jumper.keys() else char

    print(capture)


# --------------------------------------------------
if __name__ == '__main__':
    main()
