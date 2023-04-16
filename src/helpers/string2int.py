#!/usr/bin/env python3

import re
import random
from dataclasses import dataclass


@dataclass
class StringToken:
    value: str
    int_index: int


def convert(text: str) -> list[StringToken]:
    """Converts a string to an integer.

    Args:
        string (str): The string to convert.

    Returns:
        int: The converted integer.
    """

    tokens = []

    matches = re.findall('"([^"]*)"', text)
    if len(matches) == 0:
        return []
    else:
        for match in matches:
            tokens.append(StringToken(match, random.randint(100_000_000, 999_999_999)))

    return tokens
