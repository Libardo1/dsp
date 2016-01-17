# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.


def donuts(count):
 	if count < 10:
 		print('number of donuts: ',count)
 	else:
 		print('number of donuts: many')
donuts(count)

def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

def both_ends(s):
    first_two = s[:2]
    last_two = s[-2:]
    if len(s) > 2:
        print(first_two+last_two)
    elif len(s) == 2:
        print(first_two)
    else:
        print("")
both_ends('splkjslgkj')

def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

def fix_start(s):
    first_char = s[0]
    mod = s[1:].replace(first_char,"*")
    print((first_char + mod))

fix_start('badabingbadaboom')


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.
    
def mix_up(a, b):
    first_word = a[:2]
    second_word = b[:2]
    print((second_word + a[2:]), (first_word + b[2:]))

mix_up("nothing", "better")

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

def verbing(s):
    stri = s[-3:]
    if stri == "ing":
        print(s + "ly")
    elif len(s) >= 3:
        print(s + "ing")
    elif len(s) < 3:
        print(s)
verbing("")


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

import re
def not_bad(s):
    nt = s.index('not')
    bad = s.index('bad')
    if nt < bad:
        s = s.replace("not","")
        s = s.replace("bad", "good")
    elif Valueerror:
        print(s)
    print(s)
not_bad("it's not bad")


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
