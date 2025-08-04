"""
CP1404 - Prac 10
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"
    assert car.fuel == 0, 'Car has not set fuel correctly'
    car = Car(fuel=10)
    assert car.fuel == 10, 'Car has not set fuel correctly'


run_tests()


def format_phrase_as_sentence(sentence):
    """
    format a phrase as a sentence, starting with a capital and ending with a single full stop.
    then add doctests for 3 tests:
    >>> format_phrase_as_sentence('hello')
    'Hello.'
    >>> format_phrase_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase_as_sentence('i like choclate')
    'I like choclate.'
    """
    sentence = sentence.capitalize()
    if not sentence[-1] == '.':
        sentence += '.'
    return sentence


doctest.testmod()