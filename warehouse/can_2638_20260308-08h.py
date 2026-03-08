"""
Campbell's Soup Can #2638
Produced: 2026-03-08 08:48:24
Worker: TheDrummer: Cydonia 24B V4.1 (thedrummer/cydonia-24b-v4.1)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

def type_writer(text, speed=0.05, color="\033[93m"):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(speed)
    print("\033[0m")

def create_bubble(text):
    bubble = []
    border_col = "\033[35m"
    text_col = "\033[36m"
    reset_col = "\033[0m"
    
    # Calculate the width needed
    max_len = max(len(line) for line in text.split('\n'))
    
    # Create top border
    top = f" {border_col}{' ' * max_len}{reset_col}"
    bubble.append(top)
    
    for line in text.split('\n'):
        # Add left border and text
        formatted = f"{border_col}|{reset_col} {text_col}{line.ljust(max_len)}{reset_col} {border_col}|{reset_col}"
        bubble.append(formatted)
        
    # Create bottom border
    bottom = f" {border_col}{' ' * max_len}{reset_col}"
    bubble.append(bottom)
    
    # Add speech lines
    lines = ["  ", "  ", "  "]
    
    # Assemble the bubble with speech lines
    result = []
    for i, line in enumerate(lines):
        bubble_line = bubble[i] if i < len(bubble) else ""
        result.append(f"{bubble_line}  ")
    
    return '\n'.join(result)

# Woody Allen's quote
quote = "Life is divided into the horror and the misery, and I'm glad I'm in the latter."

# Color definitions
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[34m"
MAGENTA = "\033[95m"
CYAN = "\033[36m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Display the chat bubble with animation
print("\033c")  # Clear screen
time.sleep(0.5)

# Create the bubble
bubble = create_bubble(quote)

# Rainbow colors for each character
def rainbow_print(text):
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    result = ""
    for i, char in enumerate(text):
        color_idx = i % len(colors)
        result += f"{colors[color_idx]}{char}{RESET}"
    print(result)

# Show quote in rainbow style
print(f"{BOLD}{MAGENTA}                     ANOTHER QUALITY WOODY ALLEN MOMENT{RESET}")
print()
time.sleep(0.5)

# Show the quote with character-by-character color change
print()
rainbow_print("A Philosopher's Corner:")
print()

time.sleep(0.5)
type_writer("A character is emerging...      ", 0.2, BLUE)
time.sleep(0.5)
print()

# Show Woody Allen ASCII art
woody = f"""
{BLUE}   /\_/\{RESET}
{GREEN}  ( o.o ){RESET}
{RED}   > ^ <{RESET}
"""
print(woody)

# Add a blank line
print()

# The final magical quote reveal
for _ in range(3):
    print(f"{YELLOW}  *     *     *     *     *{RESET}")
    time.sleep(0.3)

print()
print(f"{BLUE}{BOLD}WOODY ALLEN{RESET} says...")
print()

# Display the quote in a typewriter effect with color
type_writer(quote, 0.03, BLUE)

# Final ASCII art with color
final_art = f"""
{RFD}{GREEN}    .-""""-\\
{MAGENTA}   /  o   o  \\
{YELLOW}  -(   =^^=   )-
{BLUE}    \\(  (-.)  )/
{GREEN}     '-(_,)-'\{RESET}
"""
print()
print(f"{MAGENTA}** THINKING DEEPLY **{RESET}")
print()
print(final_art)