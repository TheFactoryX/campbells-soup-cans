"""
Campbell's Soup Can #2938
Produced: 2026-03-24 06:14:01
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI escape codes for colors
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.03, color=Colors.WHITE, end='\n'):
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)

def blink(text, delay=0.5, times=3, color=Colors.MAGENTA):
    for _ in range(times):
        sys.stdout.write(color + text + Colors.END)
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write(' ' * len(text))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(color + text + Colors.END)
    sys.stdout.flush()
    print()

def draw_frame(width=70):
    print(Colors.CYAN + "+" + "-" * (width - 2) + "+" + Colors.END)
    for _ in range(5):
        print(Colors.CYAN + "|" + " " * (width - 2) + "|" + Colors.END)
    print(Colors.CYAN + "+" + "-" * (width - 2) + "+" + Colors.END)

def main():
    clear_screen()
    
    # Woody Allen's head in ASCII art
    woody_head = [
        Colors.YELLOW + "       .-.       " + Colors.END,
        Colors.YELLOW + "      ( o )      " + Colors.END,
        Colors.YELLOW + "      /|\\|\\      " + Colors.END,
        Colors.YELLOW + "     / | | |     " + Colors.END,
        Colors.YELLOW + "    /  |_|_|\\    " + Colors.END,
        Colors.YELLOW + "   (____|____)   " + Colors.END,
    ]
    
    # Quote
    quote = """
    "I've spent my entire life terrified of death, not because 
    I'm afraid of what comes after - frankly, that's just more 
    anxiety I don't need - but because I just realized that if 
    I die, I'll have to stop overthinking everything and making 
    elaborate excuses for not living. What a tragedy that would be!"
    """
    
    # Author
    author = "- Woody Allen"
    
    # Display
    print("\n" * 1)
    
    # Animate Woody's head
    for line in woody_head:
        typewriter(line, delay=0.04, color=Colors.YELLOW)
    
    time.sleep(0.5)
    
    # Draw frame
    draw_frame()
    time.sleep(0.3)
    
    # Display quote with typewriter effect
    print(Colors.CYAN + "|" + Colors.END + " " * 68 + Colors.CYAN + "|" + Colors.END)
    typewriter(Colors.CYAN + "|" + Colors.END + " " * 25 + Colors.BOLD + Colors.ITALIC + Colors.WHITE, delay=0.01, end='')
    
    # Quote lines
    quote_lines = quote.split("\n")
    for line in quote_lines:
        typewriter(" " + line, delay=0.02, color=Colors.WHITE)
    
    typewriter(Colors.CYAN + "|" + Colors.END + " " * 25 + Colors.BOLD + Colors.ITALIC + Colors.WHITE, delay=0.01, end='')
    print(Colors.CYAN + "|" + Colors.END + " " * 68 + Colors.CYAN + "|" + Colors.END)
    time.sleep(0.3)
    
    # Draw bottom of frame
    draw_frame()
    time.sleep(0.5)
    
    # Display author with blinking effect
    blink(author, delay=0.4, times=3, color=Colors.MAGENTA)
    
    time.sleep(1)
    print("\n" * 2)

if __name__ == "__main__":
    main()