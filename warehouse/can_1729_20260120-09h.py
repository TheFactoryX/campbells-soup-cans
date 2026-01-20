"""
Campbell's Soup Can #1729
Produced: 2026-01-20 09:47:37
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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
import os

# ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def type_text(text, delay=0.03, color=None):
    if color:
        text = color + text + Colors.END
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_woody_quote():
    clear_screen()
    
    # Woody Allen ASCII art
    woody_art = [
        "    ___     ",
        "   (o o)    ",
        "  /  V  \\   ",
        " /   |   \\  ",
        "/    |    \\ ",
        "|    |    | ",
        "|____|____| ",
        "    ||||     ",
    ]
    
    # Print Woody Allen art
    for line in woody_art:
        print(f"{Colors.MAGENTA}{line.center(80)}{Colors.END}")
    
    print("\n" + " " * 30 + f"{Colors.BLUE}{Colors.BOLD}WOODY ALLEN ON LIFE{Colors.END}\n")
    
    # Animated quote with emphasis
    quote = "I tried to be a vegetarian once, but I realized plants have feelings too. "
    type_text(quote, delay=0.02)
    
    # Emphasize key parts
    guilty_part = f"{Colors.RED}{Colors.BOLD}Now I just feel guilty about everything{Colors.END}. "
    type_text(guilty_part, delay=0.02)
    
    that_is_part = f"That's {Colors.YELLOW}{Colors.UNDERLINE}progress{Colors.END}, "
    type_text(that_is_part, delay=0.02)
    
    right_part = f"{Colors.CYAN}right{Colors.END}? "
    type_text(right_part, delay=0.02)
    
    # Final punchline
    last_part = f"At least I'm {Colors.GREEN}{Colors.BOLD}consistent{Colors.END} in my {Colors.MAGENTA}{Colors.BOLD}misery{Colors.END}."
    type_text(last_part, delay=0.03)
    
    # Decorative frame
    print("\n" + " " * 28 + Colors.BOLD + "╔" + "═" * 24 + "╗" + Colors.END)
    print(" " * 28 + Colors.BOLD + "║" + " " * 24 + "║" + Colors.END)
    print(" " * 28 + Colors.BOLD + "║" + " " + Colors.WHITE + "~ Existential Humor ~" + Colors.END + " " * 8 + Colors.BOLD + "║" + Colors.END)
    print(" " * 28 + Colors.BOLD + "║" + " " * 24 + "║" + Colors.END)
    print(" " * 28 + Colors.BOLD + "╚" + "═" * 24 + "╝" + Colors.END)
    
    # Sign-off
    print("\n" + " " * 25 + f"{Colors.ITALIC}~ Woody Allen ~{Colors.END}\n")

if __name__ == "__main__":
    display_woody_quote()