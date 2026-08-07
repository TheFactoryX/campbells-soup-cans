"""
Campbell's Soup Can #4458
Produced: 2026-08-07 11:57:26
Worker: inclusionAI: Ling 3.0 Tiny (free) (inclusionai/ling-3.0-tiny:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen — Philosophical Quote Generator with Visual Flair"""

import time
import sys
import os

# ── ANSI Color Codes ──────────────────────────────────────────────
RED       = '\033[91m'
GREEN     = '\033[92m'
YELLOW    = '\033[93m'
BLUE      = '\033[94m'
MAGENTA   = '\033[95m'
CYAN      = '\033[96m'
WHITE     = '\033[97m'
BOLD      = '\033[1m'
RESET     = '\033[0m'
DIM       = '\033[2m'
UNDERLINE = '\033[4m'
REVERSE   = '\033[7m'
BG_RED    = '\033[41m'
BG_GREEN  = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE   = '\033[44m'
BG_CYAN   = '\033[46m'
BG_MAGENTA= '\033[45m'
BG_WHITE  = '\033[47m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def blink(text, color):
    """Blink the text by rapidly switching between visible and hidden"""
    for _ in range(10):
        print(color + text + RESET, end='', flush=True)
        sys.stdout.write('\033[1A')  # move cursor up
        sys.stdout.write('\033[2K')  # clear line
        time.sleep(0.12)

def slow_reveal(text, delay=0.08, color=WHITE):
    """Reveal text one character at a time with a blink cursor"""
    print(f"{color}{DIM}{BOLD}", end='', flush=True)
    for i, ch in enumerate(text):
        if i > 0 and i % 3 == 0:
            print(RESET, end='', flush=True)
            print(color + ch + RESET, end='', flush=True)
        else:
            print(color + ch + RESET, end='', flush=True)
        time.sleep(delay)
    print(RESET)

def draw_box(title, lines):
    """Draw a fancy bordered box around text"""
    w = max(len(l) for l in lines) + 6
    h = len(lines) + 4
    top = '╭' + '─' * (w - 2) + '╮'
    bot = '╰' + '─' * (w - 2) + '╯'
    sep = '│' + ' ' * (w - 2) + '│'

    print(f"{YELLOW}{BOLD}{top}{RESET}")
    for line in lines:
        print(f"{BG_CYAN}{DIM}{sep}{RESET}")
        print(f"{BG_CYAN}  {line}{RESET}")
        print(f"{BG_CYAN}{DIM}{sep}{RESET}")
    print(f"{YELLOW}{BOLD}{bot}{RESET}")
    print()

def make_ascii_face():
    """Print a cute ASCII art face with a sad/philosophical vibe"""
    face = [
        "  .---.         .---.      .-.     .-.   .---.  ,--.  ",
        "  |  ___|      /|   |    .'  .'  .'  .'  |   |  |   |   ",
        "  | |  __     / |   |   /'  /  /  /  /   |   |  |   |   ",
        "  | | |   |   |   |    /  /  /  /  /   |   |  |   |   ",
        "  | | |   |  /|   |   /  /  /  /  /  .'   |   |  |   |   ",
        "  | |___|   / |   |  /  /  /  /  /  |   |   |  |   |   ",
        "  |          / |   |  /  /  /  /  /  |   |   |  |   |   ",
        "  |        _/  |   | /  /  /  /  /   |   |   |  |   |   ",
        "  '---'    '   '---'   '  /  '   /   '---'   '---'   '  ",
    ]
    for line in face:
        print(f"{RED}{line}{RESET}")
    print()

def draw_frame(title, body, subtitle=""):
    """Draw a large, beautiful frame around a quote"""
    # Top border
    print(f"{CYAN}{'━'*50}{RESET}")
    print(f"{BOLD}{CYAN}  🎭  WOODY ALLEN PHILOSOPHICAL QUOTE  🎭{RESET}")
    print(f"{CYAN}{'━'*50}{RESET}")
    print()
    # Title
    if subtitle:
        print(f"{DIM}{subtitle}")
    # Body with decorative lines
    for line in body:
        print(f"{BLUE}  ── {line}{RESET}")
    print()
    # Bottom border
    print(f"{CYAN}{'━'*50}{RESET}")
    print()

def typewriter_quote(quote, delay=0.06, speed=3, color=GREEN):
    """Type out the quote character by character with a blinking cursor"""
    print(f"\n{BOLD}{CYAN}  ◉  The quote  ◉{RESET}")
    print()
    for i, ch in enumerate(quote):
        if i % 14 == 0 and i > 0:
            print(f"{RED}{DIM}{BOLD}", end='', flush=True)
            time.sleep(delay * 0.08)
            sys.stdout.write('\033[1A')
            sys.stdout.write('\033[2K')
            sys.stdout.write(f"{CYAN}{BOLD}{ch}{RESET}", end='', flush=True)
            sys.stdout.write('\033[1A')
            sys.stdout.write('\033[2K')
        else:
            print(f"{color}{BOLD}{ch}{RESET}", end='', flush=True)
            time.sleep(delay)
            sys.stdout.write('\033[1A')
            sys.stdout.write('\033[2K')
    print()

def main():
    clear_screen()

    # ── ASCII Face Intro ──
    make_ascii_face()
    print(f"\n{BOLD}{CYAN}  ♪  Welcome to the Woody Allen Philosophical Quote Generator  ♪{RESET}")
    print(f"{BOLD}{CYAN}  {DIM}Every 2 seconds, a new existential dilemma arrives.{RESET}")
    print(f"{BOLD}{CYAN}  {DIM}Let the madness begin...{RESET}")
    print()
    time.sleep(1.2)

    # ── Quote 1: The classic Woody Allen existential horror ──
    quote1 = (
        "I'm not afraid of death; "
        "I just don't want to be there when it happens."
    )
    draw_frame(
        title="EXISTENTIAL ANXIETY",
        body=[
            f"Life is the most painful experience in the universe.",
            f"We are all just animals pretending to have consciousness.",
            f"Every moment you are living is a moment you are dying.",
            f"The universe is vast, lonely, and full of cosmic indifference.",
        ],
        subtitle=f"{RED}Quote: {quote1}{RESET}"
    )

    # ── Typewriter reveal ──
    typewriter_quote(quote1, delay=0.04, speed=2)

    # ── Quotes 2: More Allen-style darkness ──
    print(f"\n{BOLD}{CYAN}  ♪  Second Round ♪{RESET}")
    time.sleep(0.8)

    quote2 = "I love being alone, at least a little bit. Being with people who are happy with me is too much of a luxury."
    draw_frame(
        title="SELFISH PESSIMISM",
        body=[
            f"Loneliness is not a feeling — it is a way of life.",
            f"I have this theory that people who are happy are less well-rounded. I'm less well-rounded.",
            f"Everything is a lie. Nothing is what it seems.",
        ],
        subtitle=f"{RED}Quote: {quote2}{RESET}"
    )
    typewriter_quote(quote2, delay=0.04, speed=2)

    # ── Quote 3: Absurdity ──
    time.sleep(1.2)
    print(f"\n{BOLD}{CYAN}  ♪  Third Round ♪{RESET}")
    time.sleep(0.8)

    quote3 = "I'm so neurotic that I can never stop worrying. And I do worry all the time. That's why I'm neurotic."
    draw_frame(
        title="NEUROTIC PARANOIA",
        body=[
            f"I am not a person; I am a process that goes wrong.",
            f"Being lonely is the closest you'll ever come to being happy.",
            f"In one sense I'm an optimist. In another, I'm a pessimist.",
        ],
        subtitle=f"{RED}Quote: {quote3}{RESET}"
    )
    typewriter_quote(quote3, delay=0.04, speed=2)

    # ── Closing ──
    time.sleep(1.5)
    clear_screen()

    print(f"{BOLD}{CYAN}{'═'*50}{RESET}")
    print(f"{BOLD}{MAGENTA}  ⭐  FINAL QUOTE — The Last Word  ⭐{RESET}")
    print(f"{BOLD}{CYAN}{'═'*50}{RESET}")
    print()

    final_quote = (
        f"{BOLD}{RED}{'~'*40}{RESET}\n"
        f"{RED}{BOLD}  {DIM}I'd like to thank you for your time.  I hope you found at least "
        f"{DIM}one tiny bit of truth in this philosophical journey.  I have a feeling "
        f"{DIM}the universe didn't want me to tell you this.  Good luck.  ════{RESET}\n"
        f"{BOLD}{RED}{'~'*40}{RESET}\n"
    )
    print(final_quote)
    print(f"\n{BLUE}{BOLD}  Created with {RED}existential dread, {RESET}and {YELLOW}not enough sleep.{RESET}\n")
    print(f"{CYAN}{BOLD}  ♪  End of the Program  ♪{RESET}")

if __name__ == "__main__":
    main()