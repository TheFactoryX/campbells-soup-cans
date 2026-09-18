"""
Campbell's Soup Can #4984
Produced: 2026-09-18 19:37:05
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI escape codes
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
ITALIC = '\033[3m'
BLINK = '\033[5m'

# Colors
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

# Bright colors
BRIGHT_BLACK = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_WHITE = '\033[97m'

# Backgrounds
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'

# Cursor control
CLEAR_LINE = '\033[2K'
CURSOR_UP = '\033[A'
CURSOR_DOWN = '\033[B'
CURSOR_LEFT = '\033[D'
CURSOR_RIGHT = '\033[C'
HIDE_CURSOR = '\033[?25l'
SHOW_CURSOR = '\033[?25h'
CLEAR_SCREEN = '\033[2J'
HOME = '\033[H'

# Woody Allen ASCII portrait
WOODY = f"""{BRIGHT_YELLOW}
       ╔══════════════════════════════════════╗
       ║           {BRIGHT_WHITE}WOODY ALLEN{BRIGHT_YELLOW}            ║
       ║                                      ║
       ║         {BRIGHT_WHITE}┌─────────────┐{BRIGHT_YELLOW}         ║
       ║         │  {BRIGHT_BLACK}██{BRIGHT_YELLOW}   {BRIGHT_BLACK}██{BRIGHT_YELLOW}  │ {BRIGHT_WHITE}← glasses{BRIGHT_YELLOW}       ║
       ║         │  {BRIGHT_BLACK}██{BRIGHT_YELLOW}   {BRIGHT_BLACK}██{BRIGHT_YELLOW}  │                   ║
       ║         │      {BRIGHT_RED}▲{BRIGHT_YELLOW}      │ {BRIGHT_WHITE}← nose{BRIGHT_YELLOW}          ║
       ║         │   {BRIGHT_MAGENTA}┌─────┐{BRIGHT_YELLOW}   │ {BRIGHT_WHITE}← mouth{BRIGHT_YELLOW}         ║
       ║         │   │     │{BRIGHT_YELLOW}   │                   ║
       ║         └───┴─────┴───┘                   ║
       ║           {BRIGHT_WHITE}"neurotic since 1935"{BRIGHT_YELLOW}          ║
       ╚══════════════════════════════════════╝
{RESET}"""

# The quote - original Woody Allen style
QUOTE = ("I don't believe in an afterlife, but I'm bringing a "
         "change of underwear just in case. You know, for the "
         "awkward conversation with God.")

QUOTE_PARTS = [
    ("I don't believe in an afterlife, ", CYAN),
    ("but I'm bringing a ", BRIGHT_CYAN),
    ("change of underwear ", YELLOW + BOLD),
    ("just in case. ", BRIGHT_YELLOW),
    ("You know, ", MAGENTA),
    ("for the awkward ", RED),
    ("conversation with God.", BRIGHT_RED + BOLD),
]

def typewriter_print(text, color=WHITE, delay=0.03, end=''):
    """Print text with typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))
    if end:
        sys.stdout.write(end)
    sys.stdout.flush()

def print_boxed_quote():
    """Print the quote in a fancy animated box."""
    width = 70
    padding = 2
    
    # Top border
    print(f"\n{BRIGHT_BLACK}╔{'═' * (width + padding * 2)}╗{RESET}")
    
    # Empty line
    print(f"{BRIGHT_BLACK}║{' ' * (width + padding * 2)}║{RESET}")
    
    # Quote line - animated
    sys.stdout.write(f"{BRIGHT_BLACK}║{' ' * padding}{RESET}")
    sys.stdout.flush()
    
    for part, color in QUOTE_PARTS:
        typewriter_print(part, color, delay=0.025)
    
    # Calculate remaining spaces
    total_chars = sum(len(p) for p, _ in QUOTE_PARTS)
    remaining = width - total_chars
    sys.stdout.write(f"{' ' * (remaining + padding)}{BRIGHT_BLACK}║{RESET}\n")
    sys.stdout.flush()
    
    # Empty line
    print(f"{BRIGHT_BLACK}║{' ' * (width + padding * 2)}║{RESET}")
    
    # Bottom border with attribution
    attribution = " — Woody Allen (probably) "
    attr_len = len(attribution)
    left_pad = (width + padding * 2 - attr_len) // 2
    right_pad = width + padding * 2 - attr_len - left_pad
    print(f"{BRIGHT_BLACK}║{' ' * left_pad}{DIM}{ITALIC}{attribution}{RESET}{BRIGHT_BLACK}{' ' * right_pad}║{RESET}")
    print(f"{BRIGHT_BLACK}╚{'═' * (width + padding * 2)}╝{RESET}\n")

def animated_thought_bubble():
    """Show a thought bubble animation before the quote."""
    thoughts = [
        "wait, did I leave the stove on?",
        "what if nothing matters?",
        "my left knee hurts... is it cancer?",
        "I should've been a dentist.",
        "death is just God's way of saying 'you're fired'.",
        "why did I say 'you too' when the waiter said 'enjoy your meal'?",
    ]
    
    print(f"{HIDE_CURSOR}", end='')
    sys.stdout.flush()
    
    for i, thought in enumerate(thoughts):
        # Clear previous
        if i > 0:
            sys.stdout.write(f"{CURSOR_UP}{CLEAR_LINE}")
        
        # Draw bubble
        bubble_width = len(thought) + 4
        print(f"{BRIGHT_CYAN}  .─{'─' * bubble_width}─.")
        print(f"  (  {DIM}{ITALIC}{thought}{RESET}{BRIGHT_CYAN}  )")
        print(f"  '─{'─' * bubble_width}─'{RESET}")
        
        # Little pointer
        print(f"{BRIGHT_CYAN}     \\{RESET}")
        print(f"{BRIGHT_CYAN}      \\{RESET}")
        print(f"{BRIGHT_CYAN}       \\{RESET}")
        
        time.sleep(0.8)
        
        # Clear bubble
        for _ in range(6):
            sys.stdout.write(f"{CURSOR_UP}{CLEAR_LINE}")
            sys.stdout.flush()
    
    print(f"{SHOW_CURSOR}", end='')
    sys.stdout.flush()

def main():
    # Clear screen and start
    print(f"{CLEAR_SCREEN}{HOME}", end='')
    
    # Title
    print(f"{BRIGHT_MAGENTA}{BOLD}")
    print("    ╔══════════════════════════════════════════════════════════════╗")
    print("    ║  A WOODY ALLEN MOMENT OF EXISTENTIAL NEUROSIS               ║")
    print("    ╚══════════════════════════════════════════════════════════════╝")
    print(f"{RESET}")
    
    # Show Woody
    print(WOODY)
    
    # Animated thought process
    print(f"{CYAN}Woody is thinking...{RESET}\n")
    animated_thought_bubble()
    
    # Dramatic pause
    time.sleep(0.5)
    
    # The reveal
    print(f"\n{MAGENTA}{BOLD}And then it hits him...{RESET}\n")
    time.sleep(0.8)
    
    # Print the quote in a fancy box
    print_boxed_quote()
    
    # Final philosophical musing
    musings = [
        f"{DIM}...he immediately schedules a colonoscopy.{RESET}",
        f"{DIM}...wonders if God wears boxers or briefs.{RESET}",
        f"{DIM}...realizes he forgot to floss.{RESET}",
    ]
    
    chosen = random.choice(musings)
    typewriter_print(chosen, WHITE, delay=0.02)
    print(f"\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RESET}{YELLOW}Woody has left the building. (Ctrl+C detected){RESET}")
        sys.exit(0)