"""
Campbell's Soup Can #4135
Produced: 2026-07-09 08:44:19
Worker: Poolside: Laguna XS.2 (free) (poolside/laguna-xs.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Wisdom Generator
A neurotic philosophical quote generator with style!
"""

import time
import sys

# ANSI color codes
RESET = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'

def typewriter_effect(text, delay=0.03, color=RESET):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)

def print_ascii_brain():
    """Print a little ASCII brain for existential vibes"""
    brain = f"""
{BOLD}{RED}    ╭─────────────╮
    │  •     •  │
    │     >     │
    ╰─────────────╯{RESET}
    {CYAN}...thinking...{RESET}
"""
    print(brain)
    time.sleep(0.5)

def main():
    # Clear screen
    print('\033[2J\033[H', end='')
    
    # Print header
    header = f"""{BOLD}{MAGENTA}
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   {_YELLOW}🧠 WOODY ALLEN PHILOSOPHICAL WISDOM  🧠{_MAGENTA}              ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
{RESET}"""
    print(header)
    time.sleep(0.3)
    
    # Print the brain
    print_ascii_brain()
    
    # The quote with typewriter effect
    quote = "I'm certainly not religious... I'm more of a 'send me to hell, I'll just order pizza and watch Netflix' kind of guy."
    
    print(f"{BOLD}{BLUE}    ╭──────────────────────────────────────────────────────────────╮{RESET}")
    print(f"{BOLD}{BLUE}    │                                                              │{RESET}")
    
    # Print quote line by line with colors
    words = quote.split()
    colored_words = []
    colors = [RED, YELLOW, CYAN, MAGENTA, GREEN]
    
    for i, word in enumerate(words):
        if word in ["I'm", "religious"]:
            colored_words.append(f"{RED}{word}{RESET}")
        elif word in ["pizza", "Netflix"]:
            colored_words.append(f"{YELLOW}{word}{RESET}")
        elif word in ["hell", "send"]:
            colored_words.append(f"{MAGENTA}{word}{RESET}")
        else:
            colored_words.append(word)
    
    formatted_quote = "  " + " ".join(colored_words)
    
    # Print with typewriter
    for char in formatted_quote:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    
    print(f"{BOLD}{BLUE}    │{RESET}")
    print(f"{BOLD}{BLUE}    ╰──────────────────────────────────────────────────────────────╯{RESET}")
    
    # Footer with existential dread
    time.sleep(0.5)
    footer = f"{CYAN}    ...and that's why I'm 99% caffeine and 1% existential crisis{RESET}"
    print(footer)
    
    # Add some shaking effect for neurotic energy
    print(f"\n{BOLD}{RED}    *shivers* {RESET}{WHITE}That was a close one... I almost had an original thought.{RESET}")
    
    # Final message
    time.sleep(1)
    print(f"\n{GREEN}    {BOLD}...or was it?{RESET}")

if __name__ == "__main__":
    main()