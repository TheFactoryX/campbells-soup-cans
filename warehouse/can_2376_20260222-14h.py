"""
Campbell's Soup Can #2376
Produced: 2026-02-22 14:45:45
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_colored(text, color_code):
    """Print text in specified color using ANSI escape codes."""
    print(f"\033[{color_code}m{text}\033[0m")

def animate_text(text, delay=0.05):
    """Animate text by printing one character at a time."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def draw_woody_face():
    """Draw a simple ASCII art of Woody Allen's face."""
    print_colored("""
         ╭─────╮
        ╱       ╲
       │  •   •  │
       │    │    │
        ╲   .   ╱
         ╰─────╯
    """, 33)  # Yellow color

def main():
    # Draw Woody Allen's face
    draw_woody_face()
    time.sleep(1)

    # Print the quote with animation
    quote = """
I don't want to achieve immortality through my work;
I want to achieve it through not dying.

Also, I'm not afraid of death; I just don't want to be there when it happens.
"""
    animate_text(quote, 0.03)

    # Print a colorful border
    print_colored("=" * 50, 32)  # Green color

if __name__ == "__main__":
    main()