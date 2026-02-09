"""
Campbell's Soup Can #2137
Produced: 2026-02-09 16:13:12
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import random
import sys

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
INVERT = '\033[7m'

def clear_screen():
    """Clear terminal screen with dramatic effect"""
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def typewriter(text, color=WHITE, delay=0.03, newline=True):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))
    if newline:
        print()

def animated_box(text, width=60):
    """Print text inside an animated expanding box"""
    padded_text = f" {text} "
    box_width = min(len(padded_text) + 4, width)
    
    # Animate box expansion
    for i in range(5, box_width + 1):
        clear_screen()
        print(YELLOW + "╔" + "═" * (i-2) + "╗" + RESET)
        print(YELLOW + "║" + RESET + padded_text.center(i-2) + YELLOW + "║" + RESET)
        print(YELLOW + "╚" + "═" * (i-2) + "╝" + RESET)
        time.sleep(0.05)
    time.sleep(0.5)
    clear_screen()

def philosophical_display():
    """Main display with multiple visual effects"""
    quote = ("I'm not afraid of death; I just don't want to be there when it happens. "
             "Life is like a conveyor belt of existential crises with no off switch, "
             "and the warranty expired before I even opened the box.")
    
    clear_screen()
    
    # Phase 1: Spiral effect with colors
    colors = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]
    for i in range(30):
        color = colors[i % len(colors)]
        sys.stdout.write('\033[{};{}H'.format(i % 24 + 1, i % 80 + 1))
        sys.stdout.write(color + "◈" + RESET)
        sys.stdout.flush()
        time.sleep(0.03)
    
    time.sleep(0.3)
    clear_screen()
    
    # Phase 2: Matrix-like falling characters
    print("\n" * 5)
    for _ in range(10):
        line = ""
        for _ in range(60):
            line += random.choice("01 ") + " "
        print(random.choice([CYAN, GREEN, BLUE]) + line + RESET)
        time.sleep(0.05)
    
    time.sleep(0.3)
    clear_screen()
    
    # Phase 3: The main quote in a fancy box
    animated_box("WOODY ALLEN MODE: ENGAGED", 50)
    
    # Phase 4: The actual quote with dramatic presentation
    print("\n" * 2)
    
    # Split quote into parts for dramatic effect
    parts = [
        "While walking my dog the other day,",
        "I had an epiphany about the meaning of life.",
        "Or maybe it was just gas.",
        "Either way, I've concluded that:",
        "",
        quote,
        "",
        "So I canceled my appointment with the existentialist.",
        "Turns out he was just a nihilist in a cardigan."
    ]
    
    for i, part in enumerate(parts):
        if i == 5:  # The main quote
            typewriter(part, YELLOW, 0.04)
            time.sleep(0.8)
        elif "epiphany" in part or "concluded" in part:
            typewriter(part, CYAN, 0.03)
            time.sleep(0.4)
        elif "canceled" in part:
            typewriter(part, GREEN, 0.03)
            time.sleep(0.4)
        else:
            typewriter(part, WHITE, 0.02)
            time.sleep(0.2)
    
    time.sleep(1)
    
    # Phase 5: Final signature with blink effect
    print("\n")
    for _ in range(3):
        sys.stdout.write('\033[?25l')  # Hide cursor
        print(INVERT + "    — Woody Allen (probably while worrying about death)" + RESET)
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\033[?25h')  # Show cursor
        print(" " * 60)  # Clear line
        time.sleep(0.3)
    
    # Final touch: wavy underline
    print("\n")
    wave = "~" * 60
    for offset in range(10):
        sys.stdout.write("\033[{};0H".format(25))
        sys.stdout.write(MAGENTA + wave[offset:] + wave[:offset] + RESET)
        sys.stdout.flush()
        time.sleep(0.1)
    
    print("\n" * 2)

if __name__ == "__main__":
    try:
        philosophical_display()
    except KeyboardInterrupt:
        clear_screen()
        print(RED + "\n>> Philosophy interrupted. Too many questions, not enough answers. <<" + RESET)
        sys.exit(0)