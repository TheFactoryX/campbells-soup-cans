"""
Campbell's Soup Can #2503
Produced: 2026-03-01 13:09:58
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
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

# ANSI color codes
RESET = '\033[0m'
BOLD = '\033[1m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'

# Create a neurotic Woody Allen-style quote
quote = "I don't fear death. I just don't want to be there when it happens. And if there is an afterlife, I hope they have good lighting because I'm terrible at reading in dim spaces and I'd probably misplace my existential dread."

# Visual elements
def print_typewriter(text, delay=0.03, color=RESET):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(text_lines, border_color, title=""):
    width = max(len(line) for line in text_lines) + 4
    title_line = f" {title} " if title else ""
    top_border = "╔" + "═" * (width - len(title_line)) + title_line + "╗"
    bottom_border = "╚" + "═" * width + "╝"
    
    print(border_color + top_border + RESET)
    if title:
        print(border_color + "║" + " " * (width - len(title_line) - 2) + title_line + "║" + RESET)
    
    for line in text_lines:
        padding = width - len(line) - 2
        print(border_color + "║ " + line + " " * padding + " ║" + RESET)
    
    print(border_color + bottom_border + RESET)

def print_wooden_glasses():
    glasses = [
        "  " + CYAN + "╭" + "─" * 10 + "╮" + RESET,
        "  " + CYAN + "│" + " " * 10 + "│" + RESET,
        "  " + CYAN + "╰" + "─" * 10 + "╯" + RESET
    ]
    for line in glasses:
        print(line)
        time.sleep(0.1)

def print_animated_dots():
    for _ in range(3):
        sys.stdout.write(RED + "." + RESET)
        sys.stdout.flush()
        time.sleep(0.3)
    print()

def main():
    # Clear screen
    print("\033[H\033[J", end="")
    
    # Print title with animation
    print(YELLOW + "─" * 50 + RESET)
    print_typewriter("  W O O D Y   A L L E N   P H I L O S O P H Y  ", 0.05, BOLD + MAGENTA)
    print(YELLOW + "─" * 50 + RESET)
    time.sleep(0.5)
    
    # Draw wooden glasses animation
    print_wooden_glasses()
    time.sleep(0.7)
    
    # Print neurotic quote in a box with typewriter effect
    words = quote.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= 45:
            current_line += (word + " ")
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())
    
    # Add random neurotic thoughts as "whispers"
    whispers = [
        " (I'm probably overthinking this...)",
        " (What if I'm the only one who cares?)",
        " (This might be irrelevant but...)",
        " (I should've called my therapist...)",
        " (Does this make me sound insecure?)"
    ]
    lines[-1] += random.choice(whispers)
    
    print("\n" + BLUE + "  " + " " * 40 + "  " + RESET)
    draw_box(lines, BLUE, "NEUROTIC WISDOM")
    
    # Typewriter effect for the quote
    print("\n" + GREEN + "  " + " " * 40 + "  " + RESET)
    print(GREEN + "  ║ " + RESET, end="")
    for i, line in enumerate(lines):
        if i == 0:
            print_typewriter(line, 0.04, GREEN)
        else:
            print_typewriter(" " * 4 + line, 0.04, GREEN)
        if i < len(lines) - 1:
            print(GREEN + "  ║ " + RESET, end="")
    print(GREEN + "  ║ " + RESET, end="")
    
    # Add blinking cursor effect
    for _ in range(3):
        sys.stdout.write(BLUE + "_")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\b ")
        sys.stdout.flush()
        time.sleep(0.3)
    sys.stdout.write("\b" + RESET)
    print()
    
    # Final neurotic tagline
    print("\n" + RED + "  " + " " * 40 + "  " + RESET)
    print(RED + "  ║ ", end="")
    print_typewriter("This quote may cause existential anxiety. Side effects include: overanalyzing, second-guessing, and sudden urges to make an appointment with a therapist. Consult your physician if symptoms persist for more than 30 seconds. Which they will.", 0.02)
    print(RED + "  ║ " + RESET)
    
    # Print footer with animation
    print("\n" + YELLOW + "─" * 50 + RESET)
    print_typewriter("  (c) 2023 Allen-esque Thoughts Inc. - All rights reserved. Probably.", 0.03, BOLD)
    print(YELLOW + "─" * 50 + RESET + "\n")
    
    # Add a final neurotic sigh
    print(BLUE + "  " + " " * 40 + "  " + RESET)
    print(BLUE + "  ║ " + RESET, end="")
    print_typewriter("...and that's why I can't sleep. Good night? Maybe.", 0.05, YELLOW)
    print(BLUE + "  ║ " + RESET)
    print(BLUE + "  ╚" + "═" * 48 + "╝" + RESET)
    
    # Final animation
    print("\n" + MAGENTA + "  [Press Ctrl+C to stop overthinking...]" + RESET, end="")
    print_animated_dots()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + RED + "\n  [Overthinking interrupted. Back to regular neurosis.]" + RESET)