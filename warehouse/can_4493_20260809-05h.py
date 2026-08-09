"""
Campbell's Soup Can #4493
Produced: 2026-08-09 05:57:40
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color helpers
def fg_color(code: int) -> str:
    """Return ANSI escape for 256‑foreground color."""
    return f"\033[38;5;{code}m"

def reset() -> str:
    return "\033[0m"

def rainbow_cycle(length: int):
    """Yield rainbow colors repeatedly."""
    rainbow = [196, 202, 226, 82, 33, 129]  # red‑orange‑yellow‑green‑blue‑magenta
    i = 0
    while True:
        yield rainbow[i % len(rainbow)]
        i += 1

def animated_print(text: str, delay: float = 0.008):
    """Print text char‑by‑char with a tiny delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def main():
    # Clear screen and move cursor home
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    quote = ("I’m not afraid of death; I just wish it had better customer service. "
             "If the afterlife had a help desk, I’d probably be put on hold forever.")
    # Add a little padding
    inner = f" {quote} "
    width = len(inner) + 2  # for side borders

    # Build rainbow top/bottom borders
    color_gen = rainbow_cycle(width)
    top_border = "".join(fg_color(next(color_gen)) + "-" for _ in range(width - 2))
    bottom_border = "".join(fg_color(next(color_gen)) + "-" for _ in range(width - 2))

    top_line = "+" + top_border + reset() + "+"
    bottom_line = "+" + bottom_border + reset() + "+"
    middle_line = "|" + fg_color(255) + inner + reset() + "|"

    # Animated output
    animated_print(top_line, delay=0.001)
    time.sleep(0.1)
    animated_print(middle_line, delay=0.001)
    time.sleep(0.1)
    animated_print(bottom_line, delay=0.001)

    # Optional final pause before exit
    time.sleep(1.5)

if __name__ == "__main__":
    main()