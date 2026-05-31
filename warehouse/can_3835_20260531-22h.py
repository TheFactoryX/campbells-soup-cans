"""
Campbell's Soup Can #3835
Produced: 2026-05-31 22:13:51
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
Woody Allen-style philosophical quote generator with visual flair!
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

def typewriter(text, delay=0.03, color=RESET):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)

def print_box(text, color=CYAN):
    """Print text inside a decorative box."""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    
    print()
    print(color + '┌' + '─' * (max_len + 2) + '┐' + RESET)
    for line in lines:
        print(color + '│' + RESET + ' ' + line.ljust(max_len) + ' ' + color + '│' + RESET)
    print(color + '└' + '─' * (max_len + 2) + '┘' + RESET)
    print()

def main():
    # Clear screen (works on most terminals)
    print('\033[2J\033[H', end='')
    
    # ASCII art header
    header = f"""
{YELLOW}╔════════════════════════════════════════════════════════════╗
║  {RED}🎭{YELLOW}  WOODY ALLEN STYLE PHILOSOPHER  {RED}🎭{YELLOW}                    ║
╚════════════════════════════════════════════════════════════╝{RESET}
"""
    print(header)
    
    # Wait a moment
    time.sleep(0.5)
    
    # The quote with Woody Allen style
    quote = """I told my therapist that I'm afraid of dying.
He said, 'Don't worry, you'll probably survive.'
That's the problem - I'm not so sure about surviving...
I'm more worried about being dead. 
Wait, no, that's fine - I'll be unconscious.
But what if consciousness follows me into the afterlife?
What if I'm just... observing... from somewhere else?
That would be the worst kind of paralysis!
I'd be like, 'Hello? Is this heaven? 
Can you hear me? I'm the ghost of Christmas Past!'"""

    # Print with typewriter effect in different colors
    print()
    for i, line in enumerate(quote.split('\n')):
        delay = 0.02 if len(line) < 30 else 0.01
        color = [RED, YELLOW, MAGENTA, CYAN][i % 4]
        typewriter(line, delay=delay, color=color)
    
    print()
    
    # Attribution with flair
    attribution = f"{WHITE}                    — A neurotic philosopher{RESET}"
    print(attribution)
    
    # Footer with existential message
    footer = f"""
{GREEN}╔════════════════════════════════════════════════════════════╗
║  {RED}💡{GREEN}  Life is like a box of chocolates... I'm not opening it.{GREEN}  ║
╚════════════════════════════════════════════════════════════╝{RESET}
"""
    print(footer)

if __name__ == '__main__':
    main()