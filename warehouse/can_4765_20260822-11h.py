"""
Campbell's Soup Can #4765
Produced: 2026-08-22 11:34:43
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
🌈✨ Philosophical Anxiety Delivery System v1.0 ✨🌈
A Woody Allen-style existential crisis, beautifully packaged.
No external dependencies required - pure Python joy! 🎨
"""

import sys
import time
import random

# ─────────────────────────────────────────────────────────
# ANSI Color Palette - Because monochrome sadness is so 1999
# ─────────────────────────────────────────────────────────
class Colors:
    RED       = "\033[91m"
    GREEN     = "\033[92m"
    YELLOW    = "\033[93m"
    BLUE      = "\033[94m"
    MAGENTA   = "\033[95m"
    CYAN      = "\033[96m"
    BOLD      = "\033[1m"
    DIM       = "\033[2m"
    ITALIC    = "\033[3m"
    UNDERLINE = "\0st32m"
    BLINK     = "\033[5m"
    RESET     = "\033[0m"
    
    # Gradient helpers
    @staticmethod
    def gradient_text(text, colors):
        """Apply a color gradient across text"""
        result = ""
        n = len(colors)
        segment = max(1, len(text) // n)
        for i, char in enumerate(text):
            idx = min(i // segment, n - 1)
            result += colors[idx] + char
        return result + Colors.RESET

# ─────────────────────────────────────────────────────────
# The Existential Quote Generator
# ─────────────────────────────────────────────────────────
QUOTE = (
    "I've been worrying about the meaning of life for so long, "
    "I'm pretty sure my anxiety has its own anxiety. "
    "Turns out the real punchline isn't that life is meaningless— "
    "it's that I paid good money for a philosophy degree "
    "and all I got was this lousy existential crisis and "
    "a therapist who charges $200 an hour to tell me "
    "exactly what I already knew in the first place: "
    "nothing matters, especially not the fact that nothing matters."
)

AUTHOR = "— A Neurotic AI channeling Woody Allen"

# ─────────────────────────────────────────────────────────
# Typewriter Animation Engine
# ─────────────────────────────────────────────────────────
def typewriter(text, delay=0.03, color=None, end="\n"):
    """Print text with a typewriter effect"""
    colors = [Colors.CYAN, Colors.MAGENTA, Colors.YELLOW, Colors.GREEN, Colors.BLUE]
    for i, char in enumerate(text):
        if color:
            print(color + char, end="", flush=True)
        else:
            # Cycle through colors for a disco effect
            c = colors[i % len(colors)]
            print(c + char, end="", flush=True)
        # Vary delay slightly for natural feel
        actual_delay = delay + random.uniform(-0.005, 0.005)
        if char in ".,!?;:":
            time.sleep(actual_delay * 3)  # Pause longer at punctuation
        elif char == " ":
            time.sleep(actual_delay * 0.5)  # Shorter pause at spaces
        else:
            time.sleep(actual_delay)
    print(Colors.RESET + end, end="")

# ─────────────────────────────────────────────────────────
# ASCII Art Collection - tiny existential crisis illustrations
# ─────────────────────────────────────────────────────────
def draw_thinking_emoji():
    """Draw a colorful thinking emoji"""
    print(Colors.YELLOW + r"""
         .-~~~~~-.
       .'  o   o  `.
      |     ^     |
      |   \___/   |
       '.       .'
         '-...-'
    """ + Colors.RESET)

def draw_philosopher_hat():
    """Draw a tophat with existential dread"""
    print(Colors.MAGENTA + r"""
         _____
        /_____\
       | _____ |
       ||     ||  __
       ||     || |  |
       |_______| |  |
       |_______| |  |
        |  |  |  |  |
        |  |  |  |  |
        |__|__|__|__|
         |  |  |  |
        /   |  |   \
    """ + Colors.RESET)

def draw_anxiety_spiral():
    """Draw a spiral representing the endless cycle of worry"""
    spiral = r"""
              .-~~-.
           .- ~ ~ - .
          / ~  WORRY ~ \
         | ~ ~ ~ ~ ~ ~ ~ |
          \ ~ ~ ~ ~ ~ ~ /
           ~ - . . - ~
              | | |
             _| | |_
            (_____|_)
    """
    spiral_lines = spiral.strip("\n").split("\n")
    colors = [Colors.RED, Colors.MAGENTA, Colors.CYAN, Colors.YELLOW]
    for line in spiral_lines:
        c = random.choice(colors)
        print(c + line + Colors.RESET)
        time.sleep(0.1)

# ─────────────────────────────────────────────────────────
# Box Drawing with Style
# ─────────────────────────────────────────────────────────
def draw_styled_box(text_lines, title="EXISTENTIAL CRISIS DELUXE"):
    """Draw a fancy box around text with a title"""
    width = max(len(line) for line in text_lines + [title]) + 6
    
    # Top border with animation
    top_colors = [Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
    print(Colors.CYAN + "╔" + "═" * width + "╗")
    
    # Title
    title_centered = title.center(width)
    print("║" + Colors.BOLD + Colors.YELLOW + title_centered + Colors.RESET + "║")
    
    # Middle border
    middle = Colors.CYAN + "╠" + "─" * width + "╣"
    print(middle + Colors.RESET)
    
    # Content lines
    for line in text_lines:
        padded = "  " + line.ljust(width - 6) + "  "
        inner_width = width - 4
        c = random.choice([Colors.GREEN, Colors.YELLOW, Colors.CYAN])
        print("║" + c + padded + Colors.RESET + "║")
    
    # Bottom border
    print(Colors.CYAN + "╚" + "═" * width + "╝" + Colors.RESET)

# ─────────────────────────────────────────────────────────
# Main Event: The Existential Show
# ─────────────────────────────────────────────────────────
def main():
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Dramatic intro
    print(Colors.BOLD + Colors.RED + "\n\n" + "★·.·★ PHILOSOPHICAL ANXIETY DELIVERY SYSTEM ★·.·★" + Colors.RESET)
    print(Colors.DIM + "Initializing existential dread module..." + Colors.RESET)
    time.sleep(1)
    
    # Show some art
    draw_thinking_emoji()
    time.sleep(0.5)
    
    # Build the quote into lines for the box
    quote_lines = []
    current_line = ""
    for word in QUOTE.split():
        if len(current_line + word) > 55:
            quote_lines.append(current_line)
            current_line = word
        else:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
    if current_line:
        quote_lines.append(current_line)
    
    # Draw the fancy box
    draw_styled_box(quote_lines)
    time.sleep(0.5)
    
    # Show the anxiety spiral
    draw_anxiety_spiral()
    time.sleep(0.3)
    
    # The dramatic typewriter reveal
    print(Colors.BOLD + Colors.RED + "\n\n" + "=" * 60 + Colors.RESET)
    print(Colors.ITALIC, end="")
    typewriter(QUOTE, delay=0.04, color=Colors.CYAN)
    print(Colors.RESET + Colors.BOLD + Colors.RED + "\n" + "=" * 60 + Colors.RESET)
    
    # Author line
    time.sleep(0.3)
    print(Colors.YELLOW + "\n  " + AUTHOR + Colors.RESET)
    
    # Final flourish
    draw_philosopher_hat()
    time.sleep(0.5)
    
    # Bounce message
    print(Colors.BOLD + Colors.MAGENTA + "\n\n  💫 Remember: The answer is 42, " + 
          Colors.CYAN + "but the question is probably wrong. 💫\n" + Colors.RESET)

if __name__ == "__main__":
    main()