"""
Campbell's Soup Can #809
Produced: 2025-12-09 04:42:44
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
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

# ANSI escape codes
YELLOW = "\033[93m"
CYAN = "\033[96m"
PINK = "\033[95m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
END = "\033[0m"
FLAME = "\033[38;2;255;69;0m"
STAR = "★"

def typewriter(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay if char not in [" ", "\n"] else 0.01)
    print()

def animate_stars(duration=2, speed=0.1):
    end_time = time.time() + duration
    while time.time() < end_time:
        print(f"{YELLOW}{STAR}{END}", end="", flush=True)
        time.sleep(speed)
    print()

print("\033[2J\033[H")  # Clear screen

# Header
print(f"{YELLOW}{' ' * 10}{BOLD}🌌 THE EXISTENTIAL COMEDY HOUR 🌌{END}")
animate_stars(1)

# Quote
quote = f"{ITALIC}I don't believe in an afterlife,{END}\n" \
        f"{ITALIC}but I'm bringing a change of underwear anyway.{END}"

box_width = 42
print(f"{CYAN}╔{'═' * box_width}╗{END}")
print(f"{CYAN}║{END}  {FLAME}✨{END}  {PINK}{quote.center(box_width - 6)}{END}  {FLAME}✨{END}  {CYAN}║{END}")
print(f"{CYAN}╚{'═' * box_width}╝{END}")

# Signature
time.sleep(1)
typewriter(f"\n{YELLOW}{' ' * 12}~ Woody Allen's Backup Plan ~{END}\n", 0.05)

# Twinkling stars finale
animate_stars(1.5)