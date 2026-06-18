"""
Campbell's Soup Can #3958
Produced: 2026-06-18 17:29:22
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny theatrical script that prints a single Woody‑Allen‑style
philosophical quip, complete with colors and a faint typewriter
animation.  No external packages are required – only the standard
library.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour definitions (bright & dim)
# ----------------------------------------------------------------------
RESET   = "\033[0m"
BRIGHT  = "\033[1m"
DIM     = "\033[2m"
FG_CYAN = "\033[36m"
FG_MAG  = "\033[35m"
FG_YEL  = "\033[33m"
FG_WHITE= "\033[37m"

# ----------------------------------------------------------------------
# The quote – feel free to replace it with any neurotic, self‑deprecating line
# ----------------------------------------------------------------------
quote = (
    f"{BRIGHT}{FG_CYAN}“{RESET}"
    f"{DIM}{FG_WHITE}I think, therefore I’m "
    f"{FG_YEL}anxious{RESET}{DIM}{FG_WHITE} about the fact that "
    f"{FG_MAG}I’m not even sure{RESET}{DIM}{FG_WHITE} if I’m "
    f"{FG_CYAN}thinking{RESET}{DIM}{FG_WHITE} at all…{RESET}"
    f"{BRIGHT}{FG_CYAN}”{RESET}"
)

# ----------------------------------------------------------------------
# Helper: typewriter animation (prints one char at a time)
# ----------------------------------------------------------------------
def typewriter(text: str, delay: float = 0.04) -> None:
    """Print `text` with a classic typewriter effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        # Slightly longer pause after punctuation for drama
        if ch in ".!?…":
            time.sleep(delay * 8)
        else:
            time.sleep(delay)
    sys.stdout.write("\n")

# ----------------------------------------------------------------------
# Fancy border – a simple double‑line box using Unicode
# ----------------------------------------------------------------------
def boxed(text: str) -> str:
    lines = text.splitlines()
    width = max(len(it) for it in lines)
    top    = f"╔{'═' * (width + 2)}╗"
    bottom = f"╚{'═' * (width + 2)}╝"
    middle = "\n".join(f"║ {line.ljust(width)} ║" for line in lines)
    return f"{top}\n{middle}\n{bottom}"

# ----------------------------------------------------------------------
# Main routine
# ----------------------------------------------------------------------
def main() -> None:
    # Build the final visual: a boxed, colour‑rich quote
    visual = boxed(quote)

    # Fade‑in effect: print each line with a tiny pause
    for line in visual.splitlines():
        print(line)
        time.sleep(0.12)

    # Add a brief pause before the typewriter reveal
    time.sleep(0.6)
    print("\n" + DIM + "…and then the universe sighs:" + RESET + "\n")
    time.sleep(0.4)

    # Reveal the quote with animation
    typewriter(quote, delay=0.03)

    # End with a soft fade‑out (clear line and exit)
    time.sleep(0.8)
    print("\n" + DIM + "(Press Ctrl‑C to quit)" + RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)