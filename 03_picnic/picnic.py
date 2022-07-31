#!/usr/bin/env python3
"""
Author : k2 <k2@localhost>
Date   : 2022-06-18
Purpose: Rock the Casbah
"""
"""nargs=+"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true',)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item
    flag_arg = args.sorted
    items = sorted(items) if flag_arg else items
    if len(items) == 1:
        words = ''.join(items)
    elif len(items) == 2:
        items[-1] = 'and ' + items[-1]
        words = ' '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        words = ', '.join(items)

    print(f' You are bringing {words}.')

# --------------------------------------------------
if __name__ == '__main__':
    main()
