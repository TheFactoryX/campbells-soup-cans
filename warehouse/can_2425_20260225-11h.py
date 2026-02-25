"""
Campbell's Soup Can #2425
Produced: 2026-02-25 11:09:49
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
import sys
import os

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    # Colors
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

def clear_screen():
    """Clear terminal screen (works on most systems)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, color=Colors.BRIGHT_YELLOW, delay=0.03, end='\n'):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print(end=end)

def flickering_text(text, flicker_count=5, base_color=Colors.BRIGHT_CYAN):
    """Text that flickers like a broken neon sign"""
    for i in range(flicker_count):
        if i % 2 == 0:
            print(base_color + text + Colors.RESET, end='\r')
        else:
            print(Colors.DIM + text + Colors.RESET, end='\r')
        time.sleep(0.1)
    print(Colors.BOLD + base_color + text + Colors.RESET)

def draw_neurotic_box(quote):
    """Draw Woody Allen looking nervously at his own quote"""
    width = max(len(line) for line in quote) + 4
    
    # Top of box with nervous wobble
    for i in range(3):
        wobble = " " * (i % 2)
        print(Colors.BRIGHT_MAGENTA + "╭" + "─" * (width-2) + "╮" + Colors.RESET)
        time.sleep(0.05)
    
    # Quote lines with different colors
    emotions = [Colors.BRIGHT_YELLOW, Colors.BRIGHT_CYAN, Colors.BRIGHT_RED, Colors.BRIGHT_GREEN]
    for i, line in enumerate(quote):
        emotion = emotions[i % len(emotions)]
        padded = line.center(width-4)
        print(Colors.BRIGHT_MAGENTA + "│ " + Colors.RESET + 
              emotion + padded + Colors.RESET + 
              Colors.BRIGHT_MAGENTA + " │" + Colors.RESET)
        time.sleep(0.1)
    
    # Bottom of box with sigh
    print(Colors.BRIGHT_MAGENTA + "╰" + "─" * (width-2) + "╯" + Colors.RESET)
    time.sleep(0.2)
    
    # Woody's signature nervous addition
    print(Colors.DIM + "     ( nervously taps foot )" + Colors.RESET)

def main():
    clear_screen()
    
    # Woody Allen's existential dread in ASCII
    woody = r"""
       ╭───────────────────────────────────────╮
       │  ╭──────────────╮                    │
       │  │  (  ○    ○  )│     My therapist   │
       │  │      ⌣       │   says I have a    │
       │  ╰──────────────╯     preoccupation   │
       │                      with mortality.  │
       │                                      │
       │  But I think that's just because I   │
       │  don't want to be late for my own    │
       │  funeral. What if everyone leaves   │
       │  before I get there?                │
       │                                      │
       ╰──────────────────────────────────────╯
    """
    
    print(Colors.BRIGHT_WHITE + woody + Colors.RESET)
    time.sleep(1.5)
    
    # The quote with existential neurosis
    quote_lines = [
        "I'm not afraid of death; I just don't want to be there",
        "when it happens. I mean, what if the catering is",
        "terrible? What if they play the wrong music?",
        "",
        "And don't get me started on eternity. Forever is",
        "a very long time to be dead. I'd rather be",
        "somewhat alive for a very long time.",
        "",
        "I try to live each day as if it were my last.",
        "Which, statistically speaking, it probably is."
    ]
    
    # Animated reveal
    print("\n" + Colors.BOLD + Colors.BRIGHT_CYAN + "»" + Colors.RESET + 
          Colors.DIM + " Woody Allen's Guide to Existential Dread " + 
          Colors.RESET + Colors.BRIGHT_CYAN + "«" + Colors.RESET + "\n")
    time.sleep(0.5)
    
    draw_neurotic_box(quote_lines)
    time.sleep(0.5)
    
    # Final dramatic touch
    flickering_text("( silence... followed by nervous laughter )", 
                    flicker_count=8, 
                    base_color=Colors.BRIGHT_RED)
    
    print("\n" + Colors.ITALIC + Colors.DIM + 
          "- from 'Thoughts While Waiting for the Reaper'" + 
          Colors.RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Colors.RESET + "\n\n" + Colors.DIM + 
              "(You escaped your existential crisis. For now.)" + 
              Colors.RESET)
        sys.exit(0)