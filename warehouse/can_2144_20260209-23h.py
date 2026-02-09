"""
Campbell's Soup Can #2144
Produced: 2026-02-09 23:53:43
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def typewriter(text, color_code="\033[35m", delay=0.03):
    """Typewriter effect with random neurotic pauses"""
    for char in text:
        sys.stdout.write(f"{color_code}{char}\033[0m")
        sys.stdout.flush()
        # Woody Allen would overthink each word, so random delays
        time.sleep(delay + random.uniform(-0.01, 0.02))

def clear_screen():
    """Clear screen with dramatic effect"""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def existential_crisis():
    """Main function with Woody Allen existential presentation"""
    clear_screen()
    
    # Build the dramatic framing
    border = "░" * 60
    empty_line = "░" + " " * 58 + "░"
    
    # Top border with flickering effect
    for _ in range(3):
        sys.stdout.write(f"\033[33m{border}\033[0m\n")
        time.sleep(0.1)
    
    # Empty dramatic space
    sys.stdout.write(empty_line + "\n")
    
    # Centered title with anxiety
    title = "WOODY ALLEN'S GUIDE TO NOT EXISTING"
    padding = (58 - len(title)) // 2
    sys.stdout.write("░" + " " * padding + f"\033[36m\033[1m{title}\033[0m" + " " * (58 - len(title) - padding) + "░\n")
    sys.stdout.write(empty_line + "\n\n")
    
    # The quote with multi-color anxiety
    quote_parts = [
        ("\"I'm not afraid of death;\033[31m I just don't want to be there\033[0m", 0.04),
        ("when it happens.\033[32m It's too much like a party\033[0m", 0.04),
        ("I didn't RSVP to,\033[36m and the conversation is always\033[0m", 0.04),
        ("about mortality\033[35m and the food is terrible.\033[0m\"", 0.05)
    ]
    
    # Type each part with different colors and speeds
    for part, delay in quote_parts:
        sys.stdout.write("  ")  # Indent
        typewriter(part, delay=delay)
        print()
        time.sleep(0.3)  # Nervous pause between lines
    
    print()
    sys.stdout.write(empty_line + "\n")
    
    # Bottom border with final dramatic flicker
    for i in range(3):
        flicker_color = "\033[33m" if i % 2 == 0 else "\033[33m\033[2m"
        sys.stdout.write(f"{flicker_color}{border}\033[0m\n")
        time.sleep(0.15)
    
    # Post-script existential footnote
    time.sleep(0.5)
    footnote = "\033[90m[ Footnote: This quote probably won't age well. Nothing does. ]\033[0m"
    sys.stdout.write(" " * ((60 - len(footnote) - 4) // 2) + footnote + "\n")
    
    # Final blinking cursor effect
    for _ in range(5):
        sys.stdout.write("\033[?25l")  # Hide cursor
        sys.stdout.write("\033[33m░\033[0m")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\b \b")  # Backspace and erase
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\033[?25h")  # Show cursor
    print("\n")

if __name__ == "__main__":
    try:
        existential_crisis()
    except KeyboardInterrupt:
        # Woody Allen would probably interrupt himself anyway
        print("\n\n\033[33m[Interrupted. How appropriate. We were just getting to the good part.]\033[0m")