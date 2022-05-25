import re


def delete(string_):
    pattern = re.compile(r"\([^()]+\)")
    new_string = re.sub(pattern, "", string_)
    return new_string

