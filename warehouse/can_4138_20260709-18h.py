"""
Campbell's Soup Can #4138
Produced: 2026-07-09 18:09:48
Worker: Qwen: Qwen3.5 Plus 2026-04-20 (qwen/qwen3.5-plus-20260420)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI Escape Codes
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
DIM = "\033[2m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
RESET = "\033[0m"

def main():
    # Clear terminal screen
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()
    time.sleep(0.3)

    width = 62
    top = f"╔{'═' * width}╗"
    bot = f"╚{'═' * width}╝"
    spacer = f"║{' ' * width}║"

    # Header formatting
    header_lines = [
        f"{DIM}┌{'─' * 38}┐{RESET}",
        f"{DIM}│  {CYAN}{BOLD}[ EXISTENTIAL MANUSCRIPT ]{RESET}{DIM}          │{RESET}",
        f"{DIM}│  {ITALIC}Subject: The Uncomfortable Nature of Being{RESET}{DIM}   │{RESET}",
        f"{DIM}└{'─' * 38}┘{RESET}"
    ]

    print()
    for line in header_lines:
        print(line)
    print()

    print(top)
    print(spacer)

    # The Woody Allen-style quote, split for dramatic pacing
    quote_lines = [
        f"{RED}~ {YELLOW}{ITALIC}I don’t resent the void for being empty;",
        f"  I just wish it had warned me first.",
        f"  So here we are, clapping politely",
        f"  at a play where the script is missing,",
        f"  the actors are obviously guessing,",
        f"  and I’m convinced I’m sitting in a",
        f"  seat that’s reserved for someone else."
    ]

    # Animate line-by-line reveal with neurotic timing
    for i, line in enumerate(quote_lines):
        visible_len = len(line)
        padding = (width - 4) - visible_len
        if padding < 0: padding = 0

        # Simulate a nervous typewriter cursor
        sys.stdout.write(f"║  {line}{' ' * padding} ║\r")
        sys.stdout.write(f"║  {line}{' ' * padding}{'█' if i % 2 == 0 else '╲'} ║\n")
        sys.stdout.flush()

        # Random neurotic pause for realism
        time.sleep(random.uniform(0.3, 0.5))

    print(spacer)
    print(bot)

    # Signature
    print(f"\n{DIM}  ── typed by a man who overthinks his own shadow{RESET}")
    print(f"     during a two-hour delay at LaGuardia.\n")
    print(f"{DIM}   {'_' * 56}{RESET}")

if __name__ == "__main__":
    main()