"""
Campbell's Soup Can #5165
Produced: 2026-10-25 13:11:21
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_slow(text, delay=0.03):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_title():
    """Print the title with ASCII art"""
    title = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║           🎬 A WOODY ALLEN THOUGHT 🎬                       ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    
    # Rainbow effect for title
    colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
    for i, line in enumerate(title.split('\n')):
        if line.strip():
            color = colors[i % len(colors)]
            print(color + line + '\033[0m')
        else:
            print()

def animate_quote():
    """Display the quote with animations"""
    
    # The Woody Allen style quote
    quote = "I've come to the conclusion that the only thing I have in common with Socrates is that I'd rather be at a cafe than in the agora. Though, to be honest, even the cafe makes me anxious - what if the espresso machine achieves consciousness and starts judging my order?"
    
    # Border animation
    border_top = "┌" + "─" * 60 + "┐"
    border_bottom = "└" + "─" * 60 + "┘"
    
    # Print border with fade-in effect
    for i in range(61):
        line = "┌" + "─" * i + " " * (60 - i) + "┐"
        print('\033[90m' + line + '\033[0m', end='\r')
        time.sleep(0.02)
    
    print('\033[90m' + border_top + '\033[0m')
    
    # Print quote with typewriter effect and changing colors
    words = quote.split()
    color_codes = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
    
    print('\033[90m│ ' + '\033[0m', end='')
    
    for i, word in enumerate(words):
        color = color_codes[i % len(color_codes)]
        # Add punctuation to words that should have it
        if word.endswith(',') or word.endswith('.'):
            print_slow(color + word + ' ', 0.05)
        else:
            print_slow(color + word + ' ', 0.04)
    
    print('\033[90m' + border_bottom + '\033[0m')
    
    # Animated ellipsis
    print("\n\033[93mThinking", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="")
    print("\033[0m")

def main():
    """Main function to run the Woody Allen quote generator"""
    
    # Clear screen for better animation
    print('\033[2J\033[H', end="")
    
    # Print title
    print_title()
    time.sleep(0.5)
    
    # Print the animated quote
    animate_quote()
    
    # Add some philosophical Woody Allen commentary
    print("\n\033[95m" + "=" * 60 + "\033[0m")
    print_slow("\033[95mYou know, I was thinking about existentialism last night...", 0.04)
    print_slow("\033[95mIt's like a bad restaurant - the food is terrible, and yet, we keep going back.", 0.04)
    print_slow("\033[95mMaybe that's what life is - a series of bad meals we can't stop ordering.", 0.04)
    print("\033[95m" + "=" * 60 + "\033[0m")
    
    # Final touch - glasses ASCII art
    glasses = """
    \033[90m    ╭──────╮  ╭──────╮
       │  ●  │  │  ●  │
       ╰──────╯  ╰──────╯
       \033[90m    \033[0m
    """
    print("\n" + glasses)

if __name__ == "__main__":
    main()