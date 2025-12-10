"""
Campbell's Soup Can #850
Produced: 2025-12-10 23:30:24
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import random

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'

# ASCII art of Woody Allen glasses for visual interest
glasses = [
    "            ╔═════╗     ╔═════╗",
    "            ║     ║     ║     ║",
    "            ║ ╔═══╣     ╠═══╗ ║",
    "            ║ ║         ║ ║ ║ ║",
    "            ║ ║         ║ ║ ║ ║",
    "            ║ ║         ║ ║ ║ ║",
    "            ║ ║         ║ ║ ║ ║",
    "            ║ ╚═══╗     ╔═══╝ ║",
    "            ║     ║     ║     ║",
    "            ╚═════╝     ╚═════╝"
]

# Print glasses with typing animation
def print_with_typing(text, delay=0.04, color=WHITE):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)

# Draw glasses with a pulsing effect
def animate_glasses():
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]
    for _ in range(3):
        color = random.choice(colors)
        for line in glasses:
            sys.stdout.write(color + line + RESET + '\n')
            time.sleep(0.08)
        sys.stdout.write('\033[F' * len(glasses))  # Move cursor up
        time.sleep(0.1)

# Main program
def main():
    # Clear screen
    print('\033[2J\033[H', end='')
    
    # Title
    print_with_typing(BOLD + MAGENTA + "WOODY ALLEN PHILOSOPHY GENERATOR" + RESET + '\n\n', 0.06)
    
    # Animate glasses
    animate_glasses()
    print()  # Clear the last glasses line
    
    # Draw a fancy box
    box_width = 70
    print(BOLD + YELLOW + "╔" + "═" * (box_width - 2) + "╗" + RESET)
    
    # Neurotic Woody Allen-style philosophical quote
    quote = "I'm not afraid of death; I'm just afraid the nursing home will have cable but no remote, and I'll spend eternity flipping between infomercials and PBS, wondering if this is what Nietzsche meant by 'eternal recurrence'."
    
    # Split quote into lines to fit in box
    words = quote.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line + " " + word) <= box_width - 4:
            if current_line:
                current_line += " "
            current_line += word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    # Print quote with neurotic typing effect
    for line in lines:
        print(GREEN + "║ " + RESET, end="")
        print_with_typing(line, 0.05, BLUE)
        # Add padding to align right border
        padding = box_width - len(line) - 4
        print(" " * padding + GREEN + " ║" + RESET)
    
    print(YELLOW + "╚" + "═" * (box_width - 2) + "╝" + RESET)
    
    # Signature with Woody Allen's neurotic touch
    print_with_typing("\n" + BOLD + RED + "— Woody Allen (probably said this while checking his health insurance policy)" + RESET + '\n', 0.04)
    
    # Blinking cursor effect for that anxious, neurotic feel
    for _ in range(5):
        sys.stdout.write(BOLD + RED + "█" + RESET)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\b \b")
        sys.stdout.flush()
        time.sleep(0.2)
    
    print("\n\n" + CYAN + "Existential crisis level: " + BOLD + "MAXIMUM" + RESET)

if __name__ == "__main__":
    main()