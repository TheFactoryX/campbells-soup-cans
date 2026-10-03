"""
Campbell's Soup Can #5057
Produced: 2026-10-03 01:58:12
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Woody Allen Style Philosophical Quote Printer
A neurotic existential crisis in pure Python form.
"""

import sys
import time
import random

# ANSI Color Codes
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

# Woody Allen-style quotes (neurotic, funny, existential)
QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "I don't have a split personality; I have been cured by one.",
    "I've had a lot of worries in my life, most of which never happened.",
    "My one regret is that I didn't become a serial killer; I don't even know how to start conversations.",
    "I was having such a terrible time I considered suicide, but it occurred to me I should hold on until the afterlife, because at least they can’t disappoint you there.",
    "I’m interested in the meaning of life, mainly because I want to figure out why I'm so worried about it.",
]

def type_effect(text, delay=0.03, color=Colors.YELLOW):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_boxed(text, width=60):
    """Print text inside an ASCII art box with colors."""
    # Top border
    print(f"{Colors.CYAN}{Colors.BOLD}{'':=<{width}}{Colors.RESET}")
    
    # Content lines
    lines = []
    current_line = ""
    for word in text.split():
        if len(current_line) + len(word) + 1 <= width - 4:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())
    
    # Print lines with alternating colors
    colors = [Colors.MAGENTA, Colors.YELLOW, Colors.GREEN, Colors.BLUE]
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        padding = width - len(line) - 4
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{Colors.CYAN}|{Colors.DIM}{' ' * left_pad}{Colors.RESET}", end="")
        for char in line:
            sys.stdout.write(f"{color}{char}{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(0.02)
        print(f"{Colors.CYAN}{Colors.DIM}{' ' * right_pad}|{Colors.RESET}")
    
    # Bottom border
    print(f"{Colors.CYAN}{Colors.BOLD}{'':-<{width}}{Colors.RESET}")

def print_ascii_art():
    """Print a philosophical Woody Allen ASCII art."""
    art = f"""
    {Colors.MAGENTA}         .--.    
         |o_o |    {Colors.YELLOW}'Here I am, a profound thought,
         |:_/ |    {Colors.GREEN} floating in the existential void...'
       {Colors.CYAN}  //   \ \   
      {Colors.BLUE} (|     | )  {Colors.RED}  But seriously, should I be worried
       {Colors.MAGENTA}__\\_\\_|_|_____{Colors.YELLOW} about this meeting with the void?
    {Colors.GREEN}     |___|____|   {Colors.DIM} (I checked my calendar and there's
    {Colors.RED}     _|_____|_    {Colors.CYAN} nothing scheduled today,
    {Colors.YELLOW}    /  O   O  \   {Colors.MAGENTA} so I guess I'm free?")
    {Colors.DIM}        \~(*)~/   
    {Colors.BLUE}         ----- 
    {Colors.CYAN}        | | | | {Colors.MAGENTA}  -- Woody Allen's Brain
    {Colors.RED}        | | | | {Colors.YELLOW}     (Neurotic Department)
    {Colors.GREEN}        |_| |_|
    """
    print(art)
    time.sleep(1)

def main():
    # Clear screen
    print('\033[2J\033[H', end='')
    
    # Print title
    title = " A Woody Allen-Style Existential Crisis "
    subtitle = " Presented in Pure Python Anxiety "
    
    print(f"\n{Colors.BOLD}{Colors.CYAN}")
    print("=" * 60)
    print(title.center(60))
    print(subtitle.center(60))
    print("=" * 60)
    print(Colors.RESET)
    
    time.sleep(1)
    
    # ASCII art intro
    print_ascii_art()
    
    # Pick a random quote
    quote = random.choice(QUOTES)
    
    # Dramatic pause
    print(f"\n{Colors.DIM}{'':^60}")
    type_effect("And now, for a profound philosophical insight...", 0.05, Colors.WHITE)
    print(f"{Colors.DIM}{'':^60}")
    time.sleep(1)
    
    # Print the quote in a box
    print_boxed(quote)
    
    # Footer
    time.sleep(1)
    print(f"\n{Colors.DIM}{'-' * 60}")
    type_effect("Thank you. I'll be here all week. Try the veal.", 0.07, Colors.MAGENTA)
    print(f"{Colors.DIM}{'-' * 60}")

if __name__ == "__main__":
    main()