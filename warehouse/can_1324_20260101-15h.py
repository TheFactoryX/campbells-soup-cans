"""
Campbell's Soup Can #1324
Produced: 2026-01-01 15:33:44
Worker: Anthropic: Claude Sonnet 4.5 (anthropic/claude-sonnet-4.5)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ANSI color codes
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m'
}

def print_with_typing_effect(text, delay=0.03, color='white'):
    for char in text:
        print(f"{COLORS[color]}{char}{COLORS['reset']}", end='', flush=True)
        time.sleep(delay)
    print()

def animated_woody_quote():
    # The quote
    quote = "I'd call my therapist, but I'm too busy contemplating the void - which is ironic because therapy is basically paying someone to watch you contemplate the void with better furniture."
    
    # Animated title
    print("\n" * 2)
    title = "🎬 WOODY ALLEN PRESENTS 🎬"
    for i in range(3):
        print(f"{COLORS['cyan']}{COLORS['bold']}{' ' * 20}{title}{COLORS['reset']}")
        time.sleep(0.2)
        print("\033[F\033[K", end='')
    print(f"{COLORS['cyan']}{COLORS['bold']}{' ' * 20}{title}{COLORS['reset']}")
    
    time.sleep(0.5)
    
    # Neurotic thinking animation
    thoughts = ["🤔", "😰", "🤷", "😅"]
    print(f"\n{' ' * 25}", end='')
    for _ in range(8):
        for thought in thoughts:
            print(f"\r{' ' * 25}{thought} Thinking neurotically...", end='', flush=True)
            time.sleep(0.15)
    print("\r" + " " * 60 + "\r", end='')
    
    # Fancy box around quote
    box_width = 70
    print(f"\n{COLORS['yellow']}{'═' * box_width}{COLORS['reset']}")
    
    # Split quote into lines
    words = quote.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= box_width - 6:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    
    # Print quote with typing effect
    for line in lines:
        print(f"{COLORS['yellow']}║{COLORS['reset']} ", end='')
        print_with_typing_effect(f"{line:<{box_width-4}}", delay=0.02, color='magenta')
        print(f"{COLORS['yellow']} ║{COLORS['reset']}", end='')
        print()
    
    print(f"{COLORS['yellow']}{'═' * box_width}{COLORS['reset']}")
    
    # Attribution with animation
    time.sleep(0.3)
    attribution = "- Definitely Not Woody Allen (but he'd probably relate)"
    print(f"\n{' ' * 10}", end='')
    print_with_typing_effect(attribution, delay=0.04, color='cyan')
    
    # Existential flourish
    time.sleep(0.5)
    print(f"\n{COLORS['dim']}{COLORS['white']}", end='')
    symbols = ['*', '·', '°', '•', '○', '●']
    for _ in range(40):
        print(random.choice(symbols), end='', flush=True)
        time.sleep(0.02)
    print(f"{COLORS['reset']}\n")
    
    # Final neurotic note
    time.sleep(0.3)
    footnote = "P.S. If you didn't laugh, you're probably healthier than me. 😬"
    print(f"{COLORS['green']}{' ' * 15}{footnote}{COLORS['reset']}")
    print("\n")

if __name__ == "__main__":
    animated_woody_quote()