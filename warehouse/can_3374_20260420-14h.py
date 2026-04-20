"""
Campbell's Soup Can #3374
Produced: 2026-04-20 14:12:46
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
=================================================
A neurosis-powered existential experience in terminal form.
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
    GREY = '\033[90m'
    BG_YELLOW = '\033[43m'
    BG_CYAN = '\033[46m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_animation(text, delay=0.05, color=Colors.CYAN):
    """Print text with a typing animation effect"""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def create_box(lines, width=70):
    """Create a fancy box around text"""
    border = Colors.YELLOW + "═" * (width - 2) + Colors.RESET
    return border

def main():
    # The Woody Allen quote
    quote = (
        "I'm not afraid of death—I've been dead once and it was just "
        "a Tuesday. The real terror is realizing I've spent 47 years "
        "avoiding my therapist's calls and I'm still not sure if I'm "
        "the protagonist or just the background character in someone "
        "else's mediocre existential comedy."
    )
    
    author = "— Woody Allen (probably)"
    
    # ASCII art header
    ascii_art = f"""
{Colors.MAGENTA}
        ████████╗ █████╗ ██████╗ ████████╗    ██████╗  █████╗ ██████╗  █████╗ ██████╗  ██████╗ 
        ╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝   ██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔═══██╗
           ██║   ███████║██████╔╝   ██║      ██║   ██║███████║██████╔╝███████║██████╔╝██║   ██║
           ██║   ██╔══██║██╔══██╗   ██║      ██║   ██║██╔══██║██╔══██╗██╔══██║██╔══██╗██║   ██║
           ██║   ██║  ██║██║  ██║   ██║      ╚██████╔╝██║  ██║██║  ██║██║  ██║██║  ██║╚██████╔╝
           ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ 
{Colors.RESET}
    """
    
    clear_screen()
    
    # Print title with animation
    print(ascii_art)
    time.sleep(0.3)
    
    # Decorative top border
    print(f"\n{Colors.YELLOW}{'▓' * 40}{Colors.RESET}")
    print(f"{Colors.YELLOW}▓{Colors.RESET}" + " " * 38 + f"{Colors.YELLOW}▓{Colors.RESET}")
    
    # Quote with animation
    print(f"{Colors.YELLOW}▓{Colors.RESET}  ", end="")
    print_with_animation(quote, delay=0.03, color=Colors.CYAN)
    
    # Space for author
    print(f"{Colors.YELLOW}▓{Colors.RESET}" + " " * 38 + f"{Colors.YELLOW}▓{Colors.RESET}")
    
    # Author with different color
    print(f"    {Colors.GREEN}{Colors.BOLD}{author}{Colors.RESET}")
    
    # Bottom border
    print(f"{Colors.YELLOW}▓{Colors.RESET}" + " " * 38 + f"{Colors.YELLOW}▓{Colors.RESET}")
    print(f"{Colors.YELLOW}{'▓' * 40}{Colors.RESET}")
    
    # Footer with philosophical musing
    print(f"\n{Colors.GREY}{Colors.ITALIC}* This quote brought to you by anxiety, coffee, and existential dread.{Colors.RESET}")
    print(f"{Colors.GREY}{Colors.ITALIC}* Side effects may include: overthinking, apologizing to furniture, and existential laughter.{Colors.RESET}\n")
    
    # Blinking cursor effect for fun
    for _ in range(3):
        sys.stdout.write(f"{Colors.YELLOW}█{Colors.RESET}   ")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write(f"\b\b\b   \b\b\b")
        sys.stdout.flush()
        time.sleep(0.2)
    
    print(f"\n{Colors.CYAN}Thanks for visiting the void. Come again soon (or don't—I'm not your therapist).{Colors.RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Ah, you too prefer the exit? How very Woody Allen of you.{Colors.RESET}")