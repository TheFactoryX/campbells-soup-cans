"""
Campbell's Soup Can #4559
Produced: 2026-08-12 23:01:46
Worker: inclusionAI: Ling 3.0 Tiny (free) (inclusionai/ling-3.0-tiny:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen's Philosophy Machine
===================================
A visually stunning program that displays
funny philosophical quotes in Woody Allen's style.

Requirements: Pure Python, no external dependencies.
"""

import sys
import time

# ── ANSI Color Codes ────────────────────────────────────────
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
BOLD = '\033[1m'
RESET = '\033[0m'
DIM = '\033[2m'


def typewriter(text, delay=0.015):
    """Type out text character by character."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


def draw_banner(title):
    """Draw a fancy animated banner."""
    print(f"\n{BOLD}{CYAN}")
    print("  ╔═══════════════════════════════════════════════════════╗")
    print(f"  ║  {title:^52}  ║")
    print("  ╚═══════════════════════════════════════════════════════╝")
    print(f"{RESET}")


def print_frame(text, width=52):
    """Print a thin frame around text."""
    print(f"{CYAN}")
    print(f"  ┌{'─' * (width - 2)}┐")
    print(f"  │  {text}  │")
    print(f"  └{'─' * (width - 2)}┘")
    print(f"{RESET}")


def show_quote(quote):
    """Show a quote with a nice visual treatment."""
    print(f"\n{BOLD}{CYAN}")
    print(f"  ╔{'═' * 52}╗")
    print(f"  ║  📖  {quote}  📖  ║")
    print(f"  ╚{'═' * 52}╝")
    print(f"{RESET}")


def main():
    # ── Clear ──
    sys.stdout.write("\033c")
    sys.stdout.flush()

    # ── Title ──
    print(f"\n{BOLD}{RED}")
    print("  ╔══════════════════════════════════════════════════════════════╗")
    print("  ║   🎬  W O O D Y   A L L E N   🎬                              ║")
    print("  ║   ~  The Philosophy Machine  ~                              ║")
    print("  ╚══════════════════════════════════════════════════════════════╝")
    print(f"{RESET}")

    time.sleep(0.4)

    # ── Intro ──
    print(f"\n{DIM}  {CYAN}  ~  Thinking of some things...  ~  {RESET}")
    print(f"  {DIM}  {RED}  'Reality is that thing you have to invent to make a living.'  {RESET}")
    print(f"  {DIM}  {CYAN}  'I am not a very good actor...'  {RESET}")
    print(f"  {DIM}  {YELLOW}  'I think it would be nice if people didn\'t try so hard.'  {RESET}")

    time.sleep(0.5)

    # ── Main Quote (typewriter effect) ──
    print_frame("THE MAIN QUOTE")
    print(f"\n{BOLD}{CYAN}")
    typewriter(
        "I'm not afraid of death; I just don't want to be there when it happens.",
        delay=0.015
    )
    print(f"{RESET}")

    # ── Quote with decoration ──
    print(f"\n{CYAN}")
    print(f"  {'─' * 50}")
    print(f"  {CYAN}  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ {RESET}")
    print(f"  {CYAN}  ~  {RED}✦  I don't want to achieve immortality through my work;")
    print(f"  {CYAN}  {RED}  I want to achieve it through not dying.  ✦  {RESET}")
    print(f"  {CYAN}  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ {RESET}")
    print(f"  {'─' * 50}")

    # ── More Quotes ──
    print(f"\n{BOLD}{CYAN}")
    print("  ╔═══════════════════════════════════════════════════════╗")
    print("  ║   🌿  Additional Wisdom  🌿                          ║")
    print("  ╚═══════════════════════════════════════════════════════╝")

    more_quotes = [
        f"{RED}  {DIM}  'Life is full of misery, loneliness, and suffering - and it's all over much too soon.'  {RESET}",
        f"{YELLOW}  {DIM}  'I think it would be nice if people didn't try so hard.'  {RESET}",
        f"{MAGENTA}  {DIM}  'I am not a great actor. I think I\'m just a very good actor...'  {RESET}",
    ]
    for q in more_quotes:
        print(f"  {q}")
        time.sleep(0.3)

    # ── Closing ──
    print(f"\n\n{BOLD}{CYAN}")
    print(f"  ┌{'─' * 57}┐")
    print(f"  │  {DIM}  'Reality is that thing you have to invent to make a living.'  │")
    print(f"  └{'─' * 57}┘")
    print(f"\n{BOLD}{CYAN}  ════════════════════════════════════════════════════")
    print(f"  ║  {DIM}  {CYAN}  ──  The End.  ──  {RESET}")
    print(f"  ╚═══════════════════════════════════════════════════")
    print(f"{RESET}")


if __name__ == "__main__":
    main()