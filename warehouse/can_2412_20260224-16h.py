"""
Campbell's Soup Can #2412
Produced: 2026-02-24 16:14:01
Worker: Qwen: Qwen Plus 0728 (qwen/qwen-plus-2025-07-28)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
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
UNDERLINE = '\033[4m'
ENDC = '\033[0m'

colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_oscillating(text):
    length = len(text)
    for i in range(10):
        spaces = abs(5 - i)
        line = " " * spaces + text
        color = random.choice(colors)
        sys.stdout.write(f'\r{color}{line}{ENDC}')
        sys.stdout.flush()
        time.sleep(0.2)
    print()

def print_thinking_cloud():
    cloud = [
        "     ╭───────────────────────────────────╮",
        "     │                                   │",
        "     │  I used to worry about the       │",
        "     │  meaning of life until I realized│",
        "     │  that my anxiety has its own     │",
        "     │  gravitational pull—              │",
        "     │  it curves spacetime            ⏳ │",
        "     │  more than mass does.            │",
        "     │  Now I'm terrified of            │",
        "     │  empty space...                   │",
        "     │  ...and crowded rooms.           │",
        "     │                                   │",
        "     ╰───────────────────────────────────╯",
        "            \\   ^__^",
        "             \\  (oo)\\_______",
        "                (__)\\       )\\/\\",
        "                    ||----w |",
        "                    ||     ||"
    ]
    
    for i, line in enumerate(cloud):
        if "anxiety" in line:
            time.sleep(0.3)
            sys.stdout.write(f"{BOLD}{MAGENTA}{line}{ENDC}\n")
        elif "gravitational" in line or "spacetime" in line:
            time.sleep(0.3)
            sys.stdout.write(f"{BOLD}{BLUE}{line}{ENDC}\n")
        elif "empty space" in line or "crowded rooms" in line:
            time.sleep(0.3)
            sys.stdout.write(f"{BOLD}{RED}{line}{ENDC}\n")
        else:
            time.sleep(0.1)
            sys.stdout.write(f"{GREEN}{line}{ENDC}\n")
        sys.stdout.flush()
        time.sleep(0.1)

def print_blinking_text(text):
    for _ in range(3):
        sys.stdout.write(f"\r{BOLD}{YELLOW}{text}{ENDC}")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(f"\r{BOLD}{WHITE}{' '*len(text)}{ENDC}")
        sys.stdout.flush()
        time.sleep(0.3)
    sys.stdout.write(f"\r{BOLD}{YELLOW}{text}{ENDC}\n")

# Main program
def main():
    # Clear screen
    sys.stdout.write('\033[2J\033[H')
    
    print(f"{BOLD}{CYAN}╔════════════════════════════════════════════════╗{ENDC}")
    print_oscillating(f"{BOLD}{YELLOW}       THE UNIVERSE VS. MY STOMACH ACID{ENDC}")
    print(f"{BOLD}{CYAN}╚════════════════════════════════════════════════╝{ENDC}")
    print()
    
    time.sleep(1)
    
    # Print the cartoon with quote
    print_thinking_cloud()
    
    time.sleep(1)
    
    # Blinking existential footnote
    print()
    print_blinking_text("   (I told my therapist the universe is indifferent,")
    print_blinking_text("    but she said my mother is the real issue.)")
    
    # Wiggling period
    period = "."
    line = " "*50
    for i in range(55):
        pos = int(25 + 20 * (i % 2))  # Alternate between left and right
        sys.stdout.write(f'\r{line}')
        sys.stdout.write(f'\r{" "*pos}{RED}{BOLD}{period}{ENDC}')
        sys.stdout.flush()
        time.sleep(0.12)
    
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}Existential crisis interrupted by user.{ENDC}")