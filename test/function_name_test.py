#encoding: utf-8

from nose.tools import *
import sys
sys.path.append('../lib')

from letter_counter import count_letters

@raises(TypeError)
def test_takes_a_string_as_argument():
    count_letters()
    count_letters(1337)

def test_should_return_dictionary():
    assert_true(isinstance(count_letters("hello"), dict))

def test_should_return_a_hash_containing_correct_letters_and_counts():
    hello = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    mississippi = {'i': 4, 'p': 2, 's': 4, 'm': 1}

    assert_equal(count_letters("hello"), hello)

    assert_equal(count_letters("mississippi"), mississippi)

def test_should_count_upper_and_lowercase_lowercase():
    hello = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    mississippi = {'i': 4, 'p': 2, 's': 4, 'm': 1}

    assert_equal(count_letters("heLLo"), hello)
    assert_equal(count_letters("miSsissiPpi"), mississippi)

def test_should_only_count_letters():

    sentence = {'a': 10, 'c': 1, 'm': 2, 'l': 2, 'n': 4, 'p': 2}
    assert_equal(count_letters("A man a plan a canal Panama"), sentence)





