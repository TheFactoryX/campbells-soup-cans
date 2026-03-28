"""
Campbell's Soup Can #3016
Produced: 2026-03-28 19:45:14
Worker: Anthropic: Claude Opus 4.1 (anthropic/claude-opus-4.1)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

# ANSI color codes
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
WHITE = '\033[97m'
GRAY = '\033[90m'
RESET = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'

def typewriter_effect(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def draw_glasses():
    glasses = f"""
    {GRAY}     ___..._     _...___{RESET}
    {GRAY}  .-'       '-.-'       '-. {RESET}
    {GRAY} /    {WHITE}O{GRAY}       |       {WHITE}O{GRAY}    \\{RESET}
    {GRAY}|             |             |{RESET}
    {GRAY} \\           /|\\           /{RESET}
    {GRAY}  '-..___..-' | '-..___..-'{RESET}
    {GRAY}              |{RESET}
    """
    return glasses

def create_thought_bubble():
    bubble = f"""
    {CYAN}     .-"""""-.{RESET}
    {CYAN}   .'         '.{RESET}
    {CYAN}  /   {YELLOW}NEUROSIS{CYAN}  \\{RESET}
    {CYAN} |  {YELLOW}IN PROGRESS{CYAN}  |{RESET}
    {CYAN}  \\             /{RESET}
    {CYAN}   '.  {RED}. . .{CYAN}  .'{RESET}
    {CYAN}     '-.....-'{RESET}
    """
    return bubble

def main():
    # Clear screen
    print('\033[2J\033[H')
    
    # The quote
    quote = "My therapist says I have a fear of success, which is ironic because I'm also terrified of failure. Basically, I'm just scared of participating."
    author = "- Woody Allen (probably)"
    
    # Opening animation
    print(f"\n{MAGENTA}{'='*60}{RESET}")
    print(f"{BOLD}{WHITE}    EXISTENTIAL CRISIS LOADING...{RESET}")
    print(f"{MAGENTA}{'='*60}{RESET}\n")
    
    # Loading bar animation
    for i in range(21):
        bar = '█' * i + '░' * (20 - i)
        print(f"\r  {GRAY}[{bar}] {i*5}% {random.choice(['Questioning existence...', 'Doubting everything...', 'Analyzing neuroses...'])}{RESET}", end='')
        time.sleep(0.1)
    print("\n")
    
    # Draw Woody's glasses
    print(draw_glasses())
    time.sleep(0.5)
    
    # Thought bubble
    print(create_thought_bubble())
    time.sleep(0.5)
    
    # Quote box
    print(f"\n{CYAN}╔{'═'*70}╗{RESET}")
    print(f"{CYAN}║{RESET}{'  '*35}{CYAN}║{RESET}")
    
    # Type out the quote with dramatic effect
    print(f"{CYAN}║{RESET}  ", end='')
    words = quote.split()
    line_length = 0
    for word in words:
        if line_length + len(word) > 64:
            print(f"  {CYAN}║{RESET}")
            print(f"{CYAN}║{RESET}  ", end='')
            line_length = 0
        
        # Color certain words for emphasis
        if word.lower() in ['fear', 'terrified', 'scared', 'ironic']:
            print(f"{RED}{BOLD}{word}{RESET} ", end='', flush=True)
        elif word.lower() in ['therapist', 'success', 'failure']:
            print(f"{YELLOW}{word}{RESET} ", end='', flush=True)
        else:
            print(f"{WHITE}{word}{RESET} ", end='', flush=True)
        
        line_length += len(word) + 1
        time.sleep(0.08)
    
    # Padding to complete the line
    remaining = 66 - line_length
    print(' ' * remaining, end='')
    print(f"  {CYAN}║{RESET}")
    
    print(f"{CYAN}║{RESET}{'  '*35}{CYAN}║{RESET}")
    print(f"{CYAN}║{RESET}  {GRAY}{ITALIC}{'  '*23}{author:>40}{RESET}  {CYAN}║{RESET}")
    print(f"{CYAN}╚{'═'*70}╝{RESET}")
    
    # Final flourish
    time.sleep(0.5)
    print(f"\n{GRAY}  Press Enter to continue having an existential crisis...{RESET}")
    
    # Blinking cursor effect
    for _ in range(3):
        print(f"\r{GRAY}  ▌{RESET}", end='', flush=True)
        time.sleep(0.3)
        print(f"\r{GRAY}   {RESET}", end='', flush=True)
        time.sleep(0.3)
    
    print(f"\n\n{MAGENTA}✨ {ITALIC}Remember: Life is like a movie - terrible script, but at least the popcorn's good.{RESET} {MAGENTA}✨{RESET}\n")

if __name__ == "__main__":
    main()