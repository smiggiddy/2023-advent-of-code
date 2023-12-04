#!/usr/bin/env python
import click
import logging
import logging.handlers
import re
from pathlib import Path
from typing import List


def red(text: str) -> str:
    return f"\033[91m{text}\033[00m"


def green(text: str) -> str:
    return f"\033[92m{text}\033[00m"


def gray(text: str) -> str:
    return f"\033[97m{text}\033[00m"


def get_logger(verbosity: int = 4) -> logging.Logger:
    """Create a logger, or return an existing one with specified verbosity."""
    logger = logging.getLogger("aoc23")
    logger.setLevel(logging.DEBUG)

    if len(logger.handlers) == 0:
        _format = "{asctime} {name} [{levelname:^9s}]: {message}"
        formatter = logging.Formatter(_format, style="{")

        stderr = logging.StreamHandler()
        stderr.setFormatter(formatter)
        if verbosity is not None:
            stderr.setLevel(40 - (min(3, verbosity) * 10))
        else:
            stderr.setLevel(40)
        logger.addHandler(stderr)

        if Path("/dev/log").exists():
            syslog = logging.handlers.SysLogHandler(address="/dev/log")
            syslog.setFormatter(formatter)
            syslog.setLevel(logging.INFO)
            logger.addHandler(syslog)
    else:
        if verbosity is not None:
            stderr = logger.handlers[0]
            stderr.setLevel(40 - (min(3, verbosity) * 10))

    return logger


logger = get_logger()


class SchematicNumber:
    def __init__(self, num: str, row: int, start: int, part: bool = False) -> None:
        self.num: int = int(num)
        self.row: int = row
        self.start: int = start
        self.end: int = start + len(num)
        self.part: bool = part

    def __repr__(self) -> str:
        return f'SchematicNumber(num="{self.num}", row={self.row}, start={self.start})'

    def adjacent_to(self, sym: "SchematicSymbol") -> bool:
        possible_rows = (self.row - 1, self.row, self.row + 1)
        possible_cols = tuple(range(self.start - 1, self.end + 1))
        if sym.row in possible_rows and sym.col in possible_cols:
            return True
        return False

    def __add__(self, other) -> int:
        if isinstance(other, SchematicNumber):
            return self.num + other.num
        elif isinstance(other, int):
            return self.num + other
        else:
            raise NotImplementedError

    def __radd__(self, other) -> int:
        if isinstance(other, SchematicNumber):
            return self.num + other.num
        elif isinstance(other, int):
            return self.num + other
        else:
            raise NotImplementedError


class SchematicSymbol:
    def __init__(self, symbol: str, row: int, col: int) -> None:
        self.symbol = symbol
        self.row: int = row
        self.col: int = col

    def __repr__(self) -> str:
        return (
            f'SchematicSymbol(symbol="{self.symbol}", row={self.row}, col={self.col})'
        )


class SchematicRow:
    NUM_RE = re.compile(r"[0-9]+")
    SYM_RE = re.compile(r"[^0-9.]")

    def __init__(self, rowtext: str, row: int) -> None:
        self.data: str = rowtext
        self.row: int = row
        self.nums: List[SchematicNumber] = []
        self.syms: List[SchematicSymbol] = []

        for m in re.finditer(self.NUM_RE, rowtext):
            self.nums.append(SchematicNumber(m.group(0), row, m.start()))
        for m in re.finditer(self.SYM_RE, rowtext):
            sym = SchematicSymbol(m.group(0), row, m.start())
            self.syms.append(sym)

    def __repr__(self) -> str:
        return f'SchematicRow(rowtext="{self.data}", row={self.row})'

    @property
    def parts(self) -> List[SchematicNumber]:
        return [num for num in self.nums if num.part]


class Schematic:
    def __init__(self, file: Path) -> None:
        self.path = file
        self.rows: List[SchematicRow] = []

        with open(file) as f:
            for i, row in enumerate(f.readlines()):
                if len(row.strip()) > 0:
                    self.rows.append(SchematicRow(row.strip(), i))

        self._enumerate_parts()

    @property
    def nums(self) -> List[SchematicNumber]:
        ret = []
        for row in self.rows:
            ret.extend(row.nums)
        return ret

    @property
    def parts(self) -> List[SchematicNumber]:
        return [num for num in self.nums if num.part]

    @property
    def syms(self) -> List[SchematicSymbol]:
        ret = []
        for row in self.rows:
            ret.extend(row.syms)
        return ret

    def __str__(self) -> str:
        text = [list(row.data) for row in self.rows]
        for num in self.nums:
            for i, c in enumerate(str(num.num)):
                if num.part:
                    text[num.row][num.start + i] = green(c)
                else:
                    text[num.row][num.start + i] = red(c)
        return "\n".join(["".join(row) for row in text])

    def _enumerate_parts(self) -> None:
        for i, row in enumerate(self.rows):
            for symrow in self.rows[max(i - 1, 0) : min(i + 2, len(self.rows))]:
                for sym in symrow.syms:
                    for num in row.nums:
                        if num.adjacent_to(sym) and not num.part:
                            logger.debug(f"{num} is a part (adjacent to {sym})")
                            num.part = True

    @property
    def partssum(self) -> int:
        return sum(self.parts)


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.argument(
    "file",
    type=click.Path(dir_okay=False, readable=True, path_type=Path),
)
@click.option(
    "-d",
    "--draw",
    is_flag=True,
    help="Map the input to the part/non-part numbers visually",
)
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Increase verbosity (specify multiple times for more)",
)
def cli(file, draw, verbose):
    global logger
    logger = get_logger(verbose)
    schematic = Schematic(file=file)
    if draw:
        print(str(schematic))
    print(schematic.partssum)


if __name__ == "__main__":
    cli()
