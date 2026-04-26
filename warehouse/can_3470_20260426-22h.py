"""
Campbell's Soup Can #3470
Produced: 2026-04-26 22:59:22
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A tiny, self‑contained Python show that delivers a single Woody‑Allen‑style
philosophical quip in a splash of color and a dash of animation.
"""

import sys
import time
import itertools

# ANSI escape sequences for colors and styles
RESET   = "\033[0m"
BOLD    = "\033[1m"
ITALIC  = "\033[3m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
CYAN    = "\033[36m"
MAGENTA = "\033[35m"

# The quote – neurotic, self‑deprecating, existential
QUOTE = ("I’m not a hilarious existentialist; I just keep asking “Why am I here, "
         "and if I’m angry, why is it already 4 a.m. and I’ve only made two cocktails?”")

# Frame drawing -------------------------------------------------------------
def draw_boxed(text: str, width: int = 70) -> str:
    """Return a centered, boxed string."""
    border = f"{CYAN}{'+' + '-' * (width - 2) + '+'}{RESET}\n"
    wrapped = [text[i:i+width-4] for i in range(0, len(text), width-4)]
    body = ""
    for line in wrapped:
        body += f"{CYAN}|{RESET} {BOLD}{line:<{width-4}}{RESET}\n"
    return border + body + border

# Spinner animation ----------------------------------------------------------
def spin_message(msg: str, duration: float = 3.0, delay: float = 0.1):
    spinner = itertools.cycle(['◐', '◑', '◒', '◓', '◔', '◕', '◖', '◗'])
    end_time = time.time() + duration
    sys.stdout.write(ITALIC + YELLOW)  # set style
    while time.time() < end_time:
        spin = next(spinner)
        sys.stdout.write(f"\r{MAGENTA}{spin} {msg}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\r" + " " * (len(msg)+3) + "\r")  # clear line
    sys.stdout.flush()
    sys.stdout.write(RESET)

# Main -------------------------------------------------------------
def main():
    header = f"{BOLD}{RED}=== Wo<:{len(QUOTE)}>: The Eternal Question{RESET}"
    print(header, flush=True)
    spin_message("Contemplating the absurdity of existence...", 4, 0.08)
    print(draw_boxed(QUOTE))
    spin_message("A philosophical chuckle to boot,", 2, 0.1)
    print(f"{BOLD}{GREEN}— The Eternal & the Very Uncertain Crew{RESET}")

if __name__ == "__main__":
    main()
