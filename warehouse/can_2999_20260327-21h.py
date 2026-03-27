"""
Campbell's Soup Can #2999
Produced: 2026-03-27 21:51:04
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
importsys

# ANSI color codes
COLORS = {
    'reset': '\033[0m',
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'bright_black': '\033[90m',
    'bright_red': '\033[91m',
    'bright_green': '\033[92m',
    'bright_yellow': '\033[93m',
    'bright_blue': '\033[94m',
    'bright_magenta': '\033[95m',
    'bright_cyan': '\033[96m',
    'bright_white': '\033[97m',
}

def typewriter_print(text, color=COLORS['white'], delay=0.03):
    """Print text character by character with a given color."""
    for ch in text:
        sys.stdout.write(color + ch + COLORS['reset'])
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the whole string

def main():
    # Clear screen and move cursor to home    print("\033[2J\033[H", end='')

    # Woody Allen‑style quote (original)
    quote_lines = [
        "I spend my life searching for meaning,",
        "but the only thing I find is that the meaning",
        "is hidden in the fine print of my user agreement."
    ]

    # Determine box width
    max_len = max(len(line) for line in quote_lines)
    padding = 2
    inner_width = max_len + 2 * padding
    horiz = '+' + '-' * inner_width + '+'
    empty = '|' + ' ' * inner_width + '|'

    # Choose colors
    box_color = COLORS['bright_cyan']
    text_color = COLORS['bright_yellow']

    # Print top border with typewriter effect
    typewriter_print(horiz, box_color, delay=0.005)

    # Print empty line above quote
    typewriter_print(empty, box_color, delay=0.005)

    # Print each quote line inside the box
    for line in quote_lines:
        formatted = '|  ' + line.ljust(max_len) + '  |'
        typewriter_print(formatted, text_color, delay=0.04)

    # Print empty line below quote
    typewriter_print(empty, box_color, delay=0.005)

    # Print bottom border
    typewriter_print(horiz, box_color, delay=0.005)

    # Optional: a small Woody Allen‑style ASCII face
    face = r"""
      (\_/)
      ( •_•)
      / >🌭
    """
    # Print face with a slight delay for fun
    for ch in face:
        sys.stdout.write(COLORS['bright_magenta'] + ch + COLORS['reset'])
        sys.stdout.flush()
        time.sleep(0.005)
    print()  # final newline

if __name__ == "__main__":
    main()