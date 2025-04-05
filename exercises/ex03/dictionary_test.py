"""test codes for ex03"""

__author__: str = "730553768"

import pytest


from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import bin_len

with pytest.raises(KeyError):
    my_dictionary = {"kris": "jordan", "michael": "jordan"}
    invert(my_dictionary)

"""testing invert"""


def test_invert_empty() -> None:
    assert invert({}) == {}


def test_invert_long_use() -> None:
    assert invert({"a": "b", "c": "d", "e": "f"}) == {"b": "a", "d": "c", "f": "e"}


def test_invert_simple_use() -> None:
    assert invert({"a": "b"}) == {"b": "a"}


"""testing count"""


def test_count_edge() -> None:
    assert count([]) == {}


def test_count_use_simple() -> None:
    assert count(["hello", "hi"]) == {"hello": 1, "hi": 1}


def test_count_us_complicated() -> None:
    assert count(
        ["hello", "hi", "howdy", "hi", "howdy", "heythere", "hey", "hallo"]
    ) == {"hello": 1, "hi": 2, "howdy": 2, "heythere": 1, "hey": 1, "hallo": 1}


"""testing favorite color"""


def test_favorite_color_edge() -> None:
    assert favorite_color({}) == ""


def test_favorite_color_tie() -> None:
    assert favorite_color({"claire":"blue", "yomama": "pink}) == "blue"

def test_favorite_color_use_simple() -> None:
    assert favorite_color({"claire": "blue"}) == "blue"


"""testing bin length"""


def test_bin_edge() -> None:
    assert bin_len([]) == {}


def test_bin_simple_use() -> None:
    assert bin_len(["aaa", "bbbb"]) == {3: {"aaa"}, 4: {"bbbb"}}


def test_bin_complicated_use() -> None:
    assert bin_len(["aaa", "bbb", "cccc", "ddddd"]) == {
        3: {"aaa", "bbb"},
        4: {"cccc"},
        5: {"ddddd"},
    }