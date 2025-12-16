"""
Campbell's Soup Can #969
Produced: 2025-12-16 10:43:44
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody Allen's Existential Wisdom Generator
# A neurotic philosophical quote, delivered with style

import sys
import time
from random import choice

def print_slowly(text, delay=0.03):
    """Type-writer effect for dramatic delivery"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def draw_therapy_couch():
    """ASCII art of a therapy couch - very Woody"""
    couch = """
    ╭─────────────────────────────────────────────╮
    │   ╭──────╮  ╭──────╮  ╭──────╮  ╭──────╮   │
    │  (  ☁️   )(  ☁️   )(  ☁️   )(  ☁️   )  │
    │   ╰──────╯  ╰──────╯  ╰──────╯  ╰──────╯   │
    ╰─────────────────────────────────────────────╯
    """
    print(couch)

def main():
    # Color codes for neurotic flair
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    # Woody Allen style quotes (neurotic, funny, existential)
    quotes = [
        "I don't mind dying, I just don't want to be there when it happens. Hospitals have terrible food.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon. Also, my back hurts.",
        "I'm not afraid of death; I just don't want to be there when it happens. And I'm definitely not ready.",
        "The universe is expanding? Great, more space to feel insignificant in!",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying. And frequent check-ups.",
        "My therapist has problems with her therapist. It's a whole thing.",
        "I'm at two with nature, and neither of us is winning.",
        "Eternity is very long, especially near the end. And the middle. And the beginning. Mostly the beginning.",
        "I broke up with my girlfriend because she was two-dimensional. Flat affect, you understand.",
        "The food here is terrible, and the portions are so small. Much like my self-esteem!",
        "I took a speed-reading course. Now I can read War and Peace in twenty minutes. It's about Russia.",
        "I'm not neurotic, I'm just realistically pessimistic about everything all the time.",
        "My mother had a diet that consisted of food and regret. We bonded over second helpings of both.",
        "I don't suffer from existential dread, I just have an acute awareness that we're all hurtling through space on a dying rock."
    ]
    
    # Choose a random Woody-esque quote
    quote = choice(quotes)
    
    # Print header with anxiety-inducing countdown
    print(f"\n{BOLD}{RED}╔══════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{RED}║           WOODY ALLEN'S EXISTENTIAL          ║{RESET}")
    print(f"{BOLD}{RED}║             WISDOM GENERATOR                 ║{RESET}")
    print(f"{BOLD}{RED}╚══════════════════════════════════════════════╝{RESET}\n")
    
    print(f"{CYAN}Analyzing your existential dread...{RESET}")
    time.sleep(0.5)
    
    print(f"{YELLOW}Calculating mortality rate...{RESET}")
    time.sleep(0.5)
    
    print(f"{MAGENTA}Reviewing therapy bills...{RESET}")
    time.sleep(0.5)
    
    print(f"{GREEN}Generating appropriate neurosis...{RESET}")
    time.sleep(0.5)
    
    # Draw the therapy couch
    print(f"\n{BLUE}")
    draw_therapy_couch()
    print(RESET)
    
    # Print the quote with dramatic typing
    print(f"{BOLD}{RED}Woody says:{RESET}\n")
    print(f"{YELLOW}╔══════════════════════════════════════════════╗{RESET}")
    print(f"{YELLOW}║{RESET}", end="")
    print_slowly(f" {quote}", 0.04)
    print(f" {YELLOW}║{RESET}")
    print(f"{YELLOW}╚══════════════════════════════════════════════╝{RESET}\n")
    
    # Add a post-therapy session tagline
    print(f"{CYAN}Remember: 90% of life is just showing up.{RESET}")
    print(f"{CYAN}The other 10% is wondering why you bothered.{RESET}\n")
    
    # Blink effect for the final line
    for i in range(3):
        sys.stdout.write(f"\r{RED}Don't worry. {RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write(f"\r{BLUE}Be happy! {RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write(f"\r{MAGENTA}It's pointless! {RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
    sys.stdout.write(f"\r{GREEN}Anyway, what do I know?{RESET}\n\n")

if __name__ == "__main__":
    main()