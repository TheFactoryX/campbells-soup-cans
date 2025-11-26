"""
Campbell's Soup Can #529
Produced: 2025-11-26 07:30:58
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import shutil

# ANSI color codes
RESET   = '\033[0m'
CYN     = '\033[36m'
YEL     = '\033[33m'
BOLD    = '\033[1m'
DIM     = '\033[2m'

# Quote (Woody‑Allen style)
QUOTE = "I think I'm the only person who can make myself feel miserable for no reason at all."

# Helper for typewriter effect
def typewriter(text, color=YEL, delay=0.05):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)

# Build the box around the quote
def build_box(lines, border_color=CYN):
    max_len = max(len(line) for line in lines)
    top = border_color + '┌' + '─' * (max_len + 2) + '┐' + RESET
    bottom = border_color + '└' + '─' * (max_len + 2) + '┘' + RESET
    boxed = [top]
    for line in lines:
        padded = line.ljust(max_len)
        boxed.append(f"{border_color}│ {RESET}{padded}{border_color} │{RESET}")
    boxed.append(bottom)
    return boxed

# Create ASCII art header (optional)
def header_art():
    art = [
        BOLD + YEL + "       __      __ ",
        BOLD + YEL + " __ _|  \\__/  |__",
        BOLD + YEL + "|  (_)      (_)  ",
        "                      "]
    return art

# Main function
def main():
    # Clear screen and hide cursor
    sys.stdout.write('\033[2J\033[H\033[?25l')
    sys.stdout.flush()

    art_lines = header_art()
    box_lines = [quote_line for quote_line in [QUOTE]]
    box = build_box(box_lines)

    # Combine art and box
    content = art_lines + [''] + box

    # Get terminal width to center content
    term_width = shutil.get_terminal_size((80, 20)).columns

    for line in content:
        padded = line.center(term_width)
        if line.strip().startswith('I think'):
            # Typewriter effect for quote line
            sys.stdout.write(padded[:len(padded)//2] + RESET)  # print space before
            sys.stdout.flush()
            typewriter(QUOTE, color=YEL, delay=0.05)
            sys.stdout.write(padded[len(padded)//2 + len(QUOTE):] + RESET + '\n')
        else:
            sys.stdout.write(padded + RESET + '\n')
        sys.stdout.flush()
        time.sleep(0.07)

    # Show cursor again
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()

if __name__ == "__main__":
    main()