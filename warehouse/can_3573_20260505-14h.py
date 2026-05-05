"""
Campbell's Soup Can #3573
Produced: 2026-05-05 14:24:39
Worker: Poolside: Laguna XS.2 (free) (poolside/laguna-xs.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Philosophical Quote Generator
Because existential crises deserve flair!
"""

import time
import random
import sys

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
DIM = '\033[2m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'
RESET = '\033[0m'

def typewriter_effect(text, delay=0.03, color=WHITE):
    """Print text with a typewriter effect."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)

def print_ascii_brain():
    """Print a little neurotic brain ASCII art."""
    brain = f"""
{CYAN}    ╭─────────────────────────────╮
    │  {'_':_<(_)}  }({'_':_>_)':_'  }  │
    │   >--"--"<   >--"--"<  >--"--<   │
    ╰─────────────────────────────╯{RESET}
    """
    print(brain)

def print_quote_box(quote):
    """Print the quote in a decorative box."""
    lines = quote.split('\n')
    max_len = max(len(line) for line in lines)
    
    border_top = f"{RED}╔{'═' * (max_len + 2)}╗{RESET}"
    border_bottom = f"{RED}╚{'═' * (max_len + 2)}╝{RESET}"
    
    print(border_top)
    for line in lines:
        padding = ' ' * (max_len - len(line))
        print(f"{RED}║{RESET} {MAGENTA}{line}{RESET}{padding} {RED}║{RESET}")
    print(border_bottom)

def main():
    # Clear screen
    print('\033[2J\033[H', end='')
    
    # Print header
    header = f"""
{BOLD}{BLUE}╔══════════════════════════════════════════════════════╗
║                                                    ║
║   WOODY ALLEN STYLE PHILOSOPHICAL QUOTE GENERATOR  ║
║                                                    ║
╚══════════════════════════════════════════════════════╝{RESET}
"""
    print(header)
    
    # Print the brain
    print_ascii_brain()
    
    # The Woody Allen style quote
    quote = """I used to pray for patience,
but I'm still waiting.
Life is like a pipeline
full of existential dread
and slightly stale coffee.
I don't want immortality —
I just want to not be here
when it happens...
again."""
    
    # Print intro text
    intro = f"{DIM}Preparing profound wisdom...{RESET}"
    print(intro)
    time.sleep(1.5)
    
    # Print the quote with typewriter effect
    print(f"\n{YELLOW}Here's your existential comfort snack:{RESET}\n")
    time.sleep(0.5)
    
    # Print with color variation
    words = quote.split()
    colored_quote = []
    colors = [RED, YELLOW, MAGENTA, CYAN, WHITE]
    
    for i, word in enumerate(words):
        color = colors[i % len(colors)]
        if word in ['Life', 'I', 'patience', 'immortality']:
            colored_quote.append(f"{color}{word}{RESET}")
        else:
            colored_quote.append(word)
    
    formatted_quote = ' '.join(colored_quote)
    
    # Print with typewriter effect
    typewriter_effect(formatted_quote, delay=0.04, color=WHITE)
    
    # Print the box with the quote
    print()
    print_quote_box(quote)
    
    # Print footer
    footer = f"""
{GREEN}╔══════════════════════════════════════════════════════╗
║                                                    ║
║  Remember: Existence is suffering, but pizza helps! ║
║                                                    ║
╚══════════════════════════════════════════════════════╝{RESET}
"""
    print(footer)

if __name__ == "__main__":
    main()