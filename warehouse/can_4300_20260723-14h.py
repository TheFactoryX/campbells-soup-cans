"""
Campbell's Soup Can #4300
Produced: 2026-07-23 14:32:11
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

# Woody Allen style philosophical quote
quote = "I'm not afraid of death; I just don't want to be there when it happens. It's so hard to die when you're busy worrying about dying."

# ANSI color codes
class C:
    R = '\033[91m'  # Red
    G = '\033[92m'  # Green
    Y = '\033[93m'  # Yellow
    B = '\033[94m'  # Blue
    M = '\033[95m'  # Magenta
    C = '\033[96m'  # Cyan
    W = '\033[97m'  # White
    K = '\033[90m'  # Black/Gray
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

def animate_text(text, color=C.Y, delay=0.02):
    """Type out text character by character"""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_box(content, border_color=C.C, text_color=C.Y, bg_color=C.K):
    """Print content in a decorative box"""
    lines = content.split('\n')
    max_len = max(len(line) for line in lines)
    
    # Top border
    print(f"{border_color}{'═' * (max_len + 4)}{C.RESET}")
    
    # Content lines
    for line in lines:
        padding = max_len - len(line)
        print(f"{border_color}║{C.RESET} {text_color}{C.BOLD}{line}{C.RESET}{' ' * padding} {border_color}║{C.RESET}")
    
    # Bottom border
    print(f"{border_color}{'═' * (max_len + 4)}{C.RESET}")

def main():
    # Clear screen effect
    print("\033[2J\033[H", end="")
    
    # Animated header
    print(f"{C.C}{C.BOLD}")
    print("╔═══════════════════════════════════════════════╗")
    print("║     A Philosophical Moment (Probably Wrong)    ║")
    print("╚═══════════════════════════════════════════════╝")
    print(f"{C.RESET}")
    
    time.sleep(0.5)
    
    # Animate the quote appearing
    print(f"\n{C.M}{C.BOLD}Loading profound existential contemplation...{C.RESET}")
    for i in range(3):
        dots = "." * (i + 1)
        print(f"\r{C.M}Loading profound existential contemplation{dots}     {C.RESET}", end="", flush=True)
        time.sleep(0.3)
    print("\n")
    
    # Print the quote in a beautiful box with colors
    print(f"{C.G}{C.BOLD} wisdom center: {C.R}death & anxiety division{C.G}{C.BOLD} {C.RESET}\n")
    
    print_box(quote, border_color=C.B, text_color=C.W)
    
    # Attributed to
    print(f"\n{C.DIM}           — Anonymous, probably still anxious{C.RESET}")
    
    # Final flourish
    print(f"\n{C.Y}{'~' * 50}{C.RESET}")
    print(f"{C.M}Remember: This quote may or may not exist.{C.RESET}")
    print(f"{C.R}The uncertainty is the point.{C.RESET}\n")

if __name__ == "__main__":
    main()