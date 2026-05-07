"""
Campbell's Soup Can #3590
Produced: 2026-05-07 00:05:24
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
🎬 Woody Allen Style Philosophical Quote Generator 🎬
A neurotic, existential, self-deprecating masterpiece in terminal form.
"""

import sys
import time
import os

# ANSI Color Codes
class Colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BG_YELLOW = '\033[43m'
    BG_CYAN = '\033[46m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.05):
    """Print text slowly for dramatic effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def woody_allen_quote():
    """The masterpiece quote"""
    return """I've finally figured out the meaning of life - 
    it's a four-letter word that starts with 't' and ends with 'me'.
    Actually, wait... I think that was a typo. 
    The real meaning of life is realizing you're going to die 
    and then spending the rest of your short existence 
    worrying about whether you left the stove on.
    
    I asked a philosopher what the meaning of life was.
    He said, 'That's a 50 euro question.'
    I said, 'I'll give you 20 and a sandwich.'
    He said, 'The meaning of life is knowing your place in the universe.'
    I said, 'My place is on the couch, eating the sandwich.'
    
    And that's when I achieved enlightenment - 
    right before I spilled coffee on my existential crisis."""

def print_boxed_text(text, border_color=Colors.CYAN, text_color=Colors.WHITE):
    """Print text inside a fancy box"""
    lines = text.split('\n')
    max_width = max(len(line) for line in lines) + 4
    
    # Top border
    print(border_color + '┌' + '─' * max_width + '┐' + Colors.RESET)
    
    for line in lines:
        padding = max_width - len(line) - 2
        print(border_color + '│' + Colors.RESET + text_color + line + ' ' * padding + border_color + '│' + Colors.RESET)
    
    # Bottom border
    print(border_color + '└' + '─' * max_width + '┘' + Colors.RESET)

def main():
    clear_screen()
    
    # ASCII Art Header
    header = f"""
{Colors.MAGENTA}{Colors.BOLD}
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║      🎬  W O O D Y   A L L E N   Q U O T E  🎬             ║
    ║                                                           ║
    ║      "I'm not afraid of death, I'm just afraid             ║
    ║       it might happen while I'm watching a bad movie."     ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
{Colors.RESET}
"""
    print(header)
    time.sleep(0.5)
    
    # Loading animation
    print(f"\n{Colors.YELLOW}Loading existential crisis", end="")
    for _ in range(5):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(f" {Colors.GREEN}Complete!{Colors.RESET}\n")
    time.sleep(0.5)
    
    # The quote in a fancy box
    print(f"\n{Colors.CYAN}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}║{Colors.RESET} {Colors.ITALIC}{Colors.WHITE}And now, for my magnum opus...{Colors.RESET}" + " " * 35 + f"{Colors.CYAN}{Colors.BOLD}║{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}╚═══════════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    time.sleep(1)
    print()
    
    # Print the main quote with typewriter effect in a box
    print_boxed_text(woody_allen_quote(), border_color=Colors.YELLOW, text_color=Colors.WHITE)
    
    # Decorative footer
    print(f"""
{Colors.GREEN}
    ┌─────────────────────────────────────────────────────────────┐
    │  🦋  "The die is cast." - Julius Caesar (before he was  │    
    │      assassinated, probably by someone who was late to      │
    │      their therapy appointment)                            │
    └─────────────────────────────────────────────────────────────┘
{Colors.RESET}
    """)
    
    # Blinking cursor effect
    print(f"{Colors.RED}{Colors.ITALIC}Press Ctrl+C to exit and contemplate your mortality...{Colors.RESET}")
    
    # Keep terminal open (for Windows compatibility)
    try:
        input(f"\n{Colors.CYAN}Press Enter to existential crisis... ⟫ {Colors.RESET}")
    except (KeyboardInterrupt, EOFError):
        print(f"\n{Colors.MAGENTA}Even the exit was anticlimactic. How very Woody Allen.{Colors.RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()