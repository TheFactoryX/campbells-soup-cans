"""
Campbell's Soup Can #2080
Produced: 2026-02-06 17:04:24
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes for colors and styles
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"
ITALIC = "\033[3m"
BOLD = "\033[1m"

# Woody Allen style quote
quote = "I'm not saying life is meaningless, but if it had meaning,\n" \
        "I probably wouldn't be the one to figure it out.\n" \
        "       - My Therapist Says I'm Making Progress"

def type_with_effect(text, delay=0.03):
    """Print text with typing animation"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def blinking_cursor(duration=3, speed=0.5):
    """Create blinking cursor effect"""
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write("_")
        sys.stdout.flush()
        time.sleep(speed)
        sys.stdout.write("\b \b")
        sys.stdout.flush()
        time.sleep(speed)

def main():
    # Clear screen
    print("\033[H\033[J")
    
    # Print fancy ASCII art frame
    print(f"{YELLOW}{'-'*65}{RESET}")
    print(f"{YELLOW}|{RESET}", end="")
    print(f"{CYAN}{' '*27}WOODY ALLEN-ISMS{' '*27}{RESET}", end="")
    print(f"{YELLOW}|{RESET}")
    print(f"{YELLOW}{'-'*65}{RESET}")
    
    # Print animated quote
    print(f"\n{YELLOW}    ╭{'-'*58}╮{RESET}")
    print(f"{YELLOW}    │ {RESET}", end="")
    type_with_effect(f"{ITALIC}{BOLD}{RED}{quote}{RESET}", delay=0.04)
    print(f"{YELLOW}    ╰{'-'*58}╯{RESET}")
    
    # Add blinking cursor for dramatic effect
    print("\n\n    ")
    blinking_cursor(duration=2)
    
    # Reset colors at end
    print(RESET)

if __name__ == "__main__":
    main()