"""
Campbell's Soup Can #3391
Produced: 2026-04-21 21:05:18
Worker: Qwen: Qwen3 Max (qwen/qwen3-max)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

def typewriter_print(text, delay=0.03, color=WHITE):
    """Prints text with a typewriter effect and color"""
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_boxed_message(lines, border_color=YELLOW, text_color=WHITE):
    """Prints a message in a decorative box"""
    max_len = max(len(line) for line in lines)
    top_bottom = "█" * (max_len + 4)
    
    print(f"{border_color}{top_bottom}{RESET}")
    for line in lines:
        padding = " " * (max_len - len(line))
        print(f"{border_color}█ {text_color}{line}{padding}{border_color} █{RESET}")
    print(f"{border_color}{top_bottom}{RESET}")

def main():
    # Clear screen (works in most terminals)
    print("\033[2J\033[H", end="")
    
    # Woody Allen style quote
    quote = "I'm not saying I'm a hypochondriac, but my doctor has my will on speed dial."
    
    # Intro animation
    typewriter_print("Presenting a philosophical insight from the mind of...", delay=0.05, color=CYAN)
    time.sleep(0.5)
    
    # Name reveal with flair
    name_lines = [
        "    __        __   _                          _   _             ",
        "    \\ \\      / /__| | ___ ___  _ __ ___   ___| |_| |__   ___    ",
        "     \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ __| '_ \\ / _ \\   ",
        "      \\ V  V /  __/ | (_| (_) | | | | | |  __/ |_| | | |  __/   ",
        "       \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|\\__|_| |_|\\___|   ",
        "                                                                "
    ]
    
    for line in name_lines:
        print(f"{RED}{line}{RESET}")
        time.sleep(0.1)
    
    time.sleep(0.8)
    
    # Print the quote in a fancy box
    print("\n")
    quote_lines = [quote[i:i+50] for i in range(0, len(quote), 50)]
    print_boxed_message(quote_lines, border_color=MAGENTA, text_color=YELLOW)
    
    # Add some existential flair at the bottom
    time.sleep(1)
    typewriter_print("\n...and that's why I always carry antacids AND a will.", delay=0.04, color=GREEN)
    
    # Final philosophical flourish
    time.sleep(1.5)
    print(f"\n{BLUE}{BOLD}Existence is absurd... but at least my pharmacy gives me a loyalty card.{RESET}")
    
    # Random neurotic thought bubble
    neurotic_thoughts = [
        "Did I leave the oven on? Or was that my existential dread?",
        "My therapist charges more than my landlord. At least my landlord doesn't analyze my dreams.",
        "I'm not paranoid - I'm just aware that the universe is actively plotting against me.",
        "They say laughter is the best medicine. My HMO disagrees.",
        "I don't believe in an afterlife, but I've brought a change of underwear just in case."
    ]
    
    time.sleep(2)
    thought = random.choice(neurotic_thoughts)
    print(f"\n{WHITE}💭 {ITALIC if 'ITALIC' in locals() else ''}{thought}{RESET}")
    
    # Small ASCII art of a worried face
    time.sleep(1.5)
    worried_face = [
        "         .-'''-.         ",
        "        /       \\        ",
        "       |  o   o  |       ",
        "       |    _    |       ",
        "        \\  '---'  /      ",
        "         '._____.'       ",
        "    Existential dread level: MAX"
    ]
    
    for line in worried_face:
        print(f"{CYAN}{line}{RESET}")
        time.sleep(0.2)
    
    time.sleep(1)
    print(f"\n{RED}Don't worry... or do. Worrying is what I do best.{RESET}")

if __name__ == "__main__":
    main()