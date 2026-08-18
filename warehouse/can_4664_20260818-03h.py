"""
Campbell's Soup Can #4664
Produced: 2026-08-18 03:08:25
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

def slow_print(text, delay=0.03):
    """Print text character by character with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animated_quote():
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    # Clear screen
    print('\033[2J\033[H', end='')
    
    # ASCII art frame
    frame = f"""
    {CYAN}╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║   {YELLOW}╔═╗╔═╗╔═╗╔╦╗  ╦  ╦╔╗╔╔╦╗╦  ╦╔╗╔╔╦╗  ╔╦╗╦╔╦╗╦╔╗╔╦  ╦╔═╗╔╦╗{RESET}   ║
    ║   {YELLOW}╠═╣║╣ ║╣ ║║║  ║  ║║║║ ║ ╠╩╗║║║║ ║   ║║║║ ║ ║║║║║  ║╠═╣ ║{RESET}       ║
    ║   {YELLOW}╩ ╩╚═╝╚═╝╩ ╩  ╩═╝╩╝╚╝ ╩ ╩ ╩╩╝╚╝ ╩   ╩ ╩╩ ╩ ╩╝╚╝╩═╝╩╚═╝ ╩{RESET}       ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝{RESET}
    """
    
    slow_print(frame, 0.005)
    time.sleep(0.5)
    
    # Philosophical Woody Allen style quote
    quote_lines = [
        f"{MAGENTA}    I've been thinking about mortality lately.",
        "    Not constantly—no, that would be excessive,",
        "    but periodically, like a cosmic reminder",
        "    that pops up between checking my email.",
        "",
        "    Death and I have a complicated relationship.",
        "    I don't fear it, exactly—like a bad date",
        "    I'd rather avoid—but I definitely don't",
        "    want to RSVP 'yes' when it knocks.",
        "",
        "    The universe is a vast, indifferent place",
        "    that probably doesn't care if I exist,",
        "    which is comforting—I never asked to be",
        "    existentially concerned in the first place!",
        "",
        f"    In fact, I'm planning my immortality",
        "    through strategic avoidance of dangerous activities,",
        "    like jogging, social gatherings, and thinking",
        "    too deeply about the heat death of the universe.",
        "",
        "    Because if I'm going to face oblivion, I'd prefer",
        "    to do it while comfortably anxious on my couch,",
        "    watching documentaries about pigeons,",
        "    rather than heroically in some dramatic moment",
        "    that would look good on a commemorative t-shirt.{RESET}"
    ]
    
    for line in quote_lines:
        if line.strip() == "":
            time.sleep(0.3)
            print(line)
        else:
            slow_print(line, 0.02)
        time.sleep(0.1)
    
    # Animated closing
    time.sleep(1)
    closing = f"\n{BOLD}{BLUE}    — Anonymous Neurotic Philosopher{RESET}"
    slow_print(closing, 0.05)
    
    # Pulsing dots effect
    for _ in range(3):
        for i in range(3):
            dots = "." * i
            sys.stdout.write(f"\r{YELLOW}    contemplating existence{dots}{' ' * 5}{RESET}")
            sys.stdout.flush()
            time.sleep(0.4)
    print()

if __name__ == "__main__":
    try:
        animated_quote()
    except KeyboardInterrupt:
        print("\nEven my exit is interrupted—typical.")
        sys.exit(0)