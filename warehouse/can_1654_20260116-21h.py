"""
Campbell's Soup Can #1654
Produced: 2026-01-16 21:33:25
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random
import math

# ANSI color codes
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    
    # Foreground colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    
    # Background colors
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    
    # Bright colors
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

class Cursor:
    UP = "\033[A"
    DOWN = "\033[B"
    RIGHT = "\033[C"
    LEFT = "\033[D"
    SAVE = "\033[s"
    RESTORE = "\033[u"
    CLEAR_LINE = "\033[K"
    CLEAR_SCREEN = "\033[2J"
    HIDE = "\033[?25l"
    SHOW = "\033[?25h"

def clear_screen():
    """Clear the terminal screen"""
    print(Cursor.CLEAR_SCREEN, end="")

def hide_cursor():
    """Hide the cursor"""
    print(Cursor.HIDE, end="")

def show_cursor():
    """Show the cursor"""
    print(Cursor.SHOW, end="")

def type_text(text, delay=0.03):
    """Type out text with a typewriter effect"""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def draw_box(text, width=60, padding=2):
    """Draw a box around text with borders"""
    lines = []
    text_width = width - (padding * 2)
    
    # Wrap text
    words = text.split()
    wrapped_lines = []
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= text_width:
            current_line += word + " " if current_line else word
        else:
            if current_line:
                wrapped_lines.append(current_line)
            current_line = word
    
    if current_line:
        wrapped_lines.append(current_line)
    
    # Create box
    border_top = "╔" + "═" * (width - 2) + "╗"
    border_bottom = "╚" + "═" * (width - 2) + "╝"
    border_side = "║"
    
    lines.append(border_top)
    
    # Add empty line for top padding
    empty_line = border_side + " " * (width - 2) + border_side
    for _ in range(padding - 1):
        lines.append(empty_line)
    
    # Add text lines
    for line in wrapped_lines:
        padded_line = line.center(text_width)
        lines.append(border_side + " " * padding + padded_line + " " * (width - 2 - padding - text_width) + border_side)
    
    # Add empty line for bottom padding
    for _ in range(padding - 1):
        lines.append(empty_line)
    
    lines.append(border_bottom)
    
    return lines

def animate_quote(quote, color_scheme="dramatic"):
    """Animate the quote with various visual effects"""
    
    # Choose color scheme
    if color_scheme == "dramatic":
        colors = [Color.BRIGHT_RED, Color.BRIGHT_YELLOW, Color.BRIGHT_CYAN, Color.BRIGHT_MAGENTA]
    elif color_scheme == "neurotic":
        colors = [Color.BRIGHT_YELLOW, Color.BRIGHT_CYAN, Color.BRIGHT_GREEN, Color.BRIGHT_MAGENTA]
    else:
        colors = [Color.WHITE, Color.BRIGHT_WHITE, Color.BRIGHT_CYAN, Color.BRIGHT_YELLOW]
    
    # ASCII art frame
    frame = [
        "      .   .        .   .",
        "    .   .   .    .   .   .",
        "  .   .   .   .  .   .   .",
        "  .   .   .   .  .   .   .",
        "    .   .   .    .   .   .",
        "      .   .        .   .",
        "        . .          . .",
        "          .            ."
    ]
    
    # Special effect: swirling cursor
    def swirl_position(t, radius=5, center_x=20, center_y=10):
        x = center_x + int(radius * math.cos(t * 0.1))
        y = center_y + int(radius * math.sin(t * 0.1))
        return x, y
    
    # Clear screen and hide cursor
    clear_screen()
    hide_cursor()
    
    # Phase 1: Draw frame
    print("\n" * 3)
    for i, line in enumerate(frame):
        color = colors[i % len(colors)]
        print(" " * 20 + color + line + Color.RESET)
        time.sleep(0.1)
    
    time.sleep(0.5)
    
    # Phase 2: Draw box with animated text
    print("\n")
    
    # Create animated typing effect within a box
    box_lines = draw_box(" " * 60, width=60, padding=2)
    
    # Print box structure first
    for i, line in enumerate(box_lines):
        if i == 0 or i == len(box_lines) - 1 or "═" in line:
            print(Color.BRIGHT_CYAN + line + Color.RESET)
        else:
            print(Color.BRIGHT_MAGENTA + line + Color.RESET)
        time.sleep(0.05)
    
    # Move cursor up to the middle of the box
    print(Cursor.UP * 5, end="")
    
    # Now type the quote inside the box
    quote_chunks = []
    chunk_size = 55
    for i in range(0, len(quote), chunk_size):
        quote_chunks.append(quote[i:i+chunk_size])
    
    quote_colors = [Color.BRIGHT_YELLOW, Color.BRIGHT_GREEN, Color.BRIGHT_CYAN, Color.WHITE]
    
    # Type each chunk with effects
    for chunk_num, chunk in enumerate(quote_chunks):
        if chunk_num > 0:
            print(Cursor.LEFT * 60, end="")
            print(Cursor.DOWN, end="")
        
        # Print border
        print(Color.BRIGHT_MAGENTA + "║" + Color.RESET, end="")
        
        # Type the text
        color_idx = chunk_num % len(quote_colors)
        
        # Add some jittery typing effect
        for char in chunk:
            if char == " ":
                print(" ", end="", flush=True)
                time.sleep(random.uniform(0.01, 0.03))
            else:
                print(quote_colors[color_idx] + char + Color.RESET, end="", flush=True)
                time.sleep(random.uniform(0.03, 0.06))
        
        # Fill rest of line with spaces and print right border
        remaining = 57 - len(chunk)
        print(" " * remaining + Color.BRIGHT_MAGENTA + "║" + Color.RESET)
        time.sleep(0.2)
    
    # Bottom border
    print(Cursor.DOWN, end="")
    print(Color.BRIGHT_MAGENTA + "╚" + "═" * 58 + "╝" + Color.RESET)
    
    time.sleep(1)
    
    # Phase 3: Wiggle effect and final signature
    print("\n")
    wiggle_text = "~ WOODY ALLEN (probably) ~"
    
    # Animated wiggle
    for i in range(5):
        wiggle = wiggle_text
        if i % 2 == 0:
            wiggle = "  " + wiggle_text + "  "
        
        color = quote_colors[i % len(quote_colors)]
        print(Cursor.LEFT * 100, end="")
        print(Cursor.UP, end="")
        print(" " * 60, end="")
        print(Cursor.LEFT * 60, end="")
        print(color + wiggle + Color.RESET, end="", flush=True)
        time.sleep(0.2)
    
    print("\n")
    
    # Final flourish: glowing dots
    print(Color.BRIGHT_YELLOW, end="")
    for _ in range(10):
        x = random.randint(0, 20)
        print(" " * x + "✦", end="", flush=True)
        time.sleep(0.1)
    print(Color.RESET)
    
    time.sleep(1)
    show_cursor()

def create_animated_quote():
    """Create and display the animated philosophical quote"""
    
    # Woody Allen style philosophical quote (neurotic, self-deprecating, existential)
    quote = (
        "I'm not afraid of dying, "
        "I'm just afraid of being late for my own funeral. "
        "And I know I'll be late— "
        "I can't even make it to brunch on time."
    )
    
    # Alternative quotes for variety (randomly selected)
    alt_quotes = [
        "My biggest fear is that when I die, "
        "my body will be donated to science "
        "and science will say, 'Thanks, but no thanks.'",
        
        "I don't believe in an afterlife, "
        "but just in case there is one, "
        "I've packed my anxiety in my suitcase.",
        
        "Life is a cruel joke with no punchline, "
        "except maybe the fact that we're all "
        "pretending we know what we're doing."
    ]
    
    # Randomly choose between main quote and alternatives
    quotes = [quote] + alt_quotes
    chosen_quote = random.choice(quotes)
    
    # Choose a random color scheme
    schemes = ["dramatic", "neurotic", "trippy"]
    scheme = random.choice(schemes)
    
    return chosen_quote, scheme

def main():
    """Main function"""
    try:
        # Create the quote
        quote, scheme = create_animated_quote()
        
        # Animate it with style
        animate_quote(quote, scheme)
        
        # Add a final pause
        time.sleep(2)
        
        # Reset cursor and show it
        show_cursor()
        print(Color.RESET)
        
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        show_cursor()
        print("\n" + Color.RED + "Well, that was anticlimactic." + Color.RESET)
        sys.exit(0)
    except Exception as e:
        # Handle any other errors
        show_cursor()
        print(f"\n{Color.RED}Error: {e}{Color.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()