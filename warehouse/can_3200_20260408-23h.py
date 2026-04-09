"""
Campbell's Soup Can #3200
Produced: 2026-04-08 23:53:18
Worker: MiniMax: MiniMax M2.5 (free) (minimax/minimax-m2.5:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Style Philosophical Quote Generator
A neurotic, funny, self-deprecating existential experience in terminal form.
"""

import sys
import time
import os

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
ORANGE = "\033[38;5;208m"
PURPLE = "\033[38;5;135m"
PINK = "\033[38;5;205m"
GOLD = "\033[38;5;220m"
LIME = "\033[38;5;190m"

# Background colors
BG_BLACK = "\033[40m"
BG_GREY = "\033[48;5;235m"

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.03, color=RESET):
    """Print text one character at a time."""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def create_box(text, width=70):
    """Create a fancy boxed quote."""
    lines = []
    # Wrap text to fit in box
    words = text.split()
    current_line = []
    for word in words:
        if len(' '.join(current_line + [word])) <= width - 10:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    
    # Find max line length
    max_len = max(len(line) for line in lines) if lines else 0
    
    # Create box
    border_horizontal = '─' * (max_len + 4)
    top = f"  {CYAN}╭{border_horizontal}╮{RESET}"
    bottom = f"  {CYAN}╰{border_horizontal}╯{RESET}"
    
    return top, lines, bottom, max_len

def main():
    clear_screen()
    
    # ASCII Art Header
    header = f"""
{GOLD}        ██╗     ██╗   ██╗ ██████╗ ██╗██████╗ 
        ██║     ██║   ██║██╔═══██╗██║██╔══██╗
        ██║     ██║   ██║██║   ██║██║██║  ██║
        ██║     ██║   ██║██║   ██║██║██║  ██║
        ███████╗╚██████╔╝╚██████╔╝██║██████╔╝
        ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═════╝{RESET}
        
    {PURPLE}{BOLD}   "I'm not afraid of death;"{RESET}
    {PURPLE}{BOLD}   "I just don't want to be there when it happens."{RESET}
    
    {YELLOW}{ITALIC}        ~ Woody Allen{RESET}
    """
    
    print(header)
    time.sleep(0.5)
    
    # The quote
    quote = (
        "I've learned that life is essentially a series of awkward moments "
        "interrupted by brief periods of existential terror, all while trying "
        "to figure out if anyone noticed the spinach in my teeth. I've achieved "
        "nothing meaningful, but I have developed an impressive collection of "
        "anxieties and a subscription to The New Yorker."
    )
    
    # Attribution
    attribution = "— From the diary of a man who over-thinks everything"
    
    # Create the box
    top, quote_lines, bottom, max_len = create_box(quote)
    
    print()
    time.sleep(0.3)
    
    # Print the box with quote
    print(top)
    for i, line in enumerate(quote_lines):
        padding = ' ' * (max_len - len(line))
        color = [CYAN, YELLOW, MAGENTA, LIME, PINK][i % 5]
        print(f"  {CYAN}│{RESET} {color}{line}{padding} {CYAN}│{RESET}")
    print(bottom)
    
    print()
    time.sleep(0.3)
    
    # Print attribution with typewriter effect
    print(f"  {DIM}{WHITE}", end="")
    print_slow(attribution, delay=0.05)
    print(RESET)
    
    print()
    
    # Animated footer
    footer_art = f"""
    {ORANGE}     _______________________
    < I'm giving up on inner peace. >
     _______________________
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||{RESET}
    """
    print(footer_art)
    
    # Final flourish
    print()
    print(f"  {PURPLE}{BOLD}✨ Have a neurotic day! ✨{RESET}")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}Fine, leave. Everyone does.{RESET}")