"""
Campbell's Soup Can #2995
Produced: 2026-03-27 18:04:30
Worker: Perplexity: Sonar (perplexity/sonar)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI color codes
RED = "\033[91m"YELLOW = "\033[93m"BLUE = "\033[94m"PURPLE = "\033[95m"CYAN = "\033[96m"WHITE = "\033[97m"BOLD = "\033[1m"ITALIC = "\033[3m"RESET = "\033[0m"

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Woody Allen style quote: neurotic, self-deprecating, existential
QUOTE = "I don't fear the void of eternity... I just worry it'll be disappointed when it finds out who I really am."

def print_title():
    title = f"""{BOLD}{CYAN}
    ░██████╗░█████╗░██████╗░░█████╗░░█████╗░██████╗░░██████╗██████╗░░░
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗░░
    ╚█████╗░███████║██████╔╝███████║██║░░██║██████╔╝╚█████╗░██████╔╝░░
     ╚═══██╗██╔══██║██╔══██╗██╔══██║██║░░██║██╔══██╗░╚═══██╗██╔══██╗░░
    ██████╔╝██║░░██║██║░░██║██║░░██║██████╔╝██████╔╝██████╔╝██║░░██║░░
    ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚═════╝░╚═╝░░╚═╝░░
    {RESET}"""
    print(title)

def typewriter_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_stars():
    stars = ["*", "✦", "✧", "✩", "✪"]
    for _ in range(3):
        for star in stars:
            print(f"{PURPLE}{BOLD}         {star}  {RESET}", end="")
            sys.stdout.flush()
            time.sleep(0.2)
            sys.stdout.write("\b\b\b\b  \b\b\b\b")
        print()

# Main execution
clear_screen()
print_title()

print(f"{YELLOW}{BOLD}W{ITALIC}O{RESET}{YELLOW}{BOLD}O{ITALIC}D{RESET}{YELLOW}{BOLD}Y{ITALIC} {RESET}{YELLOW}{BOLD}A{ITALIC}L{RESET}{YELLOW}{BOLD}L{ITALIC}E{RESET}{YELLOW}{BOLD}N{ITALIC}'{RESET}{YELLOW}{BOLD}S{ITALIC} {RESET}{YELLOW}{BOLD}E{ITALIC}X{RESET}{YELLOW}{BOLD}I{ITALIC}S{RESET}{YELLOW}{BOLD}T{ITALIC}E{RESET}{YELLOW}{BOLD}N{ITALIC}T{RESET}{YELLOW}{BOLD}I{ITALIC}A{RESET}{YELLOW}{BOLD}L{ITALIC} {RESET}{YELLOW}{BOLD}C{ITALIC}R{RESET}{YELLOW}{BOLD}I{ITALIC}S{RESET}{YELLOW}{BOLD}I{ITALIC}S{RESET}")
print(f"{WHITE}╔══════════════════════════════════════════════════════════════╗{RESET}")

animate_stars()
typewriter_effect(f"{RED}{BOLD}{ITALIC}\"{QUOTE}\"{RESET}", 0.04)

print(f"{WHITE}╚══════════════════════════════════════════════════════════════╝{RESET}")
print()
print(f"{PURPLE}{BOLD}*neurotic existential dread served with a side of self-deprecation*{RESET}")

# Fade out effect
time.sleep(1)
for i in range(10, 0, -1):
    code = f"\033[3{i}m"    print(f"{code}          (fading into the existential void...){RESET}")
    time.sleep(0.1)
print(RESET)