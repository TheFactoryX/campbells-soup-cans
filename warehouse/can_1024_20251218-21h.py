"""
Campbell's Soup Can #1024
Produced: 2025-12-18 21:28:55
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
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
YELLOW = "\033[38;5;220m"
ORANGE = "\033[38;5;208m"
PINK = "\033[38;5;205m"
BLUE = "\033[38;5;81m"
RESET = "\033[0m"
BOLD = "\033[1m"
CURSOR = "\033[5m"

def typewriter(text, delay=0.03, color=RESET):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Start with blinking cursor effect
    print(f"\n{YELLOW}Generating neurosis...{CURSOR}_\033[0m", end='\r')
    time.sleep(2)
    
    # ASCII art with colors
    print(f"\n{PINK}       ,#####,")
    print(f"       #_   _#")
    print(f"{YELLOW}  O    {PINK}|a` `a|    {BLUE}____")
    print(f"{YELLOW} /|\   {PINK}\\  ˘  /   {BLUE}/    \~~~")
    print(f"{YELLOW}  A    {PINK} )   (    {BLUE}|  ~~~|")
    print(f"       {PINK}/     \   {BLUE}\____/")
    print(f"{RESET}")

    # Quote in a styled box
    quote = "I'm convinced there's a cosmic joke being played on us - but I'm\n" \
            "too insignificant to be in on the punchline, and too anxious\n" \
            "to ask for clarification."
    
    box_top = f"{ORANGE}╔{'═'*60}╗{RESET}"
    box_bottom = f"{ORANGE}╚{'═'*60}╝{RESET}"
    
    print(box_top)
    typewriter(f"{ORANGE}║ {BOLD}{YELLOW}", delay=0)
    typewriter(quote.center(58), delay=0.04, color=YELLOW)
    print(f"{ORANGE}║{RESET}")
    print(box_bottom)

    # Footer text
    time.sleep(0.5)
    print(f"\n{PINK} – Woody Allen's anxious little cousin{RESET}\n")

if __name__ == "__main__":
    main()