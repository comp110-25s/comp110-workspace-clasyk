"""main code for exercise 3"""

__author__: str = "730553768"

# so sorry but the minute i put a docstring i get like 20 errors and it's frightening
# i literally have to type the docstring after the hashtag and then delete the hashtag


def invert(og_dict: dict[str, str]) -> dict[str, str]:
    """will flipflop the key and value of a dict"""
    inv_dict: dict[str, str] = (
        {}
    )  # docstrings crash my thing sometimes so im gonna do this... sorry
    # this gives us a variable to easily return

    for key in og_dict:
        if og_dict[key] in inv_dict:
            raise KeyError("No duplicates allowed!")
        # check keyerror first to make sure no duplicates for new keys

        inv_dict[og_dict[key]] = key  # ensure old values are new keys

    return inv_dict


def count(count_list: list[str]) -> dict[str, int]:
    # docstrings are being scary for this im sorry
    """ " this function counts how many time a word is used"""

    idx: int = 0
    count_dict: dict[str, int] = {}  # gives us something to return

    while idx < len(count_list):
        if count_list[idx] in count_dict:
            count_dict[
                count_list[idx]
            ] += 1  # if something has a duplicate, it will note it

        else:
            count_dict[count_list[idx]] = 1  # if something is alone, the count is 1
        idx += 1

    return count_dict


def favorite_color(colors_dict: dict[str, str]) -> str:
    color_idx: dict[str, int] = {}
    current_color: str = ""
    stored_color: str = ""
    """ looks which color is said the most and returns it"""

    for key in colors_dict:
        if (
            colors_dict[key] in color_idx
        ):  # this essentially is count but for this function
            color_idx[
                colors_dict[key]
            ] += 1  # keeps tracking the number of times a color is said

        else:
            color_idx[colors_dict[key]] = 1  # only said once, count is one

    for current_color in color_idx:
        if stored_color == "":  # put empty case first for the edge case test
            stored_color = current_color
        if color_idx[current_color] > color_idx[stored_color]:
            stored_color = current_color  # makes sure the most named color stays
    return stored_color


def bin_len(og_list: list[str]) -> dict[int, set[str]]:
    """this sorts words by their length"""
    idx: int = 0
    new_dict: dict[int, set[str]] = {}  # gotta have something to fill

    while idx < len(og_list):
        key_return: int = len(og_list[idx])  # key for the new dictionary

        if key_return in new_dict:
            new_dict[key_return].add(og_list[idx])  # updates to the set
        else:
            new_dict[key_return] = {og_list[idx]}
        idx += 1

    return new_dict
