from dataclasses import dataclass
from classes.Line import Line
from helpers.string2int import StringToken
from keywords import KEYWORDS, COMMENT_PREFIX


@dataclass
class Lexer:
    string_maps: list[StringToken]

    def lex(self, lines: list[Line]) -> list[Line]:
        """Lexes the lines."""

        for line in lines:
            line.text = line.text.strip()
            if line.text.startswith(COMMENT_PREFIX):
                break

            for keyword in KEYWORDS:
                if line.text.startswith(keyword):
                    line.text = line.text.replace(keyword, KEYWORDS[keyword])

            for string_token in self.string_maps:
                line.text = line.text.replace(
                    str(string_token.int_index), f'"{string_token.value}"'
                )

        return lines
