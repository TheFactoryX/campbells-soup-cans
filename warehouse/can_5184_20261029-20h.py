"""
Campbell's Soup Can #5184
Produced: 2026-10-29 20:18:23
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_with_delay(text, delay=0.03, end='\n'):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(end, end='')

def create_box(text, width=60):
    """Create a styled box around text."""
    # ANSI color codes
    RESET = '\033[0m'
    BOLD = '\033[1m'
    BLUE_BG = '\033[44m'
    YELLOW_FG = '\033[33m'
    RED_FG = '\033[31m'
    
    # Wrap text to fit box width
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + 1 <= width - 8:  # Account for padding and borders
            current_line.append(word)
            current_length += len(word) + 1
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(' '.join(current_line))
    
    # Create the box
    border_top = f"{BLUE_BG}{RED_FG}┌{'─' * (width - 2)}┐{RESET}"
    border_bottom = f"{BLUE_BG}{RED_FG}└{'─' * (width - 2)}┘{RESET}"
    
    result = [border_top]
    
    for line in lines:
        padding = ' ' * ((width - 2 - len(line)) // 2)
        result.append(f"{BLUE_BG}{YELLOW_FG}│ {padding}{line}{padding} │{RESET}")
    
    result.append(border_bottom)
    return '\n'.join(result)

def main():
    # Clear screen
    print('\033[2J\033[H', end='')
    
    # Woody Allen style quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens. " \
            "The real tragedy of life is that it's over too soon, and the comedy is that we have to wait so long for it to end."
    
    # Animated intro
    print_with_delay("\n" + " " * 20, 0.1)
    print_with_delay("★ ", 0.2, end='')
    print_with_delay("★ ", 0.2, end='')
    print_with_delay("★ ", 0.2)
    
    # Title
    title = "WOODY ALLEN'S WISDOM"
    print_with_delay(f"\n{title:^60}\n", 0.05)
    
    # Create and display the quote box
    box = create_box(quote)
    
    # Print box with typewriter effect
    for line in box.split('\n'):
        print_with_delay(line, 0.02)
    
    # Animated outro
    print_with_delay("\n" + " " * 20, 0.5)
    print_with_delay("☆ ", 0.2, end='')
    print_with_delay("☆ ", 0.2, end='')
    print_with_delay("☆ ", 0.2)
    
    # Final existential thought
    print_with_delay("\n\"Why are we here? What is the meaning of life?\"", 0.1)
    print_with_delay("God only knows. I'm just trying to get a good nap.\", 0.1)

if __name__ == "__main__":
    main()