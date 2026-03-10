"""
Campbell's Soup Can #2687
Produced: 2026-03-10 19:08:53
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
RESET = "\033[0m"BOLD = "\033[1m"RED = "\033[91m"YELLOW = "\033[93m"BLUE = "\033[94m"MAGENTA = "\033[95m"CYAN = "\033[96m"WHITE = "\033[97m"PURPLE = "\033[35m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_print(text, color=RESET, delay=0.03):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)

def animate_stars():
    stars = ["*", "**", "***", "**", "*"]
    for _ in range(3):
        for star in stars:
            print(f"\r{CYAN}{BOLD} {star} {RESET}", end="")
            sys.stdout.flush()
            time.sleep(0.2)
    print()

def main():
    clear_screen()
    
    # Animated intro
    animate_stars()
    typewriter_print("Woody Allen's Neurotic Wisdom", MAGENTA, 0.04)
    animate_stars()
    print()
    
    # ASCII art frame
    frame_top = f"{YELLOW}╔{'═' * 60}╗{RESET}"
    frame_mid = f"{YELLOW}║{RESET}{' ' * 60}{YELLOW}║{RESET}"
    frame_bot = f"{YELLOW}╚{'═' * 60}╝{RESET}"
    
    quote = "I finally figured out the meaning of life—it's just God's cruel joke where we all spend eternity worrying about sex, death, and whether the bagel place opens on time."
    
    print(frame_top)
    
    # Center the quote with colors
    lines = []
    for i in range(0, len(quote), 55):
        line = quote[i:i+55].strip()
        colored_line = f"{YELLOW}║{RESET}  {WHITE}{BOLD}{line.ljust(55)}{RESET}{YELLOW}║{RESET}"
        lines.append(colored_line)
    
    for line in lines:
        print(line)
    
    # Fill remaining space
    remaining = 14 - len(lines)
    for _ in range(remaining):
        print(frame_mid)
    
    print(frame_bot)
    print()
    
    # Neurotic footer
    typewriter_print("(Don't worry, it's probably wrong...)", PURPLE, 0.05)
    print(f"\n{RED}{BOLD}Press Enter to existential crisis...{RESET}")

if __name__ == "__main__":
    try:
        main()
        input()
    except KeyboardInterrupt:
        print(f"\n{RESET}Existence terminated.")