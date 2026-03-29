"""
Campbell's Soup Can #3037
Produced: 2026-03-29 22:50:53
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sysimport time
import itertools

# ANSI color codes
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
BLUE = "\033[94m"
RESET = "\033[0m"

def spinner(duration=1.5):
    """Show a simple spinner for the given duration."""
    end = time.time() + duration
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if time.time() > end:
            break
        sys.stdout.write('\r' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r ')
    sys.stdout.flush()

def main():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    colors = [RED, YELLOW, GREEN, CYAN, MAGENTA, BLUE]
    
    # Spinner while "thinking"
    spinner()
    
    # Typewriter effect with rotating colors per word
    words = quote.split()
    for i, w in enumerate(words):
        sys.stdout.write(colors[i % len(colors)] + w + RESET + ' ')
        sys.stdout.flush()
        time.sleep(0.15)
    print()  # final newline
    
    # Simple ASCII art (a neurotic face)
    art = [
        "   _____",
        "  /     \\",
        " |  o o  |",
        " |   ^   |",
        " |  '-'  |",
        "  \\_____/"
    ]
    for line in art:
        sys.stdout.write(YELLOW + line + RESET + '\n')
        time.sleep(0.1)

if __name__ == "__main__":
    main()