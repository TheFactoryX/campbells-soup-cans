"""
Campbell's Soup Can #1406
Produced: 2026-01-05 11:32:34
Worker: Qwen: Qwen3 Coder 480B A35B (free) (qwen/qwen3-coder:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def type_writer(text, delay=0.05):
    """Simulate typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_with_border(text, border_char='~'):
    """Print text with a wavy border"""
    border = border_char * (len(text) + 4)
    print(f"\033[38;5;141m{border}\033[0m")
    print(f"\033[38;5;141m{border_char}\033[0m \033[1;37m{text}\033[0m \033[38;5;141m{border_char}\033[0m")
    print(f"\033[38;5;141m{border}\033[0m")

def print_neurotic_quote():
    """Display a Woody Allen-style quote with flair"""
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Title animation
    title = "WOODY ALLEN'S EXISTENTIAL WISDOM"
    print("\033[1;33m")
    type_writer(" " * 10 + title, 0.03)
    print("\033[0m")
    
    # Draw a neurotic brain
    brain = [
        "        ████████████████████████████████████████████████████",
        "      ██                                                  ██",
        "    ██    ██████  ██    ██  ██████  ██    ██  ██████      ██",
        "   ██    ██    ██ ███   ██ ██       ███   ██ ██    ██      ██",
        "  ██     ██    ██ ████  ██ ██       ████  ██ ██             ██",
        "  ██     ██    ██ ██ ██ ██ ██       ██ ██ ██  ██████        ██",
        "  ██     ██    ██ ██  ████ ██       ██  ████       ██       ██",
        "   ██    ██    ██ ██   ███ ██    ██ ██   ███ ██    ██      ██",
        "    ██    ██████  ██    ██  ██████  ██    ██  ██████      ██",
        "      ██                                                  ██",
        "        ████████████████████████████████████████████████████"
    ]
    
    print("\033[1;35m")
    for line in brain:
        print(" " * 8 + line)
        time.sleep(0.1)
    print("\033[0m")
    
    # Quote with dramatic pause
    print("\n" + " " * 15 + "\033[3mThinking...\033[0m")
    time.sleep(1.5)
    
    # The quote
    quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."
    author = "— Woody Allen (probably)"
    
    # Colorful display
    print("\n\033[1;36m" + " " * 12 + "┌" + "─" * 60 + "┐\033[0m")
    print("\033[1;36m" + " " * 12 + "│\033[0m" + " " * 60 + "\033[1;36m│\033[0m")
    
    # Split quote into lines
    words = quote.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line + " " + word) <= 58:
            current_line += " " + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    for i, line in enumerate(lines):
        padding = (58 - len(line)) // 2
        print("\033[1;36m" + " " * 12 + "│\033[0m" + " " * (padding + 1) + "\033[1;37m" + line + "\033[0m" + " " * (59 - padding - len(line)) + "\033[1;36m│\033[0m")
    
    print("\033[1;36m" + " " * 12 + "│\033[0m" + " " * 60 + "\033[1;36m│\033[0m")
    print("\033[1;36m" + " " * 12 + "│\033[0m" + " " * 40 + "\033[3;32m" + author + "\033[0m" + " " * (19 - len(author)) + "\033[1;36m│\033[0m")
    print("\033[1;36m" + " " * 12 + "└" + "─" * 60 + "┘\033[0m")
    
    # Anxious heartbeat
    print("\n" + " " * 25 + "\033[5;31m❤\033[0m" + " " * 2 + "\033[38;5;240m(erratically)\033[0m")
    
    # Neurotic postscript
    ps = "P.S. But if I do die, I hope it's in my sleep like my grandfather... not screaming in terror like the passengers in his car."
    print("\n\033[3;33m" + " " * 15 + ps + "\033[0m")

if __name__ == "__main__":
    print_neurotic_quote()