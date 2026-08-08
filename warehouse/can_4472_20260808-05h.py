"""
Campbell's Soup Can #4472
Produced: 2026-08-08 05:56:12
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
A neurotic existential crisis in pure Python.
No philosophers were harmed in the making of this code.
"""

import sys
import time
import itertools

# ANSI color codes because even despair needs a splash of color
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    
    BRIGHT_RED = "\033[91;1m"
    BRIGHT_GREEN = "\033[92;1m"
    BRIGHT_YELLOW = "\033[93;1m"
    BIGHT_BLUE = "\033[94;1m"
    BRIGHT_MAGENTA = "\033[95;1m"
    BRIGHT_CYAN = "\033[96;1m"

def print_slow(text, delay=0.03, end="\n"):
    """Print text character by character with existential dread."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print(end, end='', flush=True)

def print_centered(text, width=70):
    """Center text like a nervous center of attention."""
    for line in text.split('\n'):
        print(line.center(width))

def animate_text_rainbow(text, iterations=3, delay=0.2):
    """Animate text through all the colors of anxiety."""
    colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, 
              Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
    for _ in range(iterations):
        for color in colors:
            print(f"\r{color}{Colors.BOLD}{text}{Colors.RESET}", end='', flush=True)
            time.sleep(delay)
    print()

def draw_thought_bubble():
    """Draw a thought bubble for our neurotic narrator."""
    bubble = f"""
    ╭─────────────────────────────────────────────╮
    │  {Colors.ITALIC}{Colors.DIM}...if consciousness is just atoms{Colors.RESET}   │
    │  {Colors.ITALIC}{Colors.DIM}fooling themselves into thinking...{Colors.RESET}   │
    │  {Colors.ITALIC}{Colors.DIM}then I'm the most sophisticated{Colors.RESET}       │
    │  {Colors.ITALIC}{Colors.DIM}fool in the universe.{Colors.RESET}                │
    ╰─────────────────────────────────────────────╯
    """
    print_centered(bubble)

def draw_owl():
    """Draw a tiny existential owl."""
    owl = f"""
    {Colors.YELLOW}   ⌖⌖          
     {Colors.BOLD}ʕ•ᴥ•ʔ{Colors.RESET}
    {Colors.YELLOW}  /│●│\\        
     {Colors.DIM}/ │●│ \\       
           ││         
    {Colors.CYAN}    ╱╲ ╱╲       
       ╱  ╲╱  ╲{Colors.RESET}
    """
    print(owl.center(70))

def draw_quote_box(quote_lines):
    """Draw the main quote in a fancy box."""
    max_len = max(len(line) for line in quote_lines)
    padding = 4
    width = max_len + 2 * padding
    
    # Top border
    print(f"    {Colors.MAGENTA}╔{'═' * width}╗{Colors.RESET}")
    
    # Quote lines
    for line in quote_lines:
        print(f"    {Colors.MAGENTA}║{Colors.RESET}  {Colors.BOLD}{Colors.CYAN}{line:<{max_len}}{Colors.RESET}  {Colors.MAGENTA}║{Colors.RESET}")
    
    # Bottom border
    print(f"    {Colors.MAGENTA}╚{'═' * width}╝{Colors.RESET}")
    
    # Attribution
    attribution = "— A confused Pythonista"
    print(f"    {Colors.DIM}{attribution.rjust(width//2 + padding)}{Colors.RESET}")

def main():
    """Main function that questions its own existence."""
    # Clear screen effect
    print("\033[2J\033[H", end='')
    
    # Animated title
    title = "Existential Crisis.exe"
    print()
    animate_text_rainbow(title, iterations=2, delay=0.15)
    print()
    
    # Loading dots of doom
    print_centered(f"{Colors.DIM}Compiling thoughts...{Colors.RESET}")
    dots = itertools.cycle(['.', '..', '...'])
    for i in range(8):
        print(f"\r{Colors.DIM}Thinking{dots.__next__()}{' ' * 10}{Colors.RESET}", end='', flush=True)
        time.sleep(0.3)
    print()
    print()
    
    # The owl that knows too much
    draw_owl()
    
    # Thought bubble
    draw_thought_bubble()
    
    # The main philosophical crisis
    quote_lines = [
        "I'm not afraid of death,",
        "I just don't want to be there when it happens—",
        "especially since I've already",
        "'lost' my keys, my will to live,",
        "and apparently my ability",
        "to remember why I opened this refrigerator."
    ]
    
    draw_quote_box(quote_lines)
    print()
    
    # Animated existential footer
    footer_text = "404: Meaning Not Found"
    animate_text_rainbow(footer_text, iterations=4, delay=0.25)
    
    # Slow print of a bonus meta-commentary
    print()
    print_slow(f"{Colors.DIM}{Colors.ITALIC}This program will now question its own purpose and exit.{Colors.RESET}", delay=0.07)
    time.sleep(0.5)
    
    # Final existential crisis
    print()
    print_slow(f"{Colors.MAGENTA}{Colors.BOLD}P.S. - What am I doing here?{Colors.RESET}", delay=0.1)
    time.sleep(1)
    
    # Exit with style (and confusion)
    print(f"\n{Colors.DIM}Exiting... but where does 'here' begin and 'there' end?{Colors.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Even our interruption is philosophical
        print(f"\n\n{Colors.YELLOW}Interrupted! Much like the interrupted arc of my life.{Colors.RESET}")
        sys.exit(42)  # The answer, but to what question?