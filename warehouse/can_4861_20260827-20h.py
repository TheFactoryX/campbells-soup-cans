"""
Campbell's Soup Can #4861
Produced: 2026-08-27 20:30:50
Worker: Ling 3.0 Flash Fin (free) (inclusionai/ling-3.0-flash-fin:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""A neurotic philosophical revelation, Woody Allen style."""

import time
import sys
import random

# ─── ANSI Colors ───────────────────────────────────────────────
RED     = '\033[91m'
GREEN   = '\033[92m'
YELLOW  = '\033[93m'
BLUE    = '\033[94m'
MAGENTA = '\033[95m'
CYAN    = '\033[96m'
WHITE   = '\033[97m'
BOLD    = '\033[1m'
DIM     = '\033[2m'
RESET   = '\033[0m'
UNDERLINE = '\033[4m'

# ─── Helpers ───────────────────────────────────────────────────
def clear():
    print('\033c', end='')

def flash(msg, color=YELLOW, delay=0.08):
    """Type out text one character at a time."""
    for ch in msg:
        sys.stdout.write(f'{color}{ch}{RESET}')
        sys.stdout.flush()
        time.sleep(delay)
    print()

def burst(text, color=WHITE):
    """Print with random sparkle characters around it."""
    sparks = ['✦','✧','·','⋅','⋆','─','╌','╍','─']
    for ch in text:
        sys.stdout.write(f'{color}{ch}{RESET}')
        sys.stdout.flush()
        time.sleep(0.04)
    print()

def color_rand():
    return random.choice([RED,YELLOW,CYAN,MAGENTA,GREEN,BLUE,WHITE])

# ─── ASCII Art: A neurotic Woody-style head ────────────────────
def draw_head():
    colors = [RED, YELLOW, CYAN, MAGENTA, GREEN]
    frames = [
f"""{colors[0]}
{c[0]}             ╔═══════════════╗{colors[0]}
{c[0]}             ║  █████████  ║{colors[0]}
{c[0]}             ║ ████████████ ║{colors[0]}
{c[0]}             ║███▓▓▓▓▓███{colors[0]}
{c[0]}             ║███{colors[0]}{colors[1]}¿{colors[0]}{colors[2]}¿{colors[0]}███{colors[0]}
{c[0]}             ║ ████████████ ║{colors[0]}
{c[0]}             ║  █████████  ║{colors[0]}
{c[0]}             ╚═══════════════╝{colors[0]}
{c[0]}              ┌──┐    ┌──┐{colors[0]}
{c[0]}              │o o│    │o o│{colors[0]}
{c[0]}              │ ><│ >  < │{colors[0]}
{c[0]}              └┬──┘    └┬─┘{colors[0]}
{c[0]}               │ ▔▔▔▔▔ │{colors[0]}
{c[0]}               └───────┘{colors[0]}
""",
f"""{colors[1]}
{c[1]}             ╔═══════════════╗{colors[1]}
{c[1]}             ║  █████████  ║{colors[1]}
{c[1]}             ║ ████████████ ║{colors[1]}
{c[1]}             ║███▓▓▓▓▓███{colors[1]}
{c[1]}             ║███{colors[1]}{colors[2]}¿{colors[1]}{colors[3]}¿{colors[1]}███{colors[1]}
{c[1]}             ║ ████████████ ║{colors[1]}
{c[1]}             ║  █████████  ║{colors[1]}
{c[1]}             ╚═══════════════╝{colors[1]}
{c[1]}              ┌──┐    ┌──┐{colors[1]}
{c[1]}              │o o│    │o o│{colors[1]}
{c[1]}              │ ><│ >  < │{colors[1]}
{c[1]}              └┬──┘    └┬─┘{colors[1]}
{c[1]}               │ ▔▔▔▔▔ │{colors[1]}
{c[1]}               └───────┘{colors[1]}
""",
f"""{colors[2]}
{c[2]}             ╔═══════════════╗{colors[2]}
{c[2]}             ║  █████████  ║{colors[2]}
{c[2]}             ║ ████████████ ║{colors[2]}
{c[2]}             ║███▓▓▓▓▓███{colors[2]}
{c[2]}             ║███{colors[2]}{colors[3]}¿{colors[2]}{colors[4]}¿{colors[2]}███{colors[2]}
{c[2]}             ║ ████████████ ║{colors[2]}
{c[2]}             ║  █████████  ║{colors[2]}
{c[2]}             ╚═══════════════╝{colors[2]}
{c[2]}              ┌──┐    ┌──┐{colors[2]}
{c[2]}              │o o│    │o o│{colors[2]}
{c[2]}              │ ><│ >  < │{colors[2]}
{c[2]}              └┬──┘    └┬─┘{colors[2]}
{c[2]}               │ ▔▔▔▔▔ │{colors[2]}
{c[2]}               └───────┘{colors[2]}
""",
    ]
    for frame in frames:
        print(frame)
        time.sleep(0.25)
        clear_screen_below()
    print(colors[3] + """
              ┌───────────────────┐
              │  ─────────────  │
              │  ████████████  │
              │  ███▄ ▄███  │
              │  ─────────────  │
              └───────────────────┘
    """)
    time.sleep(0.5)

def clear_screen_below():
    """Move cursor up to redraw the head animation."""
    sys.stdout.write('\033[18A')
    sys.stdout.flush()

# ─── The Quote ─────────────────────────────────────────────────
def reveal_quote():
    quote = (
        "I contain multitudes of neuroses,\n"
        "each one convinced it is the only one.\n"
        "The universe is vast, indifferent, and\n"
        "absurd — much like my last relationship.\n"
        "\n"
        "I don't want to live forever;\n"
        "I just want to live long enough\n"
        "to figure out what I'm doing here.\n"
        "And I'm pretty sure the answer is: worrying."
    )
    colors_for_line = [RED, YELLOW, CYAN, MAGENTA, GREEN, BLUE, WHITE, RED]
    lines = quote.split('\n')
    for i, line in enumerate(lines):
        if line == '':
            print()
            time.sleep(0.2)
            continue
        color = colors_for_line[i % len(colors_for_line)]
        flash(line + '\n', color, delay=0.045)
        time.sleep(0.15)

# ─── The Author Card ───────────────────────────────────────────
def reveal_author():
    time.sleep(0.3)
    print()
    print(f"{BOLD}{CYAN}                    ── {DIM}·  ·  ·{RESET}{CYAN} ──{RESET}")
    burst("         — Woody Allen (sort of) —", MAGENTA)
    print(f"{BOLD}{CYAN}                    ── {DIM}·  ·  ·{RESET}{CYAN} ──{RESET}")
    time.sleep(0.5)

# ─── Closing flourish ──────────────────────────────────────────
def closing():
    time.sleep(0.5)
    symbols = ['✧','·','✦','⋅','⋆','─','╌']
    for _ in range(3):
        line = ''.join(random.choice(symbols) for _ in range(30))
        print(f"{DIM}{random.choice([RED,YELLOW,CYAN,MAGENTA])}{line}{RESET}")
        time.sleep(0.1)
    print()
    print(f"{BOLD}{YELLOW}    The question isn't whether life{RESET}"
          f"{RED}{BOLD} matters{RESET}{YELLOW} — it's whether you"
          f"{BLUE}{BOLD} stopped{RESET}{YELLOW} worrying long enough to"
          f"{GREEN}{BOLD} notice{RESET}{YELLOW}.{RESET}")
    print()
    print(f"{DIM}{'─'*50}{RESET}")
    print(f"{DIM}    Press Enter to exit...{RESET}", end='', flush=True)
    input()

# ─── Main ──────────────────────────────────────────────────────
def main():
    clear()
    print()
    print(f"{BOLD}{YELLOW}         ::  A Neurotic Awakening  ::{RESET}")
    print()
    time.sleep(0.5)
    draw_head()
    time.sleep(0.3)
    reveal_quote()
    reveal_author()
    closing()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}Good. At least something responded.{RESET}")
        sys.exit(0)