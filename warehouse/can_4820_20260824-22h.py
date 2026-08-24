"""
Campbell's Soup Can #4820
Produced: 2026-08-24 22:44:42
Worker: Google: Nano Banana Pro (Gemini 3 Pro Image Preview) (google/gemini-3-pro-image-preview)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI Escape Codes for terminal styling
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

# Foreground Colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Background Colors
BG_BLACK = "\033[40m"

# The Philosophical Quote
QUOTE = """I often wonder if my existence has any deeper meaning. 
Then I remember I spent forty-five minutes this morning 
paralyzed with indecision over two identical pairs of beige socks."""
AUTHOR = "- A Neurotic Philosopher (probably)"

def slow_type(text, color=WHITE, speed=0.04, newline=True, style=""):
    """Prints text with a retro typewriter effect."""
    sys.stdout.write(style + color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Add a tiny bit of randomness to the typing speed for realism
        time.sleep(random.uniform(speed * 0.8, speed * 1.2))
    sys.stdout.write(RESET)
    if newline:
        print()

def nervous_pause():
    """Simulates a nervous hesitation."""
    print()
    sys.stdout.write(DIM + "      (nervous shuffling) " + RESET)
    for _ in range(3):
        sys.stdout.write(DIM + "." + RESET)
        sys.stdout.flush()
        time.sleep(0.6)
    print()
    print()

def print_decorated_quote():
    """Prints the quote inside a visually interesting ASCII box."""
    lines = QUOTE.split('\n')
    max_len = max(len(line) for line in lines)
    box_width = max_len + 8
    
    border_color = CYAN + BOLD
    text_color = YELLOW + ITALIC
    
    # Top Border
    print(border_color + "  +" + "~" * box_width + "+  " + RESET)
    print(border_color + "  |  " + BG_BLACK + " " * box_width + RESET + border_color + "  |  " + RESET)

    # Quote Content
    for line in lines:
        centered_line = line.center(box_width)
        print(border_color + "  |  " + BG_BLACK + text_color + centered_line + RESET + border_color + "  |  " + RESET)
        
    # Author Section
    print(border_color + "  |  " + BG_BLACK + " " * box_width + RESET + border_color + "  |  " + RESET)
    author_line = AUTHOR.rjust(box_width - 2)
    print(border_color + "  |  " + BG_BLACK + MAGENTA + "  " + author_line + RESET + border_color + "  |  " + RESET)
    
    # Bottom Border
    print(border_color + "  |  " + BG_BLACK + UNDERLINE + " " * box_width + RESET + border_color + "  |  " + RESET)
    print(border_color + "  +" + "~" * box_width + "+  " + RESET)

# --- Main Performance ---
print('\n' * 2)

# Introduction
slow_type("(A small, disheveled figure approaches a lonely microphone...)", color=DIM, speed=0.06)
time.sleep(1)
slow_type("Ahem.", color=RED, speed=0.1, style=BOLD)
time.sleep(0.5)
slow_type("Testing, testing. Is this thing on?", color=BLUE)
nervous_pause()

# Build-up
slow_type("You know, people always ask me about the nature of reality.", color=WHITE)
time.sleep(0.5)
slow_type("They say, 'What's it all about?'", color=WHITE)
time.sleep(0.8)
slow_type("And I tell them...", color=WHITE, speed=0.1)
time.sleep(0.5)

print('\n')

# The Quote Reveal
print_decorated_quote()

print('\n')

# Outro
time.sleep(1)
slow_type("Anyway.", color=GREEN)
time.sleep(0.5)
slow_type("I think I left my anxiety running. I should go catch it.", color=GREEN)
slow_type("(scurries off stage)", color=DIM, speed=0.08)
print('\n' * 2)