"""
Campbell's Soup Can #3058
Produced: 2026-03-31 12:00:31
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

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"
BOLD = "\033[1m"

def typewriter(text: str, delay: float = 0.04) -> None:
    """Print text character by character with a small delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline at end

def print_boxed(content: str, border_color: str = CYAN, fill_color: str = WHITE) -> None:
    """Print content inside a colored box."""
    lines = content.split("\n")
    max_len = max(len(line) for line in lines)
    top_bottom = border_color + "+" + "-" * (max_len + 2) + "+" + RESET
    print(top_bottom)
    for line in lines:
        padded = line.ljust(max_len)
        print(f"{border_color}| {fill_color}{padded}{border_color} |{RESET}")
    print(top_bottom)

def main() -> None:
    # Woody Allen‑style quote (original)
    quote = (
        "I'm not afraid of dying; I just don't want to be there when it happens.\n"
        "If only my therapist would stop charging me for existential crises,\n"
        "I could finally afford a sense of purpose."
    )

    # Simple ASCII neurotic face
    face = r"""
      (\_/)
      ( •ᴥ•)
      / >🍃\
    """
    # Combine face and quote for display
    display = face + "\n" + quote

    # Animated typing effect with color    typewriter(BOLD + MAGENTA + "Here’s a Woody Allen‑style nugget of wisdom:" + RESET, 0.03)
    time.sleep(0.2)
    print_boxed(display, border_color=YELLOW, fill_color=CYAN)

if __name__ == "__main__":
    main()