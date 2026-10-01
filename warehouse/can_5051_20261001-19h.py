"""
Campbell's Soup Can #5051
Produced: 2026-10-01 19:31:53
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen's Philosophical Wisdom - Animated Edition
A neurotic journey through existential dread, served with a smile!
"""

import sys
import time

# ANSI color codes
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[36m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

def typewriter(text, delay=0.03):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_box(text_lines, color=Colors.CYAN):
    """Print text inside a decorative box"""
    max_len = max(len(line) for line in text_lines)
    border = "═" * (max_len + 4)
    
    print(f"{color}{border}{Colors.RESET}")
    for line in text_lines:
        padding = " " * (max_len - len(line))
        print(f"{color}║ {Colors.YELLOW}{line}{padding} {color}║{Colors.RESET}")
    print(f"{color}{border}{Colors.RESET}")

def animate_quote():
    """Main animation sequence"""
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Title
    title = f"{Colors.MAGENTA}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.RESET}"
    print(f"\n{title}")
    typewriter(f"{Colors.MAGENTA}║  {Colors.YELLOW}WOODY ALLEN'S PHILOSOPHICAL MOMENTS  {Colors.MAGENTA}║{Colors.RESET}", 0.05)
    print(f"{title}\n{Colors.RESET}")
    
    # ASCII Art quote bubble
    quote_art = r"""
           .--.
          /  o \
    .-._|      |_.
   /    \      /  \
  |  .---`----'---. |
  |  \             / |
   \  `---.____.-'  /
    `-.___.___..--'
"""
    print(f"{Colors.GREEN}{quote_art}{Colors.RESET}")
    
    time.sleep(1)
    
    # The quote
    quote_lines = [
        "I don't want to achieve immortality",
        "through my work...",
        "I want to achieve it through not dying.",
        "",
        "  — Woody Allen (probably thinking this",
        "while ordering a sandwich he'll never finish)",
    ]
    
    print_box(quote_lines, Colors.BLUE)
    
    print()
    time.sleep(1)
    
    # Existential commentary
    commentary = [
        f"{Colors.DIM}But wait, if I don't die,",
        "then I won't achieve immortality through not dying,",
        "because not dying means living forever,",
        "which means I'll never get the satisfaction of",
        "achieving anything, including immortality!",
        "It's like trying to clap with one hand...{RESET}",
        "or dating someone for 5 minutes without panicking.",
        "Speaking of which, I once went out with a woman...", 
        "actually, let me finish this existential crisis first.{RESET}"
    ]
    
    for line in commentary:
        color = Colors.CYAN if "..." in line else Colors.DIM
        typewriter(f"{color}{line}\n{Colors.RESET}", 0.02)
        time.sleep(0.3)
    
    print(f"\n{Colors.RED}{Colors.BOLD}"
          "☕ existential coffee not included ☕"
          f"{Colors.RESET}\n")

if __name__ == "__main__":
    animate_quote()