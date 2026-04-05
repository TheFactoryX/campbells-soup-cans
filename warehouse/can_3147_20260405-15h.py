"""
Campbell's Soup Can #3147
Produced: 2026-04-05 15:47:21
Worker: Mistral: Ministral 3 14B 2512 (mistralai/ministral-14b-2512)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random
from itertools import cycle

def get_terminal_size():
    """Get terminal width and height"""
    try:
        size = sys.stdout.get_terminal_size()
        return size.columns, size.lines
    except:
        return 80, 24

def print_colored(text, color_code):
    """Print colored text using ANSI escape codes"""
    print(f"\033[{color_code}m{text}\033[0m", end='')

def typewriter_effect(text, delay=0.05, color=33):
    """Simulate a typewriter effect with optional color"""
    for char in text:
        print_colored(char, color)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_woody_box(quote, width=60):
    """Draw a decorative box around the quote"""
    terminal_width, _ = get_terminal_size()
    box_width = min(width, terminal_width - 4)

    # Top border
    print_colored("╔" + "═" * box_width + "╗", 36)

    # Left border and quote
    quote_lines = quote.split('\n')
    for line in quote_lines:
        print_colored("║ " + line.ljust(box_width - 2) + " ║", 36)

    # Bottom border
    print_colored("╚" + "═" * box_width + "╝", 36)

def woody_animation():
    """Create a simple Woody Allen ASCII animation"""
    frames = [
        r"""
        .-""""""-.
       /          \
      |            |
      |            |
      |            |
      |            |
      |            |
      |            |
       \          /
        '-......-'
        """,
        r"""
        .-""""""-.
       /          \
      |            |
      |   O   O    |
      |    \ /     |
      |     |      |
      |    / \     |
      |   O   O    |
       \          /
        '-......-'
        """,
        r"""
        .-""""""-.
       /          \
      |            |
      |   O   O    |
      |    \ /     |
      |     |      |
      |    / \     |
      |   O   O    |
      |   /   \    |
       \          /
        '-......-'
        """
    ]

    for _ in range(3):
        for frame in cycle(frames):
            print_colored("\033[H", 0)  # Move cursor to home position
            print(frame)
            time.sleep(0.3)

def main():
    # Clear screen and get terminal size
    print("\033[H\033[J", end="")

    # Woody Allen quotes
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.\n"
        "After all, if you're not there, how can you die? It's like being absent\n"
        "from your own funeral. I wouldn't miss that for the world.",

        "Life is full of misery, loneliness, and suffering - and it's all over much\n"
        "too soon. I mean, if you think about it, we're all going to die, and\n"
        "that's the saddest thing of all. But at least we can laugh about it.",

        "I don't want to achieve immortality through my work; I want to achieve it\n"
        "through not dying. And I'm working on that too. Every day. It's a full-time\n"
        "job, but someone's gotta do it.",

        "The only thing that makes life possible is permanent, intolerable\n"
        "uncertainty. Not knowing what's going to happen next. That's what keeps\n"
        "us going. Otherwise, we'd all just curl up and die. And frankly, I'm\n"
        "considering it.",

        "I'm not anti-social, I just don't like people. I mean, I like them\n"
        "individually, but as a group, they're just a bunch of strangers who\n"
        "happen to be in the same room. And that's depressing.",

        "The heart wants what it wants, or else it does not care.\n"
        "The brain wants what it should have, after it has established\n"
        "what that is. The two should collaborate, not gang up on each\n"
        "other. But they rarely do.",

        "I'm not afraid of death; I just don't want to be there when it happens.\n"
        "I mean, if you're not there, how can you die? It's like being absent\n"
        "from your own funeral. I wouldn't miss that for the world."
    ]

    # Select a random quote
    quote = random.choice(quotes)

    # Display animation
    woody_animation()

    # Typewriter effect for the quote
    print_colored("\n\033[1;33m" + "="*50 + "\n", 0)
    print_colored("\033[1;33mWoody Allen's Wisdom:\033[0m\n", 0)
    typewriter_effect(quote, color=33)

    # Draw decorative box
    print_colored("\n\033[1;36m" + "="*50 + "\n", 0)
    draw_woody_box(quote)

    # Final thought with animation
    print_colored("\n\033[1;33mAnd remember...\033[0m\n", 0)
    typewriter_effect("The more I learn, the more I realize how much I don't know.\n"
                     "And that's what keeps me going.", color=33)

    # Exit animation
    print_colored("\n\033[1;36m" + "="*50 + "\n", 0)
    print_colored("\033[1;33mThanks for listening. Now go make your own existential crisis.\033[0m\n", 0)
    print_colored("\033[1;36m" + "="*50 + "\n", 0)

if __name__ == "__main__":
    main()