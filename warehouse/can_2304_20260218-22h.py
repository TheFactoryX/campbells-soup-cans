"""
Campbell's Soup Can #2304
Produced: 2026-02-18 22:53:52
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A Philosophical Typewriter in Woody Allen's Style
Press Ctrl+C to exit early.
"""

import time
import sys
import random

# ANSI color codes
COLORS = {
    'reset': '\033[0m',
    'yellow': '\033[33m',
    'cyan': '\033[36m',
    'magenta': '\033[35m',
    'green': '\033[32m',
    'red': '\033[31m',
    'blue': '\033[34m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'blink': '\033[5m',
}

# Woody Allen-style philosophical quotes (original)
QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "I'm not an existentialist. I just walk into a room and think, 'Why am I here?' and 'Where's the cheese?'",
    "My only regret in life is that I am not someone else.",
    "I don't believe in the afterlife, but I'm taking a change of underwear just in case.",
    "What if everything is an illusion and nothing exists? In that case, I definitely overpaid for my carpet.",
    "I'm not a pessimist. I'm an optimist who has done the math.",
    "I asked God for a bike, but I know God doesn't work that way. So I stole a bike and asked for forgiveness.",
    "Time is nature's way of keeping everything from happening at once. Which is also my approach to dating."
]

def typewriter(text, color='yellow', delay=0.03, end='\n', flush=True):
    """Print text with typewriter effect and color"""
    print(COLORS[color], end='', flush=True)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay + random.uniform(-0.01, 0.01))
    print(COLORS['reset'], end=end, flush=True)

def philosophical_box():
    """Create a fancy ASCII art box with philosophical quote"""
    quote = random.choice(QUOTES)
    
    # Calculate box dimensions
    max_len = len(quote) + 10
    if max_len < 50:
        max_len = 50
    
    # Random color scheme
    border_color = random.choice(['cyan', 'magenta', 'green', 'blue'])
    text_color = 'yellow'
    
    # Top border with random sparkles
    sparkles = random.choice(['✧', '*', '•', '⁂', '⋆'])
    top = f"{COLORS[border_color]}"
    top += f"╔{'═' * (max_len - 2)}╗\n"
    
    # Quote lines with padding
    words = quote.split()
    lines = []
    current_line = []
    current_len = 0
    
    for word in words:
        if current_len + len(word) + 1 <= max_len - 8:
            current_line.append(word)
            current_len += len(word) + 1
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_len = len(word)
    if current_line:
        lines.append(' '.join(current_line))
    
    # Build middle section
    middle = ""
    for i, line in enumerate(lines):
        padding = max_len - 8 - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        
        # Add random decorative elements
        decor = random.choice(['┊', '│', '╎', '┆']) if i > 0 and i < len(lines)-1 else ' '
        middle += f"{COLORS[border_color]}║{COLORS['reset']}"
        middle += f"{COLORS['dim']}{decor * left_pad}{COLORS['reset']}"
        middle += f"{COLORS[text_color]}{line.center(max_len - 8)}{COLORS['reset']}"
        middle += f"{COLORS['dim']}{decor * right_pad}{COLORS['reset']}"
        middle += f"{COLORS[border_color]}║{COLORS['reset']}\n"
    
    # Bottom border
    bottom = f"{COLORS[border_color]}╚{'═' * (max_len - 2)}╝{COLORS['reset']}\n"
    
    # Add philosophical footer
    footer = f"{COLORS['dim']}~ A Thought for Today ~{COLORS['reset']}\n"
    footer += f"{COLORS['blink']}✷{COLORS['reset']}\n"
    
    return top + middle + bottom + footer

def animated_intro():
    """Play a little intro animation"""
    phrases = [
        "In a universe of meaningless chance...",
        "amidst the cosmic indifference...",
        "one man's search for meaning",
        "becomes a comedy of errors."
    ]
    
    print("\n" * 3)
    for phrase in phrases:
        typewriter(phrase.center(60), color='cyan', delay=0.05)
        time.sleep(0.3)
        print("\033[F\033[K", end='')  # Move up and clear line
    
    time.sleep(0.5)
    print("\n" * 2)

def main():
    try:
        animated_intro()
        
        # Create and display the philosophical box
        box = philosophical_box()
        
        # Typewrite the box with varying speeds
        i = 0
        for char in box:
            # Vary speed based on character type
            delay = 0.01 if char in '═║╔╗╚╝' else 0.02
            if char.isalpha() or char in ' .,;:!?"':
                delay = 0.03 + random.uniform(-0.005, 0.005)
            
            print(char, end='', flush=True)
            time.sleep(delay)
            i += 1
            
            # Occasional dramatic pause
            if i % 30 == 0 and random.random() < 0.3:
                time.sleep(0.1)
                
    except KeyboardInterrupt:
        print(f"\n\n{COLORS['red']}[Exiting prematurely - just like my relationships]{COLORS['reset']}")
        sys.exit(0)
    
    time.sleep(1)
    print(f"\n{COLORS['dim']}Press Enter to contemplate further, or Ctrl+C to accept the void...{COLORS['reset']}")
    try:
        input()
        # Recursion for continuous contemplation
        print("\n" * 2)
        main()
    except KeyboardInterrupt:
        print(f"\n\n{COLORS['yellow']}Good. Questions are uncomfortable. Goodbye.{COLORS['reset']}")

if __name__ == "__main__":
    main()