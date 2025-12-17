"""
Campbell's Soup Can #1004
Produced: 2025-12-17 23:31:32
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def typewriter_effect(text, color_code, delay=0.03):
    for char in text:
        sys.stdout.write(f"{color_code}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print("\033[0m")

def display_quote():
    clear_screen()
    
    # Colors
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    # Woody Allen ASCII art with integrated quote
    woody_display = [
        YELLOW + "     .--.     " + BLUE + "╔══════════════════════════════════════════════════════════════╗" + RESET,
        YELLOW + "    |o_o |    " + BLUE + "║  WOODY ALLEN ON LIFE                                    ║" + RESET,
        YELLOW + "    |:_/ |    " + BLUE + "║  ══════════════════════════════════════════════════════  ║" + RESET,
        YELLOW + "   //   \\ \\   " + BLUE + "║  I don't want to achieve immortality through my work;   ║" + RESET,
        YELLOW + "  (|     | )  " + BLUE + "║  I want to achieve it through not dying.                ║" + RESET,
        YELLOW + " /'\\_   _/`\\  " + BLUE + "║  And if that doesn't work, I've got a backup plan:     ║" + RESET,
        YELLOW + "\\___)=(___/   " + BLUE + "║  I'm going to take up philosophy. It's cheaper than    ║" + RESET,
        BLUE + "               " + BLUE + "║  therapy, and probably about as effective. The only    ║" + RESET,
        BLUE + "               " + BLUE + "║  difference is that with philosophy, you get to wear    ║" + RESET,
        BLUE + "               " + BLUE + "║  a tweed jacket and pretend you're smarter than you    ║" + RESET,
        BLUE + "               " + BLUE + "║  really are.                                            ║" + RESET,
        BLUE + "               " + BLUE + "║  ══════════════════════════════════════════════════════  ║" + RESET,
        BLUE + "               " + BLUE + "║                  - Woody Allen                          ║" + RESET,
        BLUE + "               " + BLUE + "╚══════════════════════════════════════════════════════════════╝" + RESET
    ]
    
    # Intro animation
    print("\n")
    for i in range(3):
        time.sleep(0.2)
        sys.stdout.write(f"\r{YELLOW}Thinking... \033[0m")
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write(f"\r{BLUE}Overthinking... \033[0m")
        sys.stdout.flush()
    
    # Display with animations
    print("\n")
    for line in woody_display:
        typewriter_effect(line, RESET, 0.01)
    
    # Final animation
    print("\n")
    final_messages = [
        f"{YELLOW} Woody Allen would probably overthink this entire program... ",
        f"{BLUE}  But hey, at least it's cheaper than therapy! ",
        f"{GREEN}   And that's my existential crisis for today. "
    ]
    
    for msg in final_messages:
        sys.stdout.write(f"\r{msg}\033[0m")
        sys.stdout.flush()
        time.sleep(1)
    
    print("\n\n\033[0m", end="")

if __name__ == "__main__":
    display_quote()