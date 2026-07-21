"""
Campbell's Soup Can #4282
Produced: 2026-07-21 20:35:42
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A neurotic existential crisis, served with a side of font colors.
"""

import sys
import time
import shutil

# ANSI color codes because even despair looks better in technicolor
class Colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ORANGE = '\033[38;5;208m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    RESET = '\033[0m'

def typewriter(text, delay=0.03):
    """Print text like a neurotic typewriter having second thoughts."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animated_border(width, char="═", color=Colors.CYAN):
    """Draw a border with a little animation flair."""
    for i in range(width):
        print(color + char, end='', flush=True)
        time.sleep(0.005)
    print()

def draw_woody():
    """A minimalist ASCII Woody Allen because why not?"""
    return f"""
{Colors.YELLOW}           ┌─────────────┐
           │  ◔     ◔  │
           │     ▽     │   {Colors.ORANGE}Hi, I'm Woody.
           │   ╭─╯     │   {Colors.YELLOW}Let me ruin your evening.{Colors.RESET}
           │  ╱         │
           └──┴─────────┘
    """

def main():
    # Clear the screen for dramatic effect
    print('\033[2J\033[H', end='')
    
    # Get terminal width for centering
    try:
        term_width = shutil.get_terminal_size().columns
    except:
        term_width = 80
    
    # Draw the top border with animation
    print()
    animated_border(60)
    
    # Print Woody
    draw_woody()
    
    # Animated border again
    animated_border(60)
    
    print()
    
    # The quote with dramatic pauses
    quote_lines = [
        f"{Colors.BOLD}{Colors.PURPLE}    \"I told my therapist about my fear of death,",
        f"{Colors.BOLD}{Colors.BLUE}     she said that's perfectly normal —",
        f"{Colors.BOLD}{Colors.CYAN}     everyone's terrified of the big sleep.",
        f"{Colors.BOLD}{Colors.GREEN}     But here's my real problem: {Colors.RED}what if",
        f"{Colors.BOLD}{Colors.YELLOW}     death is just the universe's way of saying",
        f"{Colors.BOLD}{Colors.ORANGE}     'You're not *that* funny,' and then",
        f"{Colors.BOLD}{Colors.PURPLE}     I have to live with that thought",
        f"{Colors.BOLD}{Colors.BLUE}     for all eternity?\"",
    ]
    
    for line in quote_lines:
        typewriter(line)
        time.sleep(0.3)
    
    print()
    
    # Attribution
    attribution = f"{Colors.DIM}{Colors.ITALIC}     — Anonymous Neurotic Philosopher"
    typewriter(attribution, 0.05)
    
    print()
    
    # Bottom border
    animated_border(60, char="═", color=Colors.PURPLE)
    
    # A little existential footnote
    print(f"\n{Colors.DIM}   (This message will self-destruct in... never. ")
    print(f"{Colors.DIM}    Like my anxiety, it's permanent.){Colors.RESET}\n")

if __name__ == "__main__":
    main()