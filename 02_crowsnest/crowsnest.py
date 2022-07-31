#!/usr/bin/env python3
"""
Author : k2 <k2@localhost>
Date   : 2022-06-18
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')
    parser.add_argument('-s',
                        '--starboard',
                        help='Choose a starboard side',
                        action='store_true')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    side = args.starboard

    if word[0].isupper():
        article = 'An' if word[0] in 'AIUEO' else 'A'
    else:
        article = 'an' if word[0] in 'aiueo' else 'a'
    


    if side:
        print(f'Ahoy, Captain, {article} {word} off the starboard bow!')
    else:
        print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
