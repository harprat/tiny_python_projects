#!/usr/bin/env python3
"""
Author : k2 <k2@localhost>
Date   : 2022-07-02
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='A positional argument')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    # parser.add_argument('-i',
    #                     '--int',
    #                     help='A named integer argument',
    #                     metavar='int',
    #                     type=int,
    #                     default=0)

    # parser.add_argument('-f',
    #                     '--file',
    #                     help='A readable file',
    #                     metavar='FILE',
    #                     type=argparse.FileType('rt'),
    #                     default=None)

    # parser.add_argument('-o',
    #                     '--on',
    #                     help='A boolean flag',
    #                     action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.text
    if os.path.isfile(pos_arg):
        in_fh = open(pos_arg).read()
        uppercase = in_fh.upper()
    else:
        uppercase = pos_arg.upper()

    strip = uppercase.rstrip()    
    
     
    if args.outfile:
        file_arg = args.outfile
        file = os.path.dirname(os.path.realpath(__file__)) + '/' + file_arg
        out_fh = open(file, 'wt')
        out_fh.write(uppercase)
        out_fh.close()
    else:
        print(strip)

    

# --------------------------------------------------
if __name__ == '__main__':
    main()
