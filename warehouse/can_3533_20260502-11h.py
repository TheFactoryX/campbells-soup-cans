"""
Campbell's Soup Can #3533
Produced: 2026-05-02 11:59:54
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
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    BG_YELLOW = '\033[43m'
    BG_CYAN = '\033[46m'
    BG_MAGENTA = '\033[45m'

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.05):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def create_boxed_quote(quote, author="Woody Allen"):
    """Create a beautifully boxed quote with ASCII art."""
    
    # Calculate box width
    max_len = max(len(quote), len(f"— {author}"))
    width = max_len + 4
    
    # ASCII art header
    header = f"""
{Colors.CYAN}╔{'═' * (width + 2)}╗
║{Colors.YELLOW}{' ' * ((width - 22) // 2)}🎬 WOODY ALLEN SAYS 🎬{' ' * ((width - 22) // 2)}{Colors.CYAN}║
╚{'═' * (width + 2)}╝{Colors.RESET}
"""
    
    # The quote box
    quote_box = f"""
{Colors.MAGENTA}╔{'═' * (width + 2)}╗
║{Colors.WHITE} {Colors.BOLD}{quote}{Colors.RESET}{' ' * (width - len(quote) + 1)}║
║{Colors.CYAN} {Colors.ITALIC}{'— ' + author}{' ' * (width - len(author) - 2)}{Colors.RESET}║
╚{'═' * (width + 2)}╝{Colors.RESET}
"""
    
    return header + quote_box

def animated_intro():
    """Show an animated introduction."""
    frames = [
        "🤔",
        "😰", 
        "🤯",
        "😅",
        "🎬"
    ]
    
    print(f"\n{Colors.YELLOW}{Colors.BOLD}")
    for frame in frames:
        print(f"\r{frame} Preparing your existential experience...", end="", flush=True)
        time.sleep(0.3)
    print(f"{Colors.RESET}\n")

def main():
    # The Woody Allen quote
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens, "
        "because I'll probably be late and won't know what to wear."
    )
    
    # Clear screen for dramatic effect
    clear_screen()
    
    # Animated intro
    animated_intro()
    
    # Print decorative ASCII art
    ascii_art = f"""
{Colors.CYAN}
        ██████╗ ██████╗ ███████╗███╗   ██╗
        ██╔══██╗██╔══██╗██╔════╝████╗  ██║
        ██████╔╝██████╔╝█████╗  ██╔██╗ ██║
        ██╔═══╝ ██╔══██╗██╔══╝  ██║╚██╗██║
        ██║     ██║  ██║███████╗██║ ╚████║
        ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
        
        ██████╗ ███████╗ █████╗ ██████╗ 
        ██╔══██╗██╔════╝██╔══██╗██╔══██╗
        ██████╔╝█████╗  ███████║██║  ██║
        ██╔══██╗██╔══╝  ██╔══██║██║  ██║
        ██║  ██║███████╗██║  ██║██████╔╝
        ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ 
{Colors.RESET}
"""
    
    print(ascii_art)
    time.sleep(0.5)
    
    # Print the boxed quote
    print(create_boxed_quote(quote))
    
    # Add some philosophical footer
    footer = f"""
{Colors.GREEN}
    ┌─────────────────────────────────────────────┐
    │  💡 Life is full of misery, loneliness,     │
    │     and suffering - and it's all over         │
    │     much too soon. But hey, at least         │
    │     we have WiFi.                           │
    └─────────────────────────────────────────────┘
{Colors.RESET}
"""
    print(footer)
    
    # Blinking cursor effect
    print(f"\n{Colors.YELLOW}Press Ctrl+C to exit this existential crisis...{Colors.RESET}")
    
    # Fun blinking cursor animation
    cursor = "▌"
    for _ in range(10):
        print(f"\r{Colors.RED}{cursor}{Colors.RESET}", end="", flush=True)
        time.sleep(0.5)
        cursor = " " if cursor == "▌" else "▌"
    
    print(f"\n{Colors.CYAN}Thanks for playing! Now go procrastinate productively.{Colors.RESET} ✌️\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.MAGENTA}Ah, you too prefer the comfort of interruption over the agony of commitment. Wise choice.{Colors.RESET} 👋")