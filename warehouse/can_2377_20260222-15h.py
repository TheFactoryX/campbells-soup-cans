"""
Campbell's Soup Can #2377
Produced: 2026-02-22 15:41:48
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
Woody Allen meets the terminal – one funny, neurotic philosophical quote
with colorful animation and a tiny ASCII coffee mug.
Run it and watch the quote appear, one character at a time, in random colors.
"""

import time, random, sys

# ──────────────────────────────────────────────
# Helper functions for ANSI escapes
# ──────────────────────────────────────────────
def random_fg():
    """Return an ANSI code that gives a random foreground color."""
    return f"\033[3{random.randint(1, 9)}m"

def clear_screen():
    """Clear the terminal and move the cursor to the top‑left corner."""
    print("\033[2J\033[H", end="")

def banner():
    """A short “Woody Allen” intro – title scrolling & tiny head."""
    clear_screen()

    title = "W O O D Y   A L L E N   S   Q U O T E   R   T H E   C O M P A N I S T"
    # Scroll title character by character
    for i, ch in enumerate(title):
        sys.stdout.write(random_fg() + ch + "\033[0m")
        sys.stdout.flush()
        time.sleep(0.03)               # a tiny pause for drama
    print("\n", flush=True)

    # Small ASCII silhouette of Woody (no colours, just for fun)
    silhouette = r"""
       ___
    /'___'\
   (o   o)
    /     \
   /       \
   \_______/
"""
    for line in silhouette.splitlines():
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(0.25)

def animate_quote(text):
    """Print a quote, character‑by‑character, in random colours."""
    for ch in text:
        sys.stdout.write(random_fg() + ch + "\033[0m")
        sys.stdout.flush()
        time.sleep(0.04)
    print("\n", flush=True)
    print("\033[36m— Woody Allen, Existentialist of the Ordinary —\033[0m")

def coffee_mug():
    """ASCII coffee mug with a fading background colour."""
    mug_art = r"""
     __
  ___\_/
 __( o )__
|    ^    |
|   / \   |
\___/_\___/
"""
    # start with a warm yellow background
    sys.stdout.write("\033[48;5;240m")
    for line in mug_art.splitlines():
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(0.18)
    # fade to a softer gray
    sys.stdout.write("\033[48;5;232m")
    for line in mug_art.splitlines():
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(0.18)

# ──────────────────────────────────────────────
# Main routine
# ──────────────────────────────────────────────
if __name__ == "__main__":
    # 1️⃣ Show a whimsical intro
    banner()

    # 2️⃣ The single Woody‑Allen‑style philosophical quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    animate_quote(quote)

    # 3️⃣ A little caffeine‑powered ASCII coffee mug to finish the mood
    coffee_mug()