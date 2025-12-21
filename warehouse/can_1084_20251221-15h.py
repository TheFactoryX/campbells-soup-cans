"""
Campbell's Soup Can #1084
Produced: 2025-12-21 15:30:54
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A Woody Allen-style neurotic philosophical quote generator.
Because anxiety and existential dread have never been so colorful!
"""

import sys
import time
import random

def print_wobbly_text(text, color_code):
    """Print text with a wobbly, nervous effect"""
    for i, char in enumerate(text):
        # Add random wobble (tiny delays and jitter)
        sys.stdout.write(f"\033[{color_code}m{char}\033[0m")
        if random.random() < 0.1:  # 10% chance of tiny pause
            time.sleep(0.005)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def draw_anxious_heart():
    """Draw a nervous, trembling heart"""
    heart = [
        "    @@@@     @@@@    ",
        "  @@@@@@@@ @@@@@@@@  ",
        " @@@@@@@@@@@@@@@@@@ ",
        " @@@@@@@@@@@@@@@@@@ ",
        "  @@@@@@@@@@@@@@@@  ",
        "   @@@@@@@@@@@@@@   ",
        "     @@@@@@@@@@     ",
        "       @@@@@@       ",
        "         @@         "
    ]
    
    # Make it "tremble"
    for line in heart:
        offset = random.randint(-1, 1)
        print(" " * (10 + offset) + f"\033[91m{line}\033[0m")
        time.sleep(0.05)

def main():
    # ANSI color codes
    CYAN = "96"
    YELLOW = "93"
    RED = "91"
    MAGENTA = "95"
    BLUE = "94"
    
    # Woody Allen-style neurotic quotes
    quotes = [
        "I don't suffer from existential dread—I enjoy it. It's my hobby. My therapist says I have commitment issues with reality.",
        "I'm not afraid of death; I just don't want to be there when it happens. Preferably, I'd like to delegate that responsibility.",
        "Life is full of misery, loneliness, and suffering—and it's all over much too soon. Talk about false advertising!",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying. And maybe good health insurance.",
        "My greatest talent is worrying. I could win an Olympic gold medal in catastrophic thinking—if they had such an event, which they should.",
        "I'm at two with nature. We don't speak anymore. It started when I realized trees were judging me.",
        "The universe is a vast, indifferent void... and I'm pretty sure it's personally offended by my cooking.",
        "I tried meditation to find inner peace. Now I have inner peace AND anxiety about whether I'm meditating correctly.",
        "They say 'be yourself.' But what if yourself is a slightly used, neurotic mess with commitment issues and a tendency to overthink?",
        "I don't need therapy—I need a time machine to go back and prevent all my childhood traumas from happening. Or at least a very understanding bartender."
    ]
    
    # Pick a random quote
    quote = random.choice(quotes)
    
    # Print header with neurotic energy
    print("\n" * 3)
    print_wobbly_text("NEUROTIC WISDOM GENERATOR v2.1 (Last updated: My last panic attack)", CYAN)
    print_wobbly_text("=" * 70, YELLOW)
    print()
    
    # Draw the anxious heart
    draw_anxious_heart()
    print()
    
    # Print the quote with dramatic pauses
    print_wobbly_text("Today's Philosophical Insight:", MAGENTA)
    print()
    
    # Print quote with emphasis on key words
    words = quote.split()
    for i, word in enumerate(words):
        if any(key in word.lower() for key in ['afraid', 'death', 'misery', 'dread', 'worst', 'neurotic', 'anxiety', 'therapist']):
            print(f"\033[91m{word}\033[0m", end=" ")
        elif any(key in word.lower() for key in ['enjoy', 'talent', 'gold', 'peace', 'hobby']):
            print(f"\033[92m{word}\033[0m", end=" ")
        else:
            print(word, end=" ")
        sys.stdout.flush()
        time.sleep(0.1)
    
    print("\n")
    print_wobbly_text("- Woody Allen (probably, we're not sure, check his lawyer)", BLUE)
    print()
    
    # Footer with self-doubt
    print_wobbly_text("Disclaimer: This quote may or may not be helpful. Results may vary. Side effects include increased self-awareness and mild hypochondria.", YELLOW)
    print_wobbly_text("=" * 70, CYAN)
    print("\n" * 2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[93mAh, you're leaving already? Just like my last relationship. Can't say I blame you.\033[0m")
        sys.exit(0)