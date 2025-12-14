"""
Campbell's Soup Can #931
Produced: 2025-12-14 16:38:41
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import os

# ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def typewriter_effect(text, delay=0.05, color=Colors.WHITE):
    """Print text with a typewriter effect"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Colors.END + '\n')
    sys.stdout.flush()

def print_ascii_frame(width=70):
    """Print an ASCII art frame"""
    corner = '+'
    horizontal = '-'
    vertical = '|'
    
    print(f"\n{Colors.CYAN}{corner}{horizontal * (width-2)}{corner}{Colors.END}")
    print(f"{Colors.CYAN}{vertical}{' ' * (width-2)}{vertical}{Colors.END}")
    
def print_centered_line(text, width=70, color=Colors.WHITE):
    """Print a line of text centered within a frame"""
    padding = (width - len(text) - 2) // 2
    print(f"{Colors.CYAN}|{Colors.END}{' ' * padding}{color}{text}{' ' * (width - len(text) - 2 - padding)}{Colors.CYAN}|{Colors.END}")
    print(f"{Colors.CYAN}{vertical}{' ' * (width-2)}{vertical}{Colors.END}")

def main():
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Title
    print_ascii_frame()
    print_centered_line("WOODY ALLEN ON LIFE", 70, Colors.YELLOW + Colors.BOLD)
    print_centered_line("", 70)
    print_centered_line("A Philosophical Meditation", 70, Colors.MAGENTA)
    print_ascii_frame()
    
    # Main quote with typewriter effect
    print("\n")
    typewriter_effect("   \"I tried to live a meaningful life, but I kept getting distracted", 0.03, Colors.WHITE)
    typewriter_effect("   by the existential dread and my crippling fear of commitment...", 0.03, Colors.WHITE)
    typewriter_effect("   mostly to happiness.\"", 0.03, Colors.WHITE)
    
    # Decorative elements
    print("\n")
    print_centered_line("✦ ✦ ✦ ✦ ✦", 70, Colors.CYAN)
    print_centered_line("", 70)
    
    # Secondary quote
    typewriter_effect("   - Woody Allen", 0.05, Colors.GREEN + Colors.BOLD)
    typewriter_effect("   (Probably, I'm not really sure)", 0.05, Colors.YELLOW)
    
    # Footer
    print("\n")
    print_ascii_frame()
    print_centered_line("Presented by the Neurotic Philosophy Society", 70, Colors.MAGENTA)
    print_centered_line("Est. 1972. We're still working on the by-laws.", 70, Colors.YELLOW)
    print_ascii_frame()
    
    # Animated footer
    print("\n")
    for i in range(3):
        print(f"{Colors.RED}{'*' * 20} END {'*' * 20}{Colors.END}")
        time.sleep(0.3)
        print(f"{' ' * 20} END {' ' * 20}")
        time.sleep(0.3)
    
    print("\n" + Colors.BLUE + Colors.BOLD + "Press Enter to exit your existential crisis..." + Colors.END)
    input()

if __name__ == "__main__":
    main()