"""
Campbell's Soup Can #1900
Produced: 2026-01-28 09:48:38
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random
from itertools import cycle

def woody_allen_quote():
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'
    
    # Woody Allen style quote
    quote = """I'm not afraid of death; I just don't want to be there when it happens.
It's like being at a really bad party - you know you have to leave eventually,
but you'd rather just slip out the back door when no one's looking.
But death? Death doesn't have a back door. It's more like that one host
who insists you stay until the bitter end, talking about their vacation
photos while slowly draining your will to live. I've tried everything -
pretending I'm allergic to existence, claiming I have a prior engagement
with non-existence, even suggesting we reschedule for next Tuesday.
But death is the worst kind of date: punctual and impossible to cancel."""
    
    # ASCII art frames for animation
    frames = [
        ["⚪⚪⚪⚪⚪", "⚪⚪⚪⚪⚪", "⚪⚪⚪⚪⚪", "⚪⚪⚪⚪⚪", "⚪⚪⚪⚪⚪"],
        ["⚪⚫⚪⚪⚪", "⚪⚪⚫⚪⚪", "⚪⚪⚪⚫⚪", "⚪⚪⚪⚪⚫", "⚪⚪⚪⚪⚪"],
        ["⚫⚫⚫⚫⚫", "⚫⚪⚫⚪⚫", "⚫⚪⚫⚪⚫", "⚫⚪⚫⚪⚫", "⚫⚫⚫⚫⚫"],
        ["⚪⚫⚪⚪⚪", "⚪⚪⚫⚪⚪", "⚪⚪⚪⚫⚪", "⚪⚪⚪⚪⚫", "⚪⚪⚪⚪⚪"],
        ["⚪⚪⚪⚪⚪", "⚪⚪⚪⚪⚪", "⚪⚪⚪⚪⚪", "⚪⚪⚪⚪⚪", "⚪⚪⚪⚪⚪"]
    ]
    
    # Color cycle
    colors = cycle([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN])
    
    # Clear screen
    print("\033[H\033[J", end="")
    
    # Title
    title = "WOODY ALLEN: A PHILOSOPHICAL PERSPECTIVE"
    print(f"\n{BLUE}{BOLD}{title:^80}{END}\n")
    
    # Animated header
    for frame in frames * 3:
        for row in frame:
            color = next(colors)
            print(f"{color}{''.join(row):^80}{END}")
            time.sleep(0.05)
    
    # Print the quote with typewriter effect
    words = quote.split()
    sys.stdout.write("\n\n")
    for word in words:
        color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE])
        sys.stdout.write(f"{color}{word} {END}")
        sys.stdout.flush()
        time.sleep(0.05)
    
    # Add some philosophical symbols
    symbols = ["🤔", "😟", "🙈", "🙉", "🙊", "🎭", "🎬"]
    print("\n\n")
    for i in range(20):
        symbol = random.choice(symbols)
        color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN])
        print(f"{color}{symbol:^5}{END}", end="")
        time.sleep(0.1)
    
    # Sign off
    print(f"\n\n{BOLD}{YELLOW}-- Woody Allen (probably){END}")
    print(f"\n{BOLD}{CYAN}(Analysis by a neurotic AI){END}\n")

if __name__ == "__main__":
    woody_allen_quote()