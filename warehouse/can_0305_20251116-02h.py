"""
Campbell's Soup Can #305
Produced: 2025-11-16 02:21:52
Worker: DeepSeek: R1 Distill Llama 70B (free) (deepseek/deepseek-r1-distill-llama-70b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes for colors
COLORS = {
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'red': '\033[91m',
    'end': '\033[0m'
}

def clear_screen():
    """Clear the terminal screen."""
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

def type_text(text, speed=0.05):
    """Type text with a delay to simulate typing."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def quote_box(quote, author, color='blue'):
    """Print a quote with a box around it."""
    lines = [line for line in quote.split('\n') if line.strip() != '']
    max_length = max(len(line) for line in lines)
    border = f"{COLORS['yellow']}***************{COLORS['end']}"
    print(f"{COLORS['yellow']}******************************{COLORS['end']}")
    for line in lines:
        padded_line = line.center(max_length + 4)
        print(f"{COLORS['yellow']}* {COLORS[color]}{padded_line}{COLORS['yellow']} *{COLORS['end']}")
    print(f"{COLORS['yellow']}******************************{COLORS['end']}")
    time.sleep(1)
    print(f"\n{COLORS['red']}— {author}{COLORS['end']}")

def main():
    clear_screen()
    quote = "I'm not afraid of existence;\nI just don't want to be there\nwhen it runs out of coffee."
    author = "Woody Alien"
    print(f"{COLORS['blue']}\n")
    type_text("Thinking deeply about life's mysteries...", 0.1)
    time.sleep(1)
    print("\n")
    quote_box(quote, author)
    
if __name__ == "__main__":
    main()