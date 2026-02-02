"""
Campbell's Soup Can #2001
Produced: 2026-02-02 11:07:08
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import os, sys, time, random

# ANSI color codes (foreground)
COLOR = {
    30: "black", 31: "red", 32: "green", 33: "yellow",
    34: "blue", 35: "magenta", 36: "cyan", 37: "white"
}

def reset():
    return "\033[0m"

def fg(code):
    return f"\033[{code}m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Woody‑Allen‑style ASCII art (stylized “W”)
WOODY_ART = r"""
      ___   ___
 ___/   \___/   \___
/                \
|   (   )   (   )   |
|    \ /    \ /    |
 \   (____) (____) /
"""

# The quote (one piece, broken into logical lines)
QUOTE = (
    "I'm not afraid of death; I just don't want to be there when it happens,"
    "—so I'll have my notebook handy"
    "to record what I'm missing while sitting on the curb"
    "worrying about the cosmic‑tofu connection."
)

# -------------------------------------------------
# Helper to type text character‑by‑character with color changes
# -------------------------------------------------
def type_with_colors(text, delay=0.04, colour_codes=[31,32,33,34,35,36,37]):
    """Print each character of *text* in a random foreground colour."""
    for ch in text:
        sys.stdout.write(fg(random.choice(colour_codes)) + ch + reset())
        sys.stdout.flush()
        time.sleep(delay)

# -------------------------------------------------
# Main visual routine
# -------------------------------------------------
def main():
    # Start with a fresh screen
    clear()

    # Show a random‑colored Woody art
    sys.stdout.write(fg(random.choice(list(COLOR.values()))) + WOODY_ART + reset() + "\n")
    sys.stdout.flush()
    time.sleep(1)

    # Arrow “—>” indicating the quote follows
    type_with_colors("—> ", delay=TYPING_DELAY)
    TYPING_DELAY = 0.04

    # Print the quote line by line, each line with its own typing animation
    for line in QUOTE.split("\n"):                     # the split respects existing new‑lines
        type_with_colors(line + "\n", delay=TYPING_DELAY)

    # A quick pause before the cheeky wink
    time.sleep(TYPING_DELAY * 0.5)

    # Blink an ellipsis (…)
    for _ in range(5):
        for attr in (0, 5):                         # 0 = normal, 5 = blink
            sys.stdout.write(fg(random.choice(list(COLOR.values()))) + "…" + reset())
            sys.stdout.flush()
            time.sleep(BLINK_TIME)
        time.sleep(0.1)

    # Dim final thought
    sys.stdout.write(fg(30) + "Maybe we all just need a little more caffeine." + reset() + "\n")
    sys.stdout.flush()
    time.sleep(2)

if __name__ == "__main__":
    main()