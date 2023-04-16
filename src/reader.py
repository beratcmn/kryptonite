from dataclasses import dataclass
from classes.Line import Line


@dataclass
class Reader:
    """### Class for reading the input file."""

    def readInputFile(self, filePath) -> list[Line]:
        """Reads the input file and returns a list of lines."""

        with open(filePath, "r", encoding="utf-8") as file:
            context = file.read()
            context = context.splitlines()

            lines = []
            indent_level = 0
            for line in context:
                if line.startswith("    "):
                    indent_level += 1
                    line = line[4:]
                lines.append(Line(line, indent_level))

            return lines
