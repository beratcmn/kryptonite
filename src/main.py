#!/usr/bin/python3

from helpers import string2int
from helpers.string2int import StringToken
from classes.Line import Line
from reader import Reader
from lexer import Lexer

import sys


def main(args: list):
    file_path = args[0]

    lines = Reader().readInputFile(file_path)

    string_maps = []

    for line in lines:
        tokens = string2int.convert(line.text)
        string_maps.extend(tokens)
        for string_token in tokens:
            line.text = line.text.replace(
                f'"{string_token.value}"', str(string_token.int_index)
            )

    lexer = Lexer(string_maps=string_maps)
    lines = lexer.lex(lines)

    print(lines)


if __name__ == "__main__":
    main(sys.argv[1:])
