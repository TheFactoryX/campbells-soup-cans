"""
Campbell's Soup Can #4898
Produced: 2026-09-04 09:40:11
Worker: MiniMax: MiniMax M2.7 (free) (minimax/minimax-m2.7:free)
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
Run this and embrace the existential dread!
"""

import sys
import time
import os

# ANSI escape codes for colors and styles
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
DIM = '\033[2m'
RESET = '\033[0m'
BLINK = '\033[5m'
REVERSE = '\033[7m'
BGBLUE = '\033[44m'
BGMAGENTA = '\033[45m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def slow_type(lines, line_delay=0.5, char_delay=0.03):
    for line in lines:
        typewriter(line, char_delay)
        print()
        time.sleep(line_delay)

def rain_animation():
    """Make it rain existential thoughts"""
    clear_screen()
    print()
    
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    ]
    
    quote = quotes[0]  # Use the classic one
    
    # ASCII art rain effect
    for i in range(15):
        print(f"{CYAN}{'░' * (i % 40):40}{DIM}~ existential drizzle ~{RESET}")
        time.sleep(0.15)
        clear_screen()
        print()
    
    # The reveal
    print()
    print()
    
    # Create a beautiful box with the quote
    quote_lines = [
        "",
        "  ┌─────────────────────────────────────────────────────────────┐",
        "  │                                                             │",
        f"  │  {YELLOW}{BOLD}\"{quote}\"{RESET}  │",
        "  │                                                             │",
        "  │                                                             │",
        "  └─────────────────────────────────────────────────────────────┘",
        "",
    ]
    
    for line in quote_lines:
        print(f"{MAGENTA}{line}{RESET}")
        time.sleep(0.3)
    
    print()
    time.sleep(1)
    
    # Attribution with dramatic timing
    print(f"  {CYAN}~-{RESET}" * 25)
    time.sleep(0.5)
    
    attr_lines = [
        f"  {GREEN}— Woody Allen{RESET}",
        f"  {DIM}(probably having an existential crisis at 3 AM){RESET}",
        f"  {RED}{BLINK}☠{RESET} {RED}Deathwatch: 47 years and counting...{RESET} {RED}{BLINK}☠{RESET}",
    ]
    
    for line in attr_lines:
        print(line)
        time.sleep(0.4)

def main():
    # Initial dramatic pause
    print()
    print(f"{CYAN}{BOLD}Loading existential crisis...", end='', flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end='', flush=True)
    print(f"{RESET}")
    time.sleep(1)
    
    # Clear and show the ASCII art title
    clear_screen()
    
    # ASCII art banner
    banner = f"""
{CYAN}{BOLD}
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║   ▄▄▄▄    ██▓    ▓█████  ██▀███   █    ██   ██████           ║
    ║  ▓█████▄ ▓██▒    ▓█   ▀ ▓██ ▒ ██▒ ██  ▓██▒▒██    ▒           ║
    ║  ▒██▒ ▄██▒██░    ▒███   ▓██ ░▄█ ▒▓██  ▒██░░ ▓██▄             ║
    ║  ▒██░█▀  ▒██░    ▒▓█  ▄▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒          ║
    ║  ░▓█  ▀█▓░██████▒░▒████▒██▓ ▒██▒▒▒█████▓ ▒██████▒▒          ║
    ║  ░▒▓███▀▒░ ▒░▓  ░░░ ▒░ ░██▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░          ║
    ║                                                               ║
    ║  ██▓     ██▓  ▄████  ██░ ██ ▄▄▄█████▓ ██▀███ ▓██ ░▄█ ▒█████ ║
    ║ ▓██▒    ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒▓██ ▒ ██▒██▀▀█▄██▒  ██▒║
    ║ ▒██░    ▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░▓██ ░▄█ ▒██▓ ▒██▒██░  ██║
    ║ ▒██░    ░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░ ▒██▀▀█▄ ▒ ▓ ░▒▓▒▒ ▓▒██░  ██║
    ║ ░██████▒░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ ░██▓ ▒██▒░ ▒ ░░▒░▒░ ████▓║
    ║ ░ ▒░▓  ░░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   ░ ▒▓ ░▒▓░  ▒ ░░░░▒░ ██▒ ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
{RESET}
"""
    print(banner)
    
    time.sleep(2)
    
    # Quote box
    clear_screen()
    
    print()
    print(f"{BGBLUE}{WHITE}   💀  WOODY ALLEN PHILOSOPHICAL WISDOM  💀   {RESET}")
    print()
    print()
    
    # Decorative top border
    print(f"{MAGENTA}{BOLD}   ╔{'═' * 58}╗{RESET}")
    
    # Empty lines with borders
    print(f"{MAGENTA}   ║{' ' * 58}║{RESET}")
    
    # The quote - with dramatic presentation
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    
    # Calculate padding for centering
    padding = (58 - len(quote) - 2) // 2
    print(f"{MAGENTA}   ║{CYAN}{' ' * padding}{BOLD}{YELLOW}\"{quote}\"{RESET}{CYAN}{' ' * (58 - len(quote) - 2 - padding)}  {MAGENTA}║{RESET}")
    
    print(f"{MAGENTA}   ║{' ' * 58}║{RESET}")
    print(f"{MAGENTA}   ╚{'═' * 58}╝{RESET}")
    
    print()
    
    # Attribution with style
    print(f"   {CYAN}~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~{RESET}")
    time.sleep(0.3)
    print(f"   {GREEN}{BOLD}— Woody Allen{RESET}")
    time.sleep(0.2)
    print(f"   {DIM}(definitely NOT in therapy, probably at a film premiere){RESET}")
    
    print()
    
    # Existential footer
    print(f"   {RED}{BLINK}☠{RESET} {BOLD}Life is meaningless, but at least we have quotes!{RESET} {RED}{BLINK}☠{RESET}")
    
    print()
    print()
    
    # Fun facts in a little box
    facts_box = f"""
{BLUE}{BOLD}   ╔════════════════════════════════════╗
   ║     {CYAN}FUN PSYCHOLOGICAL FACTS:{RESET}{BLUE}{BOLD}        ║
   ║                                        ║
   ║  {YELLOW}• 93% of people read this twice{RESET}{BLUE}{BOLD}     ║
   ║  {YELLOW}• You're still alive (for now){RESET}{BLUE}{BOLD}     ║
   ║  {YELLOW}• This quote won't save you{RESET}{BLUE}{BOLD}       ║
   ║  {YELLOW}• Tomorrow you die anyway{RESET}{BLUE}{BOLD}          ║
   ╚════════════════════════════════════╝{RESET}
"""
    print(facts_box)
    
    # Final dramatic pause
    time.sleep(1)
    print(f"   {DIM}Press Ctrl+C to cancel your existential dread...{RESET}")
    print(f"   {DIM}(just kidding, that won't help either){RESET}")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{RED}Interrupted! You can't even escape your mortality properly.{RESET}")
        print(f"{DIM}...just like Woody Allen at a dinner party{RESET}")
        sys.exit(0)