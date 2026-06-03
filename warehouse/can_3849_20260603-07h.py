"""
Campbell's Soup Can #3849
Produced: 2026-06-03 07:12:45
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
Woody Allen's Existential Philosophy Generator
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
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)

def main():
    # ASCII art header
    header = f"""
{CYAN}    ╔══════════════════════════════════════════════════════════╗
    ║  {BOLD}{RED} WOODY ALLEN{MAGENTA}  PHILOSOPHY{GREEN}  GENERATOR  {RESET}{CYAN}     ║
    ╚══════════════════════════════════════════════════════════╝{RESET}
"""
    
    print(header)
    
    # Philosophical quote
    quote = "I'm having fun... I'm having fun... I'm having fun... I'm having fun...\nI'm having fun... I'm having fun... I'm having fun... I'm having fun..."
    
    subquote = " — Some therapist, probably"
    
    # Decorative border
    border_top = f"{YELLOW}    ╭{'─' * 58}}╮{RESET}"
    border_bottom = f"{YELLOW}    ╰{'─' * 58}}╯{RESET}"
    
    print(border_top)
    
    # Print quote with typewriter effect and color changes
    lines = quote.split('\n')
    colors = [RED, MAGENTA, CYAN, YELLOW, BLUE]
    
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        # Add some spacing
        print(f"    ")
        typewriter(f"    {line}", delay=0.08, color=color)
    
    print(f"    ")
    typewriter(f"    {subquote}", delay=0.05, color=GREEN)
    
    print(border_bottom)
    
    # Footer
    footer = f"""
{BOLD}{RED}    "The key to a happy life, they tell me, is acceptance.{RESET}{WHITE}
{CYAN}    But I haven't accepted the fact that I'm still waiting for them to tell me{RESET}
{YELLOW}    what exactly I'm supposed to accept!"{RESET}
    """
    
    time.sleep(0.5)
    print(footer)
    
    # Spinning cursor animation
    print(f"\n{MAGENTA}    Loading new philosophy", end="")
    for i in range(5):
        time.sleep(0.3)
        print('.', end='', flush=True)
    print(f" {RED}•{RESET}{MAGENTA}•{RESET}{GREEN}•{RESET}")
    
    time.sleep(0.5)
    print(f"\n{BOLD}{WHITE}    ...or maybe just another existential crisis.{RESET}\n")

if __name__ == "__main__":
    main()