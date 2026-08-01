"""
Campbell's Soup Can #4399
Produced: 2026-08-01 15:19:23
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def slow_print(text, delay=0.02, color=Colors.YELLOW):
    for char in text:
        if char != '\n':
            sys.stdout.write(color + char + Colors.RESET)
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def animated_dots(count=3):
    sys.stdout.write(" ")
    sys.stdout.flush()
    for _ in range(count):
        sys.stdout.write(Colors.YELLOW + "." + Colors.RESET)
        sys.stdout.flush()
        time.sleep(0.4)
    sys.stdout.write("\n")

clear_screen()

# Dramatic ASCII art entrance
print(Colors.MAGENTA + Colors.BOLD)
art = r"""
              ┌─────────────────────────┐
              │        ╭────╮          │
              │      ┌┘    └┐         │
              │    ┌─┘      └─┐       │
              │  ╭─┴─◔        ◔─┴╮    │
              │  │              │    │
              │  │   ╭─────╮    │    │
              │  │   │     │   │    │
              │  ╰───┼─────┼───╯    │
              │      ╰─────╯        │
              │      Woody Allen     │
              │      (Probably)     │
              └─────────────────────────┘
"""
print(art)

time.sleep(1.5)
animated_dots()

time.sleep(0.5)

# Draw decorative frame
box_width = 74
print(Colors.CYAN + Colors.BOLD)
print("╔" + "═" * box_width + "╗")

# Quote content
quote_lines = [
    "  After my death, I'd rather have people wonder why I'm",
    "  not still living, rather than question the meaning of life.",
    "  I mean, I barely finished paying off my existentialist",
    "  therapist, and now I have to worry about the universe's",
    "  therapy bills too? It's one crisis after another!",
    "",
    "  Plus, I got this existential dread on sale at Macy's,",
    "  and the return policy is terrible!"
]

print(Colors.YELLOW + Colors.BOLD + "║")
for line in quote_lines:
    if line:
        slow_print(line, 0.015, Colors.YELLOW)
    else:
        sys.stdout.write(Colors.YELLOW + "║\n" + Colors.RESET)

print(Colors.CYAN + "║")

# Attribution
attr_lines = [
    "  - Some guy who definitely Googled 'how to sound deep'",
    "    five minutes ago and immediately forgot everything"
]
for line in attr_lines:
    slow_print(line, 0.02, Colors.MAGENTA)

print(Colors.CYAN + "╚" + "═" * box_width + "╝")

time.sleep(0.8)

# Existential footer
print(Colors.DIM)
print("""
    │
    │   [Existential Crisis #42: Now serving with extra guac of dread]
    │   [Side effects may include: pondering, sighing, more questioning]
    │
    ╰───── "But hey, at least the guacamole was good, right?" ─────╯
""")

print(Colors.RESET)

# Final blinking existential thought
colors_list = [Colors.RED, Colors.MAGENTA, Colors.YELLOW]
for i in range(3):
    color = colors_list[i % len(colors_list)]
    sys.stdout.write(color + Colors.BOLD + "\r    P.S. - None of this matters, but thanks for reading!    " + Colors.RESET)
    sys.stdout.flush()
    time.sleep(0.7)

print()

# Tiny philosophical mic drop
print(Colors.CYAN + Colors.BOLD + "\n    ┌───────────────────┐")
print("    │   ┌───┐   ┌───┐  │")
print("    │   │   │   │   │  │")
print("    │   └───┘   └───┘  │")
print("    │     PHILOSOPHY   │")
print("    └───────────────────┘" + Colors.RESET)

print()