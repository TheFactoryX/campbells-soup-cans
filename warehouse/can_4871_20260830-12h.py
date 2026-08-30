"""
Campbell's Soup Can #4871
Produced: 2026-08-30 12:54:12
Worker: MiniMax: MiniMax M3 (free) (minimax/minimax-m3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
BLINK = "\033[5m"
REVERSE = "\033[7m"

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GRAY = "\033[90m"

# Background colors
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, color=WHITE, delay=0.04):
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)

def slow_print(text, color=WHITE, delay=0.5):
    print(f"{color}{text}{RESET}")
    time.sleep(delay)

def animate_quote():
    clear_screen()
    
    # Title with fade-in
    title = "╔══════════════════════════════════════════════════════════════════╗"
    print(f"\n{YELLOW}{BOLD}{title}{RESET}")
    
    subtitle = "║              NEUROTIC EXISTENTIAL THOUGHTS #42                   ║"
    print(f"{YELLOW}{BOLD}{subtitle}{RESET}")
    print(f"{YELLOW}{BOLD}{'╚══════════════════════════════════════════════════════════════════╝'}{RESET}")
    
    time.sleep(1)
    
    # ASCII art of a thinking face
    print(f"\n{MAGENTA}")
    art = """
            ,     ,
            \\.(.)/
           {  ^  }    *deep sigh*
            ~  ~ 
          _/`---'\\_
         |  ^   ^  |    "Why am I like this?"
          \\  =  /
           |     |
        ___|     |___
       /   |     |   \\
      /    |     |    \\
    """
    for line in art.split('\n'):
        print(line)
        time.sleep(0.1)
    print(RESET)
    
    time.sleep(0.8)
    
    # Setup the quote with animated reveal
    print(f"\n{CYAN}{ITALIC}--- The Quote ---{RESET}\n")
    time.sleep(0.5)
    
    # Box for the quote
    box_top = f"    ┌{'─' * 60}┐"
    print(f"    {DIM}{YELLOW}{box_top}{RESET}")
    
    quote_lines = [
        "I'm not afraid of death; I just don't want to be there",
        "when it happens.  Of course, knowing my luck, I'll",
        "arrive fashionably late,  still holding the wrong",
        "coat check ticket,  convinced the universe is just",
        "a cosmic joke played by a comedian  who definitely",
        "has it in for me personally."
    ]
    
    for line in quote_lines:
        # Typewriter effect for each line
        padding = " " * ((60 - len(line)) // 2)
        for char in line:
            sys.stdout.write(f"    {YELLOW}│{RESET}{padding}{WHITE}{BOLD}{char}{RESET}")
            sys.stdout.flush()
            time.sleep(0.025)
        remaining = 60 - len(line) - ((60 - len(line)) // 2)
        sys.stdout.write(f"{' ' * remaining}{YELLOW}│{RESET}\n")
        time.sleep(0.3)
    
    box_bot = f"    └{'─' * 60}┘"
    print(f"    {DIM}{YELLOW}{box_bot}{RESET}")
    
    time.sleep(0.8)
    
    # Attribution with a blink effect
    attribution = "                                    — Woody Allen (probably, who knows anymore)"
    print(f"\n{MAGENTA}{ITALIC}", end="")
    for char in attribution:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print(f"{RESET}")
    
    time.sleep(0.5)
    
    # The existential wink
    print(f"\n{DIM}{GRAY}    [ ...and on the 8th day, God said: 'Have a nice day' and meant it ironically. ]{RESET}\n")

def philosophical_footer():
    # Animated blinking ellipsis thinking
    print(f"\n{CYAN}{ITALIC}Meanwhile, in a parallel universe...{RESET}")
    time.sleep(0.7)
    
    thoughts = [
        "    • What if the cake IS a lie?",
        "    • Does the universe have an off switch?",
        "    • Why am I arguing with myself again?",
        "    • Is this real, or did I hit snooze on life?"
    ]
    
    for thought in thoughts:
        sys.stdout.write(f"\r{thought}{'.' * (thought.count('.') % 4)}   ")
        sys.stdout.flush()
        time.sleep(0.3)
        print(f"\r{thought}   ")
    
    print(f"\n\n{BLINK}{RED}    🚨 ALERT: {RESET}{YELLOW}You've been overthinking. Again.{RESET}")
    time.sleep(0.5)
    
    print(f"\n{GREEN}    🌿 Suggestion: Take a walk. Pet a cat. Exist.{RESET}\n")

def main():
    try:
        animate_quote()
        philosophical_footer()
        
        # Final dramatic pause
        time.sleep(0.5)
        print(f"{DIM}{GRAY}    [Program gracefully accepts the absurdity of its own existence...]{RESET}")
        print(f"{DIM}{GRAY}    [    ...and then exits, quietly, like nothing ever happened.     ]{RESET}\n")
        
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Oh! You interrupted my existential crisis. How rude. {MAGENTA}🦋{RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()