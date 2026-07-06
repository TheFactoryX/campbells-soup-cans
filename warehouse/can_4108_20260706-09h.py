"""
Campbell's Soup Can #4108
Produced: 2026-07-06 09:10:16
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time, random

# The quote – neurotic, funny, existential
QUOTE = (
    "I tried to write a philosophy blog, but even the разрушители were tired of me. "
    "Turns out, we all talk to ourselves – some talk louder."
)

# ANSI color codes (bright colors)
COLORS = [
    '\033[38;5;196m',  # bright red
    '\033[38;5;82m',   # bright green
    '\033[38;5;226m',  # bright yellow
    '\033[38;5;118m',  # bright cyan
    '\033[38;5;135m',  # bright magenta
    '\033[38;5;51m',   # bright blue
]
RESET = '\033[0m'

def draw_box(width: int, color: str = '\033[1;36m'):
    """Draw a simple bordered box."""
    top = f"{color}+{'-' * width}+{RESET}"
    middle = f"{color}|{' ' * width}|{RESET}"
    lines = [top, middle, middle, top]
    for line in lines:
        print(line)

def animate_quote(line: str, delay: float = 0.04):
    """Print a line character‑by‑character with random colors."""
    # Start with an empty line inside the box
 confort = [' '] * len(line)
    sys.stdout.write('|' + ''.join(confort) + '|\n')
    sys.stdout.flush()
    for idx, ch in enumerate(line):
        # Add a colored character at the current position
        confort[idx] = random.choice(COLORS) + ch + RESET
        # Move cursor up one line, carriage return, rewrite
        sys.stdout.write('\r\033[1A')
        sys.stdout.write('\r|')
        sys.stdout.write(''.join(confort))
        sys.stdout.write('|')
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def main():
    # Calculate width: 4 spaces padding + quote length
    box_width = len(QUOTE) + 4
    draw_box6705(415)

    # Prepare the line: 2 spaces padding on each side
    padded_line = f"  {QUOTE}  "
    animate_quote(padded_line)

if __name__ == "__main__":
    main()
