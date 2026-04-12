"""
Campbell's Soup Can #3256
Produced: 2026-04-12 13:35:09
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
🍿 Woody Allen Wisdom Generator 🍿
A neurotic, existential experience in terminal form
"""

import sys
import time
import os

# ANSI Color Codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Foreground colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Background colors
    BG_RED = '\033[41m'
    BG_YELLOW = '\033[43m'
    BG_CYAN = '\033[46m'
    BG_MAGENTA = '\033[45m'
    BG_BLACK = '\033[40m'

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Typing effect
def type_text(text, color=Colors.CYAN, delay=0.03):
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Animated box drawing
def draw_box(lines, color=Colors.YELLOW):
    max_len = max(len(line) for line in lines)
    border = '┌' + '─' * (max_len + 2) + '┐'
    bottom = '└' + '─' * (max_len + 2) + '┘'
    
    print(color + border + Colors.RESET)
    for line in lines:
        padding = ' ' * (max_len - len(line))
        print(color + '│ ' + Colors.RESET + line + padding + color + ' │' + Colors.RESET)
    print(color + bottom + Colors.RESET)

# Spinning character animation
def spin(char, delay=0.1):
    chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    for c in chars:
        print(f"\r{Colors.MAGENTA}{c} Contemplating existence...{Colors.RESET}", end='', flush=True)
        time.sleep(delay)
    print(f"\r{' ' * 30}", end='\r')

def main():
    clear_screen()
    
    # ASCII Art Header
    header = f"""
{Colors.YELLOW}
     ▄████ ▓█████  ███▄    █ ▓█████   ██████  ██▓  ██████ 
    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▒██    ▒ ▓██▒▒██    ▒ 
   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ░ ▓██▄   ▒██▒░ ▓██▄   
   ░▓█  ██▓▒▓█  ▄▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒░██░  ▒   ██▒
   ░▒▓███▀▒░▒████▒██░   ▓██░░▒████▒▒██████▒▒░██░▒██████▒▒
    ░▒   ▒ ░░ ▒░ ░▒░    ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░░▒  ▒ ▒▓▒ ▒ ░
{Colors.RESET}
"""
    print(header)
    
    # Loading animation
    print(f"\n{Colors.DIM}Initializing existential crisis...{Colors.RESET}")
    for _ in range(3):
        spin(0.08)
    print()
    
    # The Quote
    quote = "I'm not afraid of death — I'm just upset that I'll miss the ending of whatever show I'm currently binging."
    
    # Box with the quote
    quote_lines = [
        " " * 10 + "🎬 WOODY ALLEN'S DAILY EXISTENTIAL MOMENT 🎬",
        "",
        f"  \"{quote}\"",
        "",
        "  ~ Woody Allen (probably, while procrastinating)"
    ]
    
    print()
    draw_box(quote_lines, Colors.CYAN)
    
    # Footer with more ASCII art
    print(f"""
{Colors.MAGENTA}
                  ════════════════════════════════════
                      🦋 BUTTERFLY OF MEANING 🦋
                  ════════════════════════════════════
{Colors.RESET}
""")
    
    # Typing some additional commentary
    print(f"\n{Colors.GREEN}Philosophical Pondering:{Colors.RESET}")
    type_text("  Life is like a bag of chips...", delay=0.05)
    type_text("  You reach in, not knowing what you'll get...", delay=0.05)
    type_text("  And then you realize it's just Doritos...", delay=0.05)
    type_text("  And you're still hungry for meaning.", delay=0.05)
    
    print(f"\n{Colors.YELLOW}{Colors.BOLD}✨ Thanks for attending my TED Talk on Doing Nothing ✨{Colors.RESET}")
    
    print(f"""
{Colors.RED}
    ╔══════════════════════════════════════════════════╗
    ║  Remember: You're not lazy, you're on a deep       ║
    ║  intellectual journey to find the meaning of       ║
    ║  why you're watching Netflix instead of doing      ║
    ║  that thing you were supposed to do.                ║
    ╚══════════════════════════════════════════════════╝
{Colors.RESET}
""")

if __name__ == "__main__":
    main()