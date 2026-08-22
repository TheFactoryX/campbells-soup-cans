"""
Campbell's Soup Can #4759
Produced: 2026-08-22 05:42:30
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_slow(text, delay=0.03, end="\n"):
    """Print text character by character with a delay for animation effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def create_box(text, width=70):
    """Create a decorative box around the text."""
    border = "═"
    corner = "╔"
    corner_end = "╗"
    side = "║"
    
    # Wrap text to fit within box
    words = text.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= width - 4:
            current_line += (" " if current_line else "") + word
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    # Center each line
    centered_lines = [line.center(width - 4) for line in lines]
    
    # Build the box
    box_lines = []
    box_lines.append(corner + border * (width - 2) + corner_end)
    
    for line in centered_lines:
        box_lines.append(side + " " + "\033[33m" + line + "\033[0m" + " " + side)
    
    box_lines.append(corner + border * (width - 2) + corner_end)
    
    return box_lines

def main():
    # Clear screen for better animation
    print("\033[2J\033[H", end="")
    
    # Woody Allen style quote
    quote = "I don't mind being dead. I just don't want to be there when it happens. And by the way, I don't mind being alive either, but it's a lot of work - mostly involving worrying about whether I'm wearing the right socks for existential despair."
    
    # Create the box
    box = create_box(quote, width=72)
    
    # Print with animation
    print("\033[36m")  # Cyan color for the box
    for line in box:
        print_slow(line, delay=0.05)
    
    # Add some extra philosophical musings
    print("\n\033[35m")  # Magenta color
    print_slow("* Woody Allen's existential crisis *", delay=0.1)
    print_slow("\n* Overthinking since 1935 *", delay=0.1)
    print_slow("\n* Professional neurotic *", delay=0.1)
    
    # Reset colors
    print("\033[0m")
    
    # Final touch - a nervous laugh
    print_slow("\n\nHa... ha... maybe?", delay=0.2)

if __name__ == "__main__":
    main()