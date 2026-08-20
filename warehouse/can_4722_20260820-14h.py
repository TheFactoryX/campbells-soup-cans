"""
Campbell's Soup Can #4722
Produced: 2026-08-20 14:54:39
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen meets terminal — a neurotic philosophical quote, beautifully boxed."""
import time

QUOTE = "I'm not afraid of death. I'm just afraid of being there when it happens, "
QUOTE += "feeling awkward, wondering if the afterlife has Wi-Fi, and whether "
QUOTE += "my therapist is already there taking notes."

RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
BOLD = "\033[1m"


def boxed(text, width=68, color=CYAN):
    """Print text inside a colored ASCII box using ANSI escape codes."""
    width = max(width, len(text) + 4)
    top = color + "┏" + "━" * (width - 2) + "┓" + RESET
    bottom = color + "┗" + "━" * (width - 2) + "┛" + RESET
    print(top)
    pad = width - 2 - len(text)
    left = pad // 2
    right = pad - left
    print(color + "┃" + RESET + " " * left + text + " " * right + color + "┃" + RESET)
    print(bottom)


def main():
    # Playful header fade
    print(GREEN + BOLD + "         ⊂( ◕‿◕)つ Woody's Wisdom" + RESET)
    time.sleep(0.4)
    boxed(QUOTE, 72, CYAN)


if __name__ == "__main__":
    main()