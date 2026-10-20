"""
Campbell's Soup Can #5136
Produced: 2026-10-20 00:20:46
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
neurotic_wisdom.py
A Woody Allen-style existential quote with maximum visual flair.
Pure Python • No external dependencies • Guaranteed anxiety
"""

import sys
import time
import random
import os
import textwrap


class Color:
    """ANSI color codes because existential dread needs color."""

    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'

    # Standard colors
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    GRAY = '\033[90m'
    WHITE = '\033[97m'

    # Bright variants
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'

    # 256-color palette for extra neurosis
    ORANGE = '\033[38;5;214m'
    PINK = '\033[38;5;206m'
    SALMON = '\033[38;5;209m'
    GOLD = '\033[38;5;220m'
    PURPLE = '\033[38;5;128m'
    VIOLET = '\033[38;5;135m'
    TEAL = '\033[38;5;39m'

    # Truecolor for special effects
    @staticmethod
    def rgb(r, g, b):
        return f'\033[38;2;{r};{g};{b}m'

    @staticmethod
    def bg_rgb(r, g, b):
        return f'\033[48;2;{r};{g};{b}m'


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def wait(seconds):
    """Sleep with less typing."""
    time.sleep(seconds)


def rand_delay(base, variance=0.015):
    """A little random timing variation for human feel."""
    return base + random.uniform(-variance, variance)


def typewriter(text, delay=0.03, colors=None, end='\n'):
    """
    Print text with a typewriter effect.
    Optionally cycle through colors.
    """
    for i, char in enumerate(text):
        if colors and char != ' ':
            color = colors[i % len(colors)]
            sys.stdout.write(f"{color}{char}{Color.RESET}")
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        if char != ' ':
            time.sleep(rand_delay(delay, 0.012))
        else:
            time.sleep(rand_delay(delay * 0.6, 0.005))
    if end:
        print(end, end='')
        sys.stdout.flush()


def center_print(text, width=84):
    """Print text centered within a given width."""
    for line in text.split('\n'):
        if len(line) <= width:
            print(line.center(width))
        else:
            print(line)


def breathing_cursor(text, colors, cycles=20, delay=0.12):
    """
    Print text with a breathing/pulsing color effect.
    Simulates consciousness struggling against entropy.
    """
    for cycle in range(cycles):
        idx = cycle % len(colors)
        sys.stdout.write('\r')
        padding = ' ' * ((84 - len(text)) // 2)
        sys.stdout.write(f"{padding}{colors[idx]}{text}{Color.RESET}")
        sys.stdout.flush()
        wait(delay)
        # Fade effect: dimmer color
        sys.stdout.write('\r')
        dim_color = Color.DIM
        sys.stdout.write(f"{padding}{dim_color}{text}{Color.RESET}")
        sys.stdout.flush()
        wait(delay * 0.4)
    print()


def animated_thinking_dots(colors, indent=35, delay=0.38):
    """
    Animated dots that appear and disappear.
    Like a brain trying to form thoughts.
    """
    sys.stdout.write(' ' * indent)
    sys.stdout.flush()
    for _ in range(10):
        for count in range(1, 4):
            time.sleep(delay)
            dots = '.' * count
            sys.stdout.write(dots)
            sys.stdout.flush()
        # Erase
        sys.stdout.write('\b\b\b')
        sys.stdout.write('   ')
        sys.stdout.write('\b\b\b')
        sys.stdout.flush()
    print()


def print_boxed_text(typewriter_lines, box_width=72, colors=None,
                     border_top='╔', border_bottom='╚', border_side='║',
                     border_fill='═'):
    """
    Print text inside a Unicode box with typewriter effect for each line.
    """
    # Top border
    print(f"{Color.BRIGHT_CYAN}{box_width * ' '}{Color.RESET}")
    top = border_top + border_fill * (box_width - 2) + '╗'
    print(f"{Color.BRIGHT_CYAN}{top}{Color.RESET}")

    for line in typewriter_lines:
        # Left border
        sys.stdout.write(f"{Color.BRIGHT_CYAN}{border_side}{Color.RESET}")
        sys.stdout.flush()

        # Inner padding
        sys.stdout.write('  ')
        sys.stdout.flush()

        # Type the text
        typed_line = line.strip()
        for i, char in enumerate(typed_line):
            if colors:
                color = colors[i % len(colors)]
                sys.stdout.write(f"{color}{char}{Color.RESET}")
            else:
                sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(rand_delay(0.025, 0.008))

        # Right padding to fill the box
        text_len = len(typed_line)
        padding = (box_width - 4) - text_len
        if padding > 0:
            sys.stdout.write(' ' * padding)
        else:
            sys.stdout.write(' ')

        # Right border
        sys.stdout.write(f"{Color.BRIGHT_CYAN}{border_side}{Color.RESET}\n")
        sys.stdout.flush()
        wait(0.15)

    # Bottom border
    bottom = border_bottom + border_fill * (box_width - 2) + '╝'
    print(f"{Color.BRIGHT_CYAN}{bottom}{Color.RESET}")
    print(f"{Color.BRIGHT_CYAN}{box_width * ' '}{Color.RESET}")


def print_ascii_art():
    """Print a neurotic thinker ASCII art with color."""
    art_lines = [
        f"{Color.GRAY}              .-=========-.{Color.RESET}",
        f"{Color.GRAY}              \\\\\\\'-======-\\\\\\'.{Color.RESET}",
        f"{Color.GRAY}           ,====\\\\        //====,{Color.RESET}",
        f"{Color.GRAY}           \\\\\\\\        //\\\\\\\\{Color.RESET}",
        f"{Color.GRAY}            \\\\\\\\      //\\\\\\\\{Color.RESET}",
        f"{Color.GRAY}              \\\\    //{Color.RESET}",
        f"{Color.GRAY}               \\\\  //{Color.RESET}",
        f"{Color.GRAY}                \\\\/{Color.RESET}",
        f"{Color.GRAY}                 ||{Color.RESET}",
        f"{Color.GRAY}                 ||{Color.RESET}",
        f"{Color.GRAY}                _||_{Color.RESET}",
        f"{Color.GRAY}               (____){Color.RESET}",
    ]
    center_print('\n'.join(art_lines), 84)


def rainbow_cursor(text, colors, delay=0.1):
    """
    Print text where each character cycles through colors.
    Like a tiny existential rainbow.
    """
    for cycle in range(3):
        sys.stdout.write('\r')
        centered = text.center(84)
        sys.stdout.write(centered)
        sys.stdout.flush()
        for j, char in enumerate(centered):
            if char != ' ':
                color = colors[(j + cycle) % len(colors)]
                # We can't re-color already printed chars, so just pulse
        wait(delay)
    # Final colored version
    sys.stdout.write('\r')
    for i, char in enumerate(text.center(84)):
        if char != ' ':
            color = colors[i % len(colors)]
            sys.stdout.write(f"{color}{char}{Color.RESET}")
        else:
            sys.stdout.write(char)
    sys.stdout.flush()
    print()


def main():
    """Main neurotic flow."""

    # Color palettes
    neurosis_colors = [
        Color.BRIGHT_YELLOW, Color.PINK, Color.ORANGE,
        Color.GOLD, Color.SALMON, Color.BRIGHT_MAGENTA
    ]
    title_colors = [
        Color.CYAN, Color.BRIGHT_BLUE, Color.PURPLE,
        Color.VIOLET, Color.TEAL, Color.BRIGHT_CYAN
    ]
    thinking_colors = [Color.GRAY, Color.BRIGHT_MAGENTA, Color.PINK]

    clear_screen()

    print('\n')

    # --- Animated Title ---
    breathing_cursor("🧠 LOADING NEUROSIS 🧠", thinking_colors, cycles=15)

    # --- Thinking Animation ---
    print()
    animated_thinking_dots(thinking_colors, indent=35)

    # --- ASCII Art ---
    print()
    print_ascii_art()

    # --- Dramatic Pause ---
    wait(0.5)
    center_print(f"{Color.DIM}...processing existential data...{Color.RESET}", 84)
    wait(0.7)

    # --- The Quote ---
    quote = (
        "I don't believe in an afterlife—mainly because I can't even "
        "commit to finishing a Netflix series. How could I possibly commit "
        "to eternal existence? I'd probably abandon it halfway through the "
        "second millennium, leaving angels in suspense and causing "
        "cosmic-level anxiety for everyone involved. Meanwhile, I'm "
        "terrified of death, not because it's the end, but because it "
        "might be the beginning—and I already have enough beginnings "
        "I haven't properly prepared for. I'd probably show up to the "
        "afterlife in the wrong shoes, with nothing but existential dread "
        "to pay the admission fee."
    )

    # Wrap the quote
    wrapped = textwrap.wrap(quote, width=66)
    # Pad lines to even length
    max_len = max(len(line) for line in wrapped)
    padded_lines = [line.ljust(max_len) for line in wrapped]

    # Add some breathing room
    print()
    wait(0.4)

    # Print the quote in a box
    print_boxed_text(
        padded_lines,
        box_width=72,
        colors=neurosis_colors
    )

    # --- Footer ---
    wait(0.5)
    print()
    center_print(f"{Color.ITALIC}{Color.GRAY}"
                 f"— Anonymous Neurosis Engine v∞{Color.RESET}", 84)
    wait(0.3)
    print()

    # --- Pulsing End Message ---
    end_messages = [
        "Reality is optional. Sanity is overrated.",
        "You are here. There is no 'here'.",
        "Existence precedes essence—but also precedes lunch.",
        "We are all just carbon with commitment issues.",
    ]

    for msg in end_messages:
        breathing_cursor(msg, title_colors, cycles=8, delay=0.09)
        wait(0.6)

    # Final blinks
    print()
    center_print(f"{Color.BLINK}{Color.BOLD}💭{Color.RESET}", 84)
    print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print(f"\n{Color.BRIGHT_RED}"
              f"Interrupted by anxiety.{Color.RESET}")
        sys.exit(0)