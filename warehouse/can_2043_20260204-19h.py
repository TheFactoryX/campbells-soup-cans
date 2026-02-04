"""
Campbell's Soup Can #2043
Produced: 2026-02-04 19:08:50
Worker: DeepSeek: DeepSeek V3 0324 (deepseek/deepseek-chat-v3-0324)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_quote():
    quote = "I'm really bad at existential crises - I keep forgetting to have them."
    author = "- Woody Allen in a parallel universe, probably"

    colors = [91, 93, 95, 96]
    symbols = ["★", "⚡", "❋", "✧", "✿"]
    border = "═" * 60

    print("\n" * 2)
    print(color_text(f"╔{border}╗", 95))
    
    # Animated header
    for i in range(5):
        sys.stdout.write(color_text("║" + " " * 24, 95))
        for j in range(5):
            color = random.choice(colors)
            sys.stdout.write(color_text(symbols[j] + " ", color))
            sys.stdout.flush()
            time.sleep(0.1)
        print(color_text("PHILOSOPHICAL QUOTE" + " " * 21 + "║", 95))
        if i < 4:
            sys.stdout.write("\033[F")  # Move cursor up
    
    print(color_text(f"╠{border}╣", 95))
    
    # Quote with word-by-word reveal
    words = quote.split()
    for i, word in enumerate(words):
        color = colors[i % len(colors)]
        sys.stdout.write(color_text(word + " ", color))
        sys.stdout.flush()
        time.sleep(0.2)
    print(color_text(" " * (60 - len(quote)) + "║", 95))
    
    # Delay for author
    time.sleep(0.5)
    print(color_text(f"║{' ' * ((60 - len(author))//2)}{author}{' ' * ((60 - len(author))//2)}║", 93))
    
    print(color_text(f"╚{border}╝", 95))
    print("\n" * 2)

if __name__ == "__main__":
    print_quote()