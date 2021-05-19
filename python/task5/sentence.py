"""Module contains sentence iterator"""
import re
from typing import List


class SentenceIterator:
    """
    Class with iterator implementation
    """

    def __init__(self, words: List[str]):
        self._words = words
        self._counter = 0
        self._length = len(words)

    def __iter__(self):
        return self

    def __next__(self):
        while self._counter < self._length:
            self._counter += 1
            return self._words[self._counter - 1]
        raise StopIteration


class Sentence:
    """
    Contains functions that can be used as string holder that yields word
    one by one
    """

    punctuation = ".!?"

    r_punctuation = r"|\.|\!|\?"
    r_not_alpha = r"\W+"

    punctuation_pattern = re.compile(r_punctuation)
    other_chars_pattern = re.compile(r_not_alpha)

    def __init__(self, sentence: str):
        self.check_type(sentence)
        self.check_punctuation(sentence)

        self._sentence = sentence
        self.chars_count = self.set_chars_count()
        self.other_count = len(self._sentence) - self.chars_count

    def check_type(self, sentence):
        """
        Checks if given sentence is string
        :param sentence: Given sentence to test
        :return: None
        """
        if not isinstance(sentence, str):
            raise TypeError(f"Was given {type(sentence)}, str required instead")

    def check_punctuation(self, sentence):
        """
        Checks if given sentence ended with punctuation chars
        :param sentence: Given sentence to test
        :return: None
        """
        if sentence[-1] not in self.punctuation:
            raise ValueError(f"Sentence should be completed with '.!?',"
                             f" got {sentence[-1]} instead")

    def set_chars_count(self) -> int:
        """
        Counts latin chars in sentence
        :return: Number of latin chars
        :rtype: int
        """
        words_count = 0
        for char in self._sentence:
            if str.isalpha(char):
                words_count += 1
        return words_count

    def del_other_chars(self) -> str:
        """
        Delete from sentence punctuation chars
        :return: Formatted string
        :rtype: str
        """
        return self.punctuation_pattern.sub("", self._sentence)

    def _words(self):
        for word in self._sentence.split():
            yield self.punctuation_pattern.sub("", word)

    @property
    def words(self) -> List[str]:
        """
        Returns list of words in the sentence
        :return: List of words
        :rtype: List[str]
        """
        return self.punctuation_pattern.sub("", self._sentence).split()

    @property
    def other_chars(self) -> List[str]:
        """
        Returns all chars that are not latin(from understanding in regex of r\\W
         pattern)
        :return: Non-latin chars in the sentence
        :rtype: List[str]
        """
        return self.other_chars_pattern.findall(self._sentence)

    def __repr__(self):
        return f"<Sentence(words={self.chars_count}, " \
               f"other_chars={self.other_count})>"

    def __getitem__(self, item):
        """Delegates basic behavior of list.__getitem__ logic"""
        if isinstance(item, int):
            return self.del_other_chars().split()[item]

        if isinstance(item, slice):
            return self.del_other_chars().split()[item]

    def __iter__(self):
        """Returns SentenceIterator instance"""
        return SentenceIterator(self.words)
