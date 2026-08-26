"""
Campbell's Soup Can #4851
Produced: 2026-08-26 09:02:00
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
A neurotic, self-deprecating, existential experience in terminal form
"""

import sys
import time
import os

# ANSI Color Codes
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    DIM = "\033[2m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, delay=0.05, color=Colors.YELLOW):
    """Print text with a typewriter effect"""
    for char in text:
        print(f"{color}{char}{Colors.RESET}", end='', flush=True)
        time.sleep(delay)
    print()

def print_centered(text, color=Colors.CYAN):
    """Print text centered with color"""
    terminal_width = os.get_terminal_size().columns
    padding = (terminal_width - len(text)) // 2
    print(f"{color}{' ' * padding}{text}{Colors.RESET}")

def print_slowly(lines, delay=0.1):
    """Print lines with delay between them"""
    for line in lines:
        print(line)
        time.sleep(delay)

def main():
    clear_screen()
    
    # ASCII Art Header
    header = f"""{Colors.MAGENTA}
    ╔══════════════════════════════════════════════════════════════════╗
    ║                                                                  ║
    ║     ██╗  ██╗ ██████╗ ██╗  ██╗                                 ║
    ║     ██║  ██║██╔═████╗██║  ██║                                 ║
    ║     ███████║██║██╔██║███████║                                 ║
    ║     ╚════██║████╔╝██║╚════██║                                 ║
    ║          ██║╚██████╔╝     ██║                                 ║
    ║          ╚═╝ ╚═════╝      ╚═╝                                 ║
    ║                                                                  ║
    ║     ███████╗███████╗ ██████╗ █████╗ ██████╗ ███████╗            ║
    ║     ██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝            ║
    ║     █████╗  ███████╗██║     ███████║██████╔╝█████╗              ║
    ║     ██╔══╝  ╚════██║██║     ██╔══██║██╔═══╝ ██╔══╝              ║
    ║     ███████╗███████║╚██████╗██║  ██║██║     ███████╗            ║
    ║     ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝            ║
    ║                                                                  ║
    ╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}"""

    print(header)
    time.sleep(0.5)
    
    # Decorative line
    print(f"\n{Colors.CYAN}{'═' * 70}{Colors.RESET}\n")
    
    # Quote presentation
    print(f"{Colors.BOLD}{Colors.YELLOW}    A Profound Existential Meditation by Woody Allen:{Colors.RESET}\n")
    
    time.sleep(0.3)
    
    # The actual quote with typewriter effect
    quote = '"I\'ve been dating the same woman for forty years. I figure, if I stick' 
    quote2 = ' around long enough, she might respect me. Or at least die first.'
    quote3 = ' Either way, it\'s progress."'
    
    print(f"{Colors.WHITE}{Colors.BG_BLUE}  ┌{'─' * 60}┐  {Colors.RESET}")
    print(f"{Colors.WHITE}{Colors.BG_BLUE}  │{Colors.RESET}", end='')
    
    # Typewriter effect for the quote
    typewriter_effect(f"  {quote}", delay=0.04, color=Colors.BOLD + Colors.WHITE)
    typewriter_effect(f"  {quote2}", delay=0.04, color=Colors.BOLD + Colors.WHITE)
    typewriter_effect(f"  {quote3}", delay=0.04, color=Colors.BOLD + Colors.WHITE)
    
    print(f"{Colors.WHITE}{Colors.BG_BLUE}  └{'─' * 60}┘  {Colors.RESET}\n")
    
    time.sleep(0.3)
    
    # Attribution with animation
    attribution = "        — Woody Allen (from his upcoming film: 'Death Gets No Respect')"
    for char in attribution:
        print(f"{Colors.MAGENTA}{char}{Colors.RESET}", end='', flush=True)
        time.sleep(0.03)
    print("\n")
    
    # Philosophical analysis (simulated)
    analysis = [
        f"{Colors.DIM}    Analysis: This quote explores themes of:{Colors.RESET}",
        f"{Colors.DIM}      • The absurdity of romantic commitment{Colors.RESET}",
        f"{Colors.DIM}      • Male ego and mortality{Colors.RESET}",
        f"{Colors.DIM}      • The passage of time and regret{Colors.RESET}",
        f"{Colors.DIM}      • Jewish-American self-deprecation{Colors.RESET}",
    ]
    
    print_slowly(analysis, delay=0.15)
    
    time.sleep(0.3)
    
    # Decorative footer
    print(f"\n{Colors.CYAN}{'═' * 70}{Colors.RESET}")
    
    footer = f"""{Colors.YELLOW}
    ╭──────────────────────────────────────────────────────╮
    │  🎬 "I'm not afraid of death. I just don't want to   │
    │      be there when it happens."                     │
    │                                    — Woody Allen     │
    ╰──────────────────────────────────────────────────────╯
    {Colors.RESET}"""
    
    print(footer)
    
    # Final existential thought
    time.sleep(0.5)
    print(f"\n{Colors.ITALIC}{Colors.DIM}    (The meaning of life is left as an exercise for the reader){Colors.RESET}\n")
    
    print(f"{Colors.CYAN}{'═' * 70}{Colors.RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.MAGENTA}    Interrupted! Just like life itself...{Colors.RESET}\n")
        sys.exit(0)