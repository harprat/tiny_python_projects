#!/usr/bin/env python3
"""Going further tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput
import test


# --------------------------------------------------
def test_article_case_consonant():
    """a Brigantine -> A Brigatine"""
    
    out = getoutput(f'{test.prg} {test.consonant_words[0]}')
    if test.consonant_words[0][0].isupper():
        assert out.strip() == test.template.format('A', test.consonant_words[0][0].upper())

# --------------------------------------------------
def test_article_case_vowel():
    """a Brigantine -> A Brigatine"""
    
    out = getoutput(f'{prg} {vowel_words[0][0]}')
    if vowel_words[0].isupper():
        assert out.strip() == template.format('An', vowel_words[0][0].upper())

# --------------------------------------------------
def test_choose_side():
    """Starboard or larboard"""
    
    template_starboard = 'Ahoy, Captain, {} {} off the starboard bow!'

    out = getoutput(f'{prg} -s Brigatine')
    assert out.strip() == template_starboard.format('A', 'Brigatine')
