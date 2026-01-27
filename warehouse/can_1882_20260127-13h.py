"""
Campbell's Soup Can #1882
Produced: 2026-01-27 13:58:19
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen's Existential Typing Machine.
A single‑file Python script that displays a neurotic,
self‑deprecating philosophical quote in vibrant ANSI colors.
"""

import time, random, os, sys

# ANSI foreground colour codes – we'll pick randomly from here.
FG = {
    'red':    '31',
    'green':  '32',
    'yellow': '33',
    'blue':   '34',
    'magenta':'35',
    'cyan':   '36',
    'white':  '37',
}


def color(text: str, fg: str = 'white') -> str:
    """Return text wrapped with an ANSI colour escape code."""
    return f"\033[{FG[fg]}m{text}\033[0m"


def clear_screen() -> None:
    """Clear the terminal using ANSI sequences."""
    print("\033[2J\033[H", end='')


def print_header() -> None:
    """Show a tiny ASCII portrait of Woody Allen (very stylised)."""
    woody = r"""
      ___
     ( o o )
      | ^ |
     /     \\
    (       )
    """
    for line in woody.splitlines():
        time.sleep(0.15)
        print(color(line, random.choice(list(FG.values()))))
    print()  # give a little breathing space


def animate_typing(text: str) -> None:
    """
    Print the quote one character at a time, each character in a random colour.
    The growing text is centred inside a box that widens with each new char.
    """
    border_width = 70                # big enough for any quote + padding
    border = "+" + "-" * border_width + "+"
    max_len = len(text)

    for idx in range(max_len):
        displayed = text[: idx + 1]
        pad = " " * (border_width - len(displayed))
        line = f"|{displayed}{pad}|"

        clear_screen()
        print(border)
        print(color(line, random.choice(list(FG.values()))))
        print(border)
        sys.stdout.flush()
        time.sleep(0.04)            # “typing” speed


def rainbow_words(quote: str) -> str:
    """Return the quote where every word is coloured randomly."""
    words = quote.split()
    coloured = [color(w, random.choice(list(FG.values()))) for w in words]
    return " ".join(coloured)


def final_box(quote: str) -> None:
    """Print a nicely coloured box with the quote already fully rendered."""
    border_width = 70
    border = "+" + "-" * border_width + "+"
    padded = quote.center(border_width)

    print(border)
    print(color(padded, random.choice(list(FG.values()))))
    print(border)


def blinking_cursor() -> None:
    """A tiny “typing‑cursor” animation after the quote."""
    cursor = color('>', 'white')
    for _ in range(15):
        print("\r", end='')                # return to start of line
        print(cursor, end='')
        time.sleep(0.4)
        print("\r", end='')                # hide
        time.sleep(0.4)


def main() -> None:
    # 1️⃣ Header – Woody’s silhouette
    print_header()

    # 2️⃣ Typing animation – the chosen philosophical punch‑line
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    animate_typing(quote)

    # 3️⃣ Final static box – each word in a different colour
    final_box(rainbow_words(quote))

    # 4️⃣ End with a blinking cursor – because even Woody can’t finish without a final punctuation
    blinking_cursor()


if __name__ == "__main__":
    main()