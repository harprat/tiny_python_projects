#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
template = 'Ahoy, Captain, {} {} off the larboard bow!'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('a', word)


# --------------------------------------------------
# def test_consonant_upper():
#     """brigantine -> a Brigatine"""

#     for word in consonant_words:
#         out = getoutput(f'{prg} {word.title()}')
#         assert out.strip() == template.format('a', word.title())


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('an', word)


# --------------------------------------------------
# def test_vowel_upper():
#     """octopus -> an Octopus"""

#     for word in vowel_words:
#         out = getoutput(f'{prg} {word.upper()}')
#         assert out.strip() == template.format('an', word.upper())

# --------------------------------------------------
# def test_article_case_consonant():
#     """a Brigantine -> A Brigatine"""
    
#     out = getoutput(f'{prg} {consonant_words[0]}')
#     if consonant_words[0][0].isupper():
#         assert out.strip() == template.format('A', consonant_words[0][0].upper())

# --------------------------------------------------
# def test_article_case_vowel():
#     """a Brigantine -> A Brigatine"""
    
#     out = getoutput(f'{prg} {vowel_words[0][0]}')
#     if vowel_words[0].isupper():
#         assert out.strip() == template.format('An', vowel_words[0][0].upper())

# --------------------------------------------------
# def test_choose_side():
#     """Starboard or larboard"""
    
#     template_starboard = 'Ahoy, Captain, {} {} off the starboard bow!'

#     out = getoutput(f'{prg} -s Brigatine')
#     assert out.strip() == template_starboard.format('A', 'Brigatine')
