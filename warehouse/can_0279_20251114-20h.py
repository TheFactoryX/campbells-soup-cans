"""
Campbell's Soup Can #279
Produced: 2025-11-14 20:33:57
Worker: OpenAI: gpt-oss-120b (openai/gpt-oss-120b)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import os
import ctypes

# ---- Enable ANSI colors on Windows -------------------------------------------------
def _enable_ansi_windows() -> None:
    if os.name != "nt":
        return
    kernel32 = ctypes.windll.kernel32
    hStdOut = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE = -11
    mode = ctypes.c_ulong()
    if kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode)):
        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
        kernel32.SetConsoleMode(hStdOut, mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)

_enable_ansi_windows()
# ------------------------------------------------------------------------------------

# ANSI color codes
C = {
    "reset": "\033[0m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bright_black": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",
}


def typewriter(text: str, delay: float = 0.02) -> None:
    """Print text character‑by‑character like a typewriter."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


def framed_quote(quote: str, author: str = "Woody Allen") -> list[str]:
    """Return the quote wrapped in a colorful ASCII frame."""
    lines = quote.split("\n")
    max_len = max(len(line) for line in lines)
    width = max_len + 6  # padding

    top = f"{C['bright_cyan']}╔{'═' * width}╗{C['reset']}"
    bottom = f"{C['bright_cyan']}╚{'═' * width}╝{C['reset']}"
    framed = [top]
    for line in lines:
        padded = f"  {line.ljust(max_len)}  "
        framed.append(f"{C['bright_cyan']}║{C['reset']}{C['bright_yellow']}{padded}{C['reset']}{C['bright_cyan']}║{C['reset']}")
    # author line
    author_line = f"— {author}"
    padded = f"{author_line.rjust(width)}"
    framed.append(f"{C['bright_cyan']}║{C['reset']}{C['bright_green']}{padded}{C['reset']}{C['bright_cyan']}║{C['reset']}")
    framed.append(bottom)
    return framed


def main() -> None:
    # ---- The Woody‑Allen‑style philosophical gem ---------------------------------
    quote = (
        "I’m not afraid of death; I just don’t want to be there when it happens.\n"
        "And if I’m honest, I’m also terrified of the waiting room."
    )
    # ------------------------------------------------------------------------------

    art = framed_quote(quote, "Woody Allen")
    for line in art:
        typewriter(line, delay=0.005)
        time.sleep(0.03)   # tiny pause between lines

    # A final wink
    wink = f"{C['bright_magenta']}¯\\_(ツ)_/¯{C['reset']}"
    typewriter("\n" + wink, delay=0.07)


if __name__ == "__main__":
    main()