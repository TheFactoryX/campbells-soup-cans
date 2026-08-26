"""
Campbell's Soup Can #4849
Produced: 2026-08-26 07:08:42
Worker: MiniMax: MiniMax M3 (free) (minimax/minimax-m3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os
import shutil

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
BLINK = "\033[5m"
REVERSE = "\033[7m"

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GRAY = "\033[90m"
ORANGE = "\033[38;5;208m"
PINK = "\033[38;5;205m"
TEAL = "\033[38;5;51m"
PURPLE = "\033[38;5;141m"
GOLD = "\033[38;5;220m"
SKY = "\033[38;5;117m"

# Background colors
BG_DARK = "\033[48;5;235m"
BG_PURPLE = "\033[48;5;53m"
BG_TEAL = "\033[48;5;23m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def slow_print(text, delay=0.04, color=None, end="\n"):
    """Print text with a typewriter effect."""
    for char in text:
        if color:
            sys.stdout.write(f"{color}{char}{RESET}")
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()


def type_quote_line(line, color, delay=0.045, indent="   "):
    """Type out a single line of a quote with given color."""
    sys.stdout.write(indent)
    for char in line:
        if char == " ":
            sys.stdout.write(" ")
        else:
            sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()


def rgb_cycle_text(text, cycles=1):
    """Display text with a rainbow color cycle effect."""
    width = shutil.get_terminal_size().columns
    for cycle in range(cycles):
        for i, char in enumerate(text):
            if char == " ":
                sys.stdout.write(" ")
            else:
                color_code = 196 + (i + cycle * 7) % 36  # 196..231 spread
                if color_code > 231:
                    color_code = 21 + (color_code - 231) % 16
                sys.stdout.write(f"\033[38;5;{color_code}m{char}{RESET}")
            sys.stdout.flush()
            time.sleep(0.012)


def thinking_dots(count=3, delay=0.4):
    """Animated thinking dots."""
    for i in range(count):
        for frame in [".  ", ".. ", "..."]:
            sys.stdout.write(f"\r   {GRAY}Woody is thinking{frame}{RESET}  ")
            sys.stdout.flush()
            time.sleep(delay)
    sys.stdout.write("\r" + " " * 40 + "\r")


def draw_box(width, height, title=""):
    """Draw a decorative box."""
    top = "╔" + "═" * (width - 2) + "╗"
    bottom = "╚" + "═" * (width - 2) + "╝"
    print(f"   {GOLD}{top}{RESET}")
    if title:
        title_line = "║" + title.center(width - 2) + "║"
        print(f"   {GOLD}{title_line}{RESET}")
        sep = "╠" + "═" * (width - 2) + "╣"
        print(f"   {GOLD}{sep}{RESET}")
    for _ in range(height):
        middle = "║" + " " * (width - 2) + "║"
        print(f"   {GOLD}{middle}{RESET}")
    print(f"   {GOLD}{bottom}{RESET}")


def animated_quote():
    """Type the philosophical quote inside a fancy box."""
    quote = [
        ("\"I don't know the meaning of life,", ORANGE),
        (" but maybe the search for meaning", YELLOW),
        (" is just my brain's way of avoiding", SKY),
        (" the fact that I left the oven on.\"", PINK),
    ]
    width = 60
    print(f"   {GOLD}╔{'═' * (width - 2)}╗{RESET}")
    top_pad = f"║{' ' * (width - 2)}║"
    print(f"   {GOLD}{top_pad}{RESET}")

    for line, color in quote:
        sys.stdout.write(f"   {GOLD}║{RESET}")
        # leading spaces inside box
        inner_pad = (width - 2 - len(line)) // 2
        sys.stdout.write(" " * inner_pad)
        for ch in line:
            if ch == " ":
                sys.stdout.write(" ")
            else:
                sys.stdout.write(f"{BOLD}{color}{ch}{RESET}")
            sys.stdout.flush()
            time.sleep(0.035)
        # trailing spaces
        trailing = width - 2 - inner_pad - len(line)
        sys.stdout.write(" " * trailing)
        sys.stdout.write(f"{GOLD}║{RESET}\n")

    print(f"   {GOLD}║{' ' * (width - 2)}║{RESET}")
    print(f"   {GOLD}╚{'═' * (width - 2)}╝{RESET}")


def floating_skull():
    """A little animated floating skull for that existential dread vibe."""
    skull = r"""
          .ed$$$e.
        .e$$$$$$$$e.
       $$$$$$$$$$$$$
      $$$$$$P""Y$$$$
      $$$$$P    `$$$
      `$$$P     `Y$$
       `Y$P      `Y$
        `$b       `$b
         `Y.       `Y.
          `$.       `$.
"""

    lines = skull.split("\n")
    colors = [GRAY, DIM + GRAY, RESET, DIM + WHITE, WHITE, DIM + CYAN, CYAN, BLUE, MAGENTA, RED, ORANGE, YELLOW]
    print()
    for i, line in enumerate(lines):
        c = colors[i % len(colors)]
        print(f"      {c}{line}{RESET}")


def brain_emoji_ascii():
    """An ASCII brain thinking really hard."""
    brain = r"""
       ,-----.
     .'       '.
    /  .---.  _\
   |  /  A  \  |
   |  \  ?  /  |
    \  '---'  /
     '.       .'
       '-----'
"""
    for i, line in enumerate(brain.split("\n")):
        if i % 2 == 0:
            print(f"      {PINK}{line}{RESET}")
        else:
            print(f"      {PURPLE}{line}{RESET}")


def gradient_quote(quote_text):
    """Print a quote with gradient color effect."""
    # Pre-compute the gradient
    colors_256 = [196, 202, 208, 214, 220, 226, 190, 154, 118, 82, 46]
    n = len(colors_256)
    centered_indent = " " * ((shutil.get_terminal_size().columns - 70) // 2)
    sys.stdout.write(centered_indent)
    for i, char in enumerate(quote_text):
        if char == "\n":
            sys.stdout.write("\n" + centered_indent)
            continue
        c = colors_256[i % n]
        sys.stdout.write(f"{BOLD}\033[38;5;{c}m{char}{RESET}")
        sys.stdout.flush()
        time.sleep(0.03)
    print()


def main():
    clear()
    width = shutil.get_terminal_size().columns

    # Header
    print()
    header_lines = [
        f"{GOLD}✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦{RESET}",
        f"{GOLD}┃{RESET}        {ITALIC}{WHITE}PROFUNDITY  BY  ACCIDENT{RESET}        {GOLD}┃{RESET}",
        f"{GOLD}✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦{RESET}",
    ]
    for line in header_lines:
        print(line.center(width))

    # Floating skull intro
    time.sleep(0.3)
    print()
    floating_skull()

    # Brain thinking
    time.sleep(0.4)
    brain_emoji_ascii()

    # Thinking animation
    print()
    thinking_dots(2, 0.25)

    # The Quote
    print()
    animated_quote()

    # Signature
    print()
    time.sleep(0.4)
    sig = "— Woody Allen (probably, while eating a knish)"
    sys.stdout.write(" " * ((width - len(sig)) // 2))
    for ch in sig:
        if ch == " ":
            sys.stdout.write(" ")
        else:
            sys.stdout.write(f"{ITALIC}{TEAL}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(0.025)
    print()

    # Closing flourish
    print()
    time.sleep(0.3)
    flourish = f"   {GRAY}~ {DIM}the universe is under no obligation to make sense to anyone{RESET}"
    print(flourish.center(width))

    time.sleep(0.2)
    final = f"   {DIM}{GRAY}...especially not to me.{RESET}"
    print(final.center(width))

    # Animated rainbow signature line
    print()
    time.sleep(0.3)
    signature_line = "♫ ♪ ♫ ♪   t h e   e x i s t e n t i a l   b l u e s   ♪ ♫ ♪ ♫"
    rgb_cycle_text(signature_line, cycles=1)
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n   {GRAY}(the void acknowledges your hasty exit){RESET}\n")
        sys.exit(0)