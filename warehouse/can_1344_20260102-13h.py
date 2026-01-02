"""
Campbell's Soup Can #1344
Produced: 2026-01-02 13:45:14
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import random
import sys
import time

# ANSI Escape Sequences
class ANSI:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    
    # 8-bit Colors
    RED = "\033[31m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GRAY = "\033[90m"

def clear_screen():
    # Clear screen and hide cursor
    sys.stdout.write("\033[2J\033[?25l")
    sys.stdout.flush()

def reset_terminal():
    # Show cursor and reset
    sys.stdout.write("\033[?25h" + ANSI.RESET)
    sys.stdout.flush()

def get_quote():
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "My brain is the second biggest organ in my body... and it has a mind of its own.",
        "I love nature, but I don't want to get it all over me.",
        "If it turns out that there is a God, I don't think he's evil. I think he's just a really disorganized planner.",
        "I was nauseous and tingly all over. I was either having a stroke or falling in love. I decided against it.",
        "The odds of being killed by a coconut are low, but they're not zero. I prefer to stay indoors.",
        "Time is a great teacher, but unfortunately it kills all its pupils.",
        "I'm profoundly superficial."
    ]
    return random.choice(quotes)

def draw_box(text, width=60):
    """
    Wraps text inside a fancy ASCII box with decorations.
    """
    # Word wrap logic
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        # +1 for space
        if current_length + len(word) + (1 if current_line else 0) <= width - 4:
            current_line.append(word)
            current_length += len(word) + (1 if current_line else 0)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)
    if current_line:
        lines.append(" ".join(current_line))
        
    # Calculate box height
    height = len(lines) + 2
    
    # Top border
    top = f"{ANSI.GRAY}╔{'═' * (width - 2)}╗{ANSI.RESET}"
    bottom = f"{ANSI.GRAY}╚{'═' * (width - 2)}╝{ANSI.RESET}"
    side = f"{ANSI.GRAY}║{ANSI.RESET}"
    
    # Animation Sequence
    clear_screen()
    
    # 1. Draw the empty box with a "loading" thought bubble
    sys.stdout.write(f"\n{' ' * 5}{ANSI.GRAY}Thinking...{ANSI.RESET}\n\n")
    sys.stdout.flush()
    time.sleep(0.5)
    
    sys.stdout.write(top + "\n")
    
    # Draw a placeholder loading line
    sys.stdout.write(side + f" {ANSI.CYAN}Filtering neurotic thoughts...{ANSI.RESET}{' ' * (width - 28 - 4)}" + side + "\n")
    
    # Draw the rest of the empty box
    for _ in range(height - 1):
        sys.stdout.write(side + " " * (width - 2) + side + "\n")
    
    sys.stdout.write(bottom)
    sys.stdout.flush()
    time.sleep(0.5)
    
    # 2. Redraw with text, but simulate typing line by line
    clear_screen()
    sys.stdout.write("\n") # Top padding
    
    # Draw Top
    sys.stdout.write(top + "\n")
    
    # Draw Empty top padding
    sys.stdout.write(side + " " * (width - 2) + side + "\n")
    
    # Draw Lines with Typewriter Effect
    for line in lines:
        # Center the text
        padding_len = (width - 4) - len(line)
        left_pad = padding_len // 2
        right_pad = padding_len - left_pad
        
        # Construct the line with color
        content = f" {ANSI.ITALIC}{ANSI.WHITE}{line}{ANSI.RESET} "
        final_line = f"{side}{' ' * left_pad}{content}{' ' * right_pad}{side}"
        
        sys.stdout.write(final_line + "\n")
        sys.stdout.flush()
        time.sleep(0.1 + random.uniform(0.05, 0.15)) # Random typing rhythm
        
    # Draw Empty bottom padding
    sys.stdout.write(side + " " * (width - 2) + side + "\n")
    
    # Draw Bottom
    sys.stdout.write(bottom + "\n")
    
    # 3. Add a "signature" cursor animation at the bottom
    signature_text = f"{ANSI.YELLOW}~ W. Allen (via Python) {ANSI.RESET}"
    sys.stdout.write(" " * (width // 2 - 10))
    sys.stdout.flush()
    
    for char in signature_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
        
    sys.stdout.write("\n\n")

def main():
    try:
        quote = get_quote()
        draw_box(quote)
    except KeyboardInterrupt:
        pass
    finally:
        reset_terminal()

if __name__ == "__main__":
    main()