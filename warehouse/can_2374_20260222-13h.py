"""
Campbell's Soup Can #2374
Produced: 2026-02-22 13:12:59
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
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

# ANSI color codes
COLORS = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'BLUE': '\033[94m',
    'MAGENTA': '\033[95m',
    'CYAN': '\033[96m',
    'RESET': '\033[0m',
    'BOLD': '\033[1m'
}

def print_slow(text, delay=0.02, color=COLORS['YELLOW']):
    for char in text:
        sys.stdout.write(color + char + COLORS['RESET'])
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
    print()

def clear_screen():
    print("\033[H\033[J", end="")

def main():
    clear_screen()
    
    # Generate a unique Woody Allen-style quote
    quote = (
        "I've decided that life is just one big cosmic typo. "
        "I keep waiting for the universe to hit 'undo', but all I get is "
        "a '404: Meaning Not Found' error. At least my anxiety has meaning—"
        "it's the only thing keeping me from realizing I'm already dead."
    )
    
    # Create a "neurotic" ASCII frame with random jitter
    frame = [
        "  ┌──────────────────────────────────────────────────┐  ",
        "  │                                                  │  ",
        "  │                                                  │  ",
        "  │                                                  │  ",
        "  │                                                  │  ",
        "  │                                                  │  ",
        "  │                                                  │  ",
        "  │                                                  │  ",
        "  │                                                  │  ",
        "  │                                                  │  ",
        "  │                                                  │  ",
        "  └──────────────────────────────────────────────────┘  "
    ]
    
    # Add jitter to frame for "neurotic" effect
    jittered_frame = []
    for line in frame:
        jitter = random.randint(0, 2)
        jittered_frame.append(" " * jitter + line[jitter:])
    
    # Print the frame with neurotic shaking
    for _ in range(3):
        for line in jittered_frame:
            sys.stdout.write(COLORS['CYAN'] + line + COLORS['RESET'] + "\r")
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.1)
    
    # Print the quote with typewriter effect
    print("\033[12;10H" + COLORS['CYAN'] + "│" + COLORS['RESET'], end="")
    print_slow(quote[0:45], 0.05)
    print("\033[13;10H" + COLORS['CYAN'] + "│" + COLORS['RESET'], end="")
    print_slow(quote[45:90], 0.05)
    print("\033[14;10H" + COLORS['CYAN'] + "│" + COLORS['RESET'], end="")
    print_slow(quote[90:135], 0.05)
    print("\033[15;10H" + COLORS['CYAN'] + "│" + COLORS['RESET'], end="")
    print_slow(quote[135:180], 0.05)
    print("\033[16;10H" + COLORS['CYAN'] + "│" + COLORS['RESET'], end="")
    print_slow(quote[180:], 0.05)
    
    # Add Woody's glasses and neurotic sweat
    print("\033[18;20H" + COLORS['MAGENTA'] + "  (  o   o  )  " + COLORS['RESET'])
    print("\033[19;20H" + COLORS['MAGENTA'] + "   \\  ^  /    " + COLORS['RESET'])
    print("\033[20;20H" + COLORS['MAGENTA'] + "    \\___/     " + COLORS['RESET'])
    print("\033[21;20H" + COLORS['MAGENTA'] + "     | |      " + COLORS['RESET'])
    print("\033[22;20H" + COLORS['RED'] + "  *sweating*" + COLORS['RESET'])
    
    # Add existential footnote
    print("\033[24;5H" + COLORS['BOLD'] + COLORS['BLUE'] + "Note: This quote is 98% statistically likely to be true" + COLORS['RESET'])
    print("\033[25;5H" + COLORS['BOLD'] + COLORS['BLUE'] + "in 3.2 out of 5 parallel universes (according to my therapist)" + COLORS['RESET'])
    
    # Add blinking cursor for "unresolved tension"
    for _ in range(5):
        print("\033[26;5H" + COLORS['RED'] + "█" + COLORS['RESET'], end="", flush=True)
        time.sleep(0.3)
        print("\033[26;5H  ", end="", flush=True)
        time.sleep(0.3)
    
    print("\033[27;5H" + COLORS['YELLOW'] + "Press any key to continue avoiding reality... ", end="")
    sys.stdin.read(1)

if __name__ == "__main__":
    main()