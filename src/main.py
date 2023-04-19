#!/usr/bin/python3

from helpers import string2int
from helpers.string2int import StringToken
from classes.Line import Line
from reader import Reader

import sys


def main(args: list):
    file_path = args[0]

    lines = Reader().readInputFile(file_path)
    string_tokens = []

    for line in lines:
        tokens = string2int.convert(line.text)
        string_tokens.extend(tokens)
        for string_token in tokens:
            line.text = line.text.replace(
                f'"{string_token.value}"', str(string_token.int_index)
            )


if __name__ == "__main__":
    main(sys.argv[1:])
