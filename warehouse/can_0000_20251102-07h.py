"""
Campbell's Soup Can #0
Produced: 2025-11-02 07:50:31
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(text, color_code, end='\n'):
    sys.stdout.write(f"\033[{color_code}m{text}\033[0m{end}")
    sys.stdout.flush()

def box_centered(text, width, border='.'):
    padding = ' ' * ((width - len(text)) // 2)
    return f"{border} {padding}{text}{padding} {border}"

def animated_appearance(text, color_code, delay=0.05):
    for i in range(len(text) + 1):
        print_colored(f"{text[:i]:<{len(text)}}", color_code)
        time.sleep(delay)

def quote_animation():
    clear_screen()
    
    # ANSI colors
    TITLE_COLOR = "38;5;208"
    BRAIN_COLOR = "38;5;45"
    QUOTE_COLOR = "38;5;208"
    FOOTER_COLOR = "38;5;202"
    EFFECT_COLOR = "38;5;196"
    
    # Quote definition
    quote_parts = [
        "I've developed a theory",
        "that the world is full of misery",
        "and suffering - the real question is",
        "Why do I keep parking my car"
    ]
    
    brain = [
        "     .-.           ( O.O )",
        "   '-().().-       (-_-)_|",
        "     /|/ |         ^^^^^"
    ]
    
    # Animated intro message
    intro = "🧠 MY NEUROTIC THOUGHTS 🧠"
    for i in range(len(intro)+1):
        clear_screen()
        print coloured(box_centered(intro[:i], 60, '✲'))


        # Print upper border
        print(f"✲{'─' * 56}✲")
        
        # Print ASCII brain
        for line in brain:
            print(box_centered(line, 60, ' '))
        
        print(f"✲{'─' * 56}✲")
        
        print_colored("\n", TITLE_COLOR, end='')
        time.sleep(0.08)
    
    # Animated quote
    print("\n" * 5)
    for part in quote_parts:
        animated_appearance(part, QUOTE_COLOR, 0.07)
        time.sleep(0.3)
    print("\n" * 2)
    
    # Animated effects
    effects = [
        "(ERR: High-Existential-Threat Detected)",
        "⚠️ Too Many Numbers in My Coffee ☕",
        "ಠ益ಠ Optimalism is overrated"
    ]
    for _ in range(2):
        for effect in effects:
            print_colored(effect, EFFECT_COLOR)
            time.sleep(2)
            clear_screen()  # Swap effects in and out
    
    # Bottom border
    print(f"\n")

if __name__ == "__main__":
    quote_animation()