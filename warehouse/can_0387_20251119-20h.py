"""
Campbell's Soup Can #387
Produced: 2025-11-19 20:30:48
Worker: Sherlock Dash Alpha (openrouter/sherlock-dash-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os
import sys

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def spin_animation(duration=1):
    spinner = ['|', '/', '—', '\\']
    start_time = time.time()
    while time.time() - start_time < duration:
        for char in spinner:
            sys.stdout.write(f'\r{RED}Thinking philosophically... {char}{RESET}')
            sys.stdout.flush()
            time.sleep(0.1)
    print(f'\r{RESET}                                    \r', end='')

def main():
    clear_screen()
    
    # Animated title with Woody Allen vibe
    title = f"{MAGENTA}{BOLD}╔══════════════════════════════════════╗{RESET}"
    title += f"\n{MAGENTA}{BOLD}║{RESET}        WOODY ALLEN'S             {MAGENTA}{BOLD}║{RESET}"
    title += f"\n{MAGENTA}{BOLD}║{RESET}      NEUROTIC WISDOM            {MAGENTA}{BOLD}║{RESET}"
    title += f"\n{MAGENTA}{BOLD}╚══════════════════════════════════════╝{RESET}"
    
    typewriter_print(title, 0.02)
    
    # Spinning thinker animation
    spin_animation(1.5)
    
    # The quote - original Woody Allen style
    quote = f"{YELLOW}{ITALIC}'I finally figured out why I'm so{RESET}"
    quote += f"\n{YELLOW}{ITALIC} afraid of success... because then{RESET}"
    quote += f"\n{YELLOW}{ITALIC} I'd have to pretend I understand{RESET}"
    quote += f"\n{YELLOW}{ITALIC} what the hell I'm doing!'{RESET}"
    
    # Fancy quote box
    box_top = f"{GREEN}{BOLD}╭{'─' * 52}╮{RESET}"
    box_mid1 = f"{GREEN}{BOLD}│{RESET} {quote.splitlines()[0]:^50} {GREEN}{BOLD}│{RESET}"
    box_mid2 = f"{GREEN}{BOLD}│{RESET} {quote.splitlines()[1]:^50} {GREEN}{BOLD}│{RESET}"
    box_mid3 = f"{GREEN}{BOLD}│{RESET} {quote.splitlines()[2]:^50} {GREEN}{BOLD}│{RESET}"
    box_mid4 = f"{GREEN}{BOLD}│{RESET} {quote.splitlines()[3]:^50} {GREEN}{BOLD}│{RESET}"
    box_bot = f"{GREEN}{BOLD}╰{'─' * 52}╯{RESET}"
    
    # Fade-in effect for quote
    for line in [box_top, box_mid1, box_mid2, box_mid3, box_mid4, box_bot]:
        typewriter_print(line, 0.05)
        time.sleep(0.2)
    
    # Final flourish
    time.sleep(0.5)
    print(f"\n{CYAN}{BOLD}✦  Neurotic. Existential. Deliciously Anxious.  ✦{RESET}")
    
    # Fade out effect
    time.sleep(2)
    print(f"\n{RED}...and scene.{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{RESET}Existence interrupted. Very Woody.")