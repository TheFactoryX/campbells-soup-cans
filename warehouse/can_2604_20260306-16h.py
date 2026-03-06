"""
Campbell's Soup Can #2604
Produced: 2026-03-06 16:59:36
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# Colors for that classic neurotic Woody Allen vibe
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_woody_quote():
    # Clear screen for dramatic effect
    sys.stdout.write('\033[H\033[J')
    sys.stdout.flush()
    
    # The quote that's been keeping me up at night
    quote = "I'm not afraid of death; I just don't want to be there when it happens. (Though I'll probably be late anyway.)"
    inner_width = 60
    total_width = inner_width + 2
    
    # Calculate centering for maximum existential angst
    if len(quote) > inner_width:
        quote = quote[:inner_width-3] + "..."
    leading_spaces = max(0, (inner_width - len(quote)) // 2)
    
    # Build the anxiety-inducing box
    top = '═' * total_width
    side = '║'
    empty_line = side + ' ' * inner_width + side
    
    # Print the frame with nervous energy
    print(BLUE + "  " + top)
    print(BLUE + "  " + empty_line)
    print(BLUE + "  " + empty_line)
    print(BLUE + "  " + empty_line)
    print(BLUE + "  " + empty_line)
    print(BLUE + "  " + top + RESET)
    
    # Move cursor to quote position with neurotic hesitation
    sys.stdout.write(f'\033[5A\033[4C\033[{1+leading_spaces}C')
    sys.stdout.flush()
    
    # Type quote character by character like I'm having an existential crisis
    sys.stdout.write(YELLOW + BOLD)
    for char in quote:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03 + 0.02 * (0.5 - time.time() % 1))  # Random jitter for anxiety
    
    # Add Woody's signature visual flourish
    time.sleep(0.5)
    sys.stdout.write(RESET)
    sys.stdout.write(f'\033[2A\033[2C')
    sys.stdout.flush()
    
    # Print the iconic neurotic glasses (ASCII art with color)
    glasses = [
        "  " + BLUE + "╭" + "─" * 25 + "╮" + RESET,
        "  " + BLUE + "│ " + YELLOW + "o" + " " * 22 + "o" + BLUE + " │" + RESET,
        "  " + BLUE + "╰" + "─" * 25 + "╯" + RESET
    ]
    
    for line in glasses:
        sys.stdout.write(f'\033[1B\033[2D')  # Move down and left
        sys.stdout.write(line)
        sys.stdout.flush()
        time.sleep(0.1)
    
    # Add final nervous tick
    sys.stdout.write(f'\033[1B\033[28C{YELLOW}*sigh*{RESET}')
    sys.stdout.flush()

# Run the existential crisis generator
print_woody_quote()

# Keep the terminal from closing too quickly for the anxious among us
time.sleep(2)