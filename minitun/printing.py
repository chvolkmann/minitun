from typing import Final

from rich.console import Console

console: Final = Console()
print = console.print


def debug(msg: str) -> None:
    print(msg, style="debug")


def info(msg: str) -> None:
    print(msg, style="warn")


def success(msg: str) -> None:
    print(msg, style="success")


def warn(msg: str) -> None:
    print(msg, style="warn")


def error(msg: str) -> None:
    print(msg, style="error")
