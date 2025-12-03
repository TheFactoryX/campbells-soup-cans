"""
Campbell's Soup Can #695
Produced: 2025-12-03 20:37:58
Worker: Meituan: LongCat Flash Chat (free) (meituan/longcat-flash-chat:free)
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

# ANSI color codes
COLORS = {
    'clear': '\033[0m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'purple': '\033[38;5;141m',
    'orange': '\033[38;5;208m',
    'pink': '\033[38;5;205m',
    'beige': '\033[38;5;223m',
    'bold': '\033[1m',
    'blink': '\033[5m',
    'underline': '\033[4m',
}

def typewriter(text, delay=0.05, color=None):
    """Print text with typewriter effect"""
    for char in text:
        col = COLORS.get(color, COLORS['clear']) if color else ''
        sys.stdout.write(col + char + COLORS['clear'])
        sys.stdout.flush()
        time.sleep(delay)
    print()

def create_quote_box(quote, author):
    """Create a nicely formatted ASCII box with the quote"""
    lines = quote.split('\n')
    max_len = max(len(line) for line in lines)
    box_width = max_len + 8
    inner_width = box_width - 4

    # Top border
    print(f"{COLORS['purple']}╔{'═' * (box_width - 2)}╗{COLORS['clear']}")
    
    # Empty line
    print(f"{COLORS['purple']}║{' ' * (box_width - 2)}║{COLORS['clear']}")
    
    # Quote lines
    for line in lines:
        padded_line = f"  {line:<{inner_width - 2}}"
        print(f"{COLORS['purple']}║{COLORS['yellow']}{padded_line}{COLORS['purple']}║{COLORS['clear']}")
    
    # Empty line
    print(f"{COLORS['purple']}║{' ' * (box_width - 2)}║{COLORS['clear']}")
    
    # Author line
    padded_author = f"  {author:<{inner_width - 2}}"
    print(f"{COLORS['purple']}║{COLORS['cyan']}{padded_author}{COLORS['purple']}║{COLORS['clear']}")
    
    # Bottom border
    print(f"{COLORS['purple']}╚{'═' * (box_width - 2)}╝{COLORS['clear']}")

def spinning_cursor():
    """Simple spinner animation"""
    chars = ['|', '/', '-', '\\']
    for _ in range(16):
        for ch in chars:
            sys.stdout.write(f"\r{COLORS['beige']} {ch} Deep Philosophical Thinking {ch}{COLORS['clear']}")
            sys.stdout.flush()
            time.sleep(0.1)

def draw_people():
    """Draw a couple of sad people figures"""
    people = [
        f"  {COLORS['pink']}{COLORS['bold']}O{COLORS['clear']}    {COLORS['green']}{COLORS['bold']}O{COLORS['clear']}  ",
        f" {COLORS['pink']}\|/\033[0m   {COLORS['green']}\|/\033[0m ",
        f"  {COLORS['pink']}^ \033[0m   {COLORS['green']}^ \033[0m  ",
        f" / \\   / \\ ",
        f"|   | |   |",
    ]
    
    for i, line in enumerate(people):
        spaces_before = " " * (10 + min(i, len(people) - i))
        spaces_between = " " * (15 - abs(i - 2) * 3)
        if i < len(people) - 1:
            print(f"{spaces_before}{line}{spaces_between}{line}")
        else:
            # Last line gets extra decoration
            print(f"{COLORS['red']}{spaces_before}...wondering if free will exists...{COLORS['clear']}")

def main():
    quote = (
        "The meaning of life? \n\n"
        "It's like looking for a match under a mattress\n"
        "in a hotel room after being informed\n"
        "that one's room - and possibly one's existence -\n"
        "has been cancelled. \n\n"
        "And anyway, matches cause cancer."
    )
    author = "— Woody Allen (probably)"

    print("\n" * 3)  # Add some space at the top
    
    # Animate entrance
    typewriter("Initializing Existential Crisis...", delay=0.03, color="blue")
    time.sleep(0.5)
    spinning_cursor()
    print("\n")
    time.sleep(0.8)

    # ASCII art people
    draw_people()
    print("\n" * 2)
    time.sleep(1.2)

    # Type out the quote with dramatic pauses
    print(f"{COLORS['bold']}A moment of profound wisdom approaches...{COLORS['clear']}")
    time.sleep(1.5)
    
    create_quote_box(quote, author)
    print("\n")

    # Final thought
    typewriter("Philosophically yours,", delay=0.06, color="magenta")
    typewriter("…or at least for now.", delay=0.06, color="magenta")
    time.sleep(0.8)
    
    # Blinking dots (like a nervous tic)
    for i in range(5):
        sys.stdout.write(f"{COLORS['blink']}{COLORS['yellow']}...{COLORS['clear']}")
        sys.stdout.flush()
        time.sleep(0.5 if i < 4 else 1.5)
    
    print("\n\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{COLORS['red']}Philosophy interrupted by basic anxiety!{COLORS['clear']}\n")
        sys.exit(0)