"""
Campbell's Soup Can #2326
Produced: 2026-02-20 04:58:08
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

def print_ansi(text, color):
    sys.stdout.write(f"{color}{text}\033[0m")
    sys.stdout.flush()

def type_print(text, color, delay=0.02):
    for char in text:
        print_ansi(char, color)
        time.sleep(delay)

def main():
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    WHITE = "\033[97m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    
    # ASCII art Woody
    woody_art = [
        "    ,-----.",
        "   /  o o  \\",
        "  |    ^    |",
        "   \\  ---  /",
        "    `-----'",
        "     (o o)",
        "    /  v  \\",
        "   /_______\\",
        "  (Worried about existence)"
    ]
    
    # Philosophy quote in Woody Allen style
    quote = "I'm not afraid of death; I just don't want to be there when it happens... but if I'm not there, how will I know it happened? And if I'm there, won't that be the worst possible time to be present?"
    
    # Print ASCII art
    print("\n" * 5)
    for line in woody_art:
        print_ansi(line.center(60), WHITE)
        time.sleep(0.1)
    print()
    
    # Print quote box with animation
    box_width = 58
    top_border = f"{BLUE}┌{'─' * (box_width-2)}┐"
    bottom_border = f"{BLUE}└{'─' * (box_width-2)}┘"
    
    print_ansi(top_border, BLUE)
    print()
    
    # Split quote into lines
    words = quote.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= box_width - 4:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    
    # Animate each line with typewriter effect
    for line in lines:
        print_ansi(f"{BLUE}│ ", BLUE)
        type_print(line.ljust(box_width-4), YELLOW)
        print_ansi(f" {BLUE}│", BLUE)
        print()
        time.sleep(0.1)
    
    print_ansi(bottom_border, BLUE)
    
    # Add neurotic footer
    print()
    time.sleep(0.5)
    print_ansi("  (This quote has been approved by my therapist... who is also my mother)", RED)
    time.sleep(0.3)
    print_ansi("  ...or was it my analyst? I can never remember these things.", GREEN)
    
    # Final sigh effect
    time.sleep(1)
    print("\n" * 2)
    print_ansi("  *sigh*".center(60), WHITE)
    time.sleep(0.5)
    print_ansi("  ...and now I'm depressed again.", RED)

if __name__ == "__main__":
    main()