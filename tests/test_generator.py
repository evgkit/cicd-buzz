import unittest

from buzz import generator


def test_sample_single_word():
    list_of_words = ('foo', 'bar', 'foobar')
    word = generator.sample(list_of_words)
    assert word in list_of_words


def test_sample_multiple_words():
    list_of_words = ('foo', 'bar', 'foobar')
    words = generator.sample(list_of_words, 2)
    assert len(words) == 2
    assert words[0] in list_of_words
    assert words[1] in list_of_words
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
