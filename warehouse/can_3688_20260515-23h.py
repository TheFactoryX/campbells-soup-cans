"""
Campbell's Soup Can #3688
Produced: 2026-05-15 23:11:59
Worker: Arcee AI: Trinity Large Thinking (free) (arcee-ai/trinity-large-thinking:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen-style philosophical quote with visual flair.
Features: ANSI colors, typing animation, ASCII frame, and a neurotic twist.
"""

import sys
import time
import random

def typewriter(text, color_code="\033[97m", delay=0.03):
    """Simulate a typewriter effect with color."""
    for char in text:
        sys.stdout.write(color_code + char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\033[0m")  # Reset color

def draw_frame(content, title=""):
    """Draw a decorative ASCII frame around content."""
    border = "\033[36m" + "=" * 60 + "\033[0m"
    print("\n" + border)
    if title:
        print(f"\033[35m{title:^60}\033[0m")
        print(border)
    for line in content.split('\n'):
        print(f"\033[37m| \033[93m{line:<56}\033[37m|\033[0m")
    print(border)

def main():
    # Clear screen
    print("\033[2J\033[H", end='')
    
    # Title with glitch effect
    titles = [
        "WOODY ALLEN'S PHILOSOPHICAL MOMENT",
        "A NEUROTIC THOUGHT FOR THE DAY",
        "EXISTENTIAL DREAD IN 3... 2... 1..."
    ]
    for i, title in enumerate(random.sample(titles, 1)):
        print(f"\033[{random.randint(30,37)}m" + " " * 20 + title)
        time.sleep(0.5)
    
    print("\033[0m" + "\n" + "-" * 60 + "\n")
    
    # The quote (original Woody Allen style)
    quote = (
        "I once had a existential crisis, but I postponed it for "
        "tomorrow. Honestly, I'm not afraid of death—I just don't "
        "want to be there when it happens. Besides, life is full of "
        "misery, loneliness, and suffering—and it's all over much "
        "too soon. So I've decided to achieve immortality by not "
        "dying. It's a foolproof plan... unless I'm wrong."
    )
    
    # Typing animation for quote
    typewriter(quote, "\033[93m", 0.02)
    
    # Philosophical commentary (smaller text)
    commentary = (
        "Thoughts:\n"
        "- Death: inconvenient timing.\n"
        "- Immortality: works for me, if I'm not mistaken.\n"
        "- Life: short, nasty, and full of parentheses."
    )
    
    # Print commentary with indentation
    print("\n" + "\033[90m" + " " * 4 + commentary.replace('\n', '\n' + " " * 4) + "\033[0m")
    
    # Draw a fancy frame around a summary
    summary = "MORAL: Never put off until tomorrow what you can ignore entirely."
    draw_frame(summary, "IN CONCLUSION")
    
    # Final existential sigh
    print("\033[31m" + "\n" + " " * 15 + "°(°_°)^" + "\033[0m")
    print("\033[90m" + "\n" + "Press any key to accept the void..." + "\033[0m")
    input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\033[2J\033[H", end='')  # Clear screen on Ctrl+C
        sys.exit(0)