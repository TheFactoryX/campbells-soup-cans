"""
Campbell's Soup Can #5257
Produced: 2026-11-19 03:28:50
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os
import sys

# ANSI color codes
class Colors:
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_writer(text, delay=0.05, color=Colors.YELLOW):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_border(width, color=Colors.CYAN):
    """Print a decorative border"""
    border = "═" * width
    print(color + "╔" + border + "╗" + Colors.RESET)

def print_quote():
    quote = (
        "I'm not actually afraid of death. I'm just not enthusiastic about being dead. "
        "It's the uncertainty that really gets me. I mean, what if I die and there's nothing after? "
        "Then I've spent my entire life being neurotic, anxious, and misanthropic for absolutely nothing. "
        "And the worst part? I'll probably still find something to complain about in the afterlife."
    )
    
    author = "— Woody Allen (probably)"
    
    # Calculate padding for centering
    max_width = 70
    words = quote.split()
    lines = []
    current_line = []
    current_length = 0
    
    # Word wrap the quote
    for word in words:
        if current_length + len(word) + 1 <= max_width:
            current_line.append(word)
            current_length += len(word) + 1
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(" ".join(current_line))
    
    # Print the border
    print_border(max_width + 4)
    
    # Print title
    title = "A WOODY ALLEN STYLE PHILOSOPHICAL QUOTE"
    padding = (max_width - len(title)) // 2
    print(Colors.CYAN + "║ " + Colors.YELLOW + Colors.BOLD + 
          " " * padding + title + " " * padding + Colors.CYAN + " ║" + Colors.RESET)
    
    # Print empty line
    print(Colors.CYAN + "║" + " " * (max_width + 2) + "║" + Colors.RESET)
    
    # Print the quote with typewriter effect
    for line in lines:
        padding = (max_width - len(line)) // 2
        sys.stdout.write(Colors.CYAN + "║ " + Colors.YELLOW)
        sys.stdout.flush()
        
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        
        print(Colors.CYAN + " " * (max_width - len(line) - padding) + "║" + Colors.RESET)
        time.sleep(0.2)
    
    # Print empty line
    print(Colors.CYAN + "║" + " " * (max_width + 2) + "║" + Colors.RESET)
    
    # Print author
    author_padding = (max_width - len(author)) // 2
    print(Colors.CYAN + "║ " + Colors.MAGENTA + Colors.BOLD + 
          " " * author_padding + author + " " * author_padding + 
          Colors.CYAN + "║" + Colors.RESET)
    
    # Print bottom border
    print(Colors.CYAN + "╚" + "═" * max_width + "╝" + Colors.RESET)

def main():
    clear_screen()
    
    # Animated intro
    print(Colors.YELLOW + "\n" + "=" * 70)
    print(Colors.YELLOW + "PRESENTING: A TYPICALLY NEUROTIC EXISTENTIAL CRISIS")
    print(Colors.YELLOW + "=" * 70 + "\n")
    
    time.sleep(1)
    
    # Print the quote
    print_quote()
    
    # Add some philosophical anxiety at the end
    print("\n" + Colors.RED + "P.S.: I'm probably overthinking this entire presentation. "
          "What if the colors are too bright? What if you're judging my coding choices? "
          "What if there's no meaning to any of this... including this sentence?" + Colors.RESET)
    
    print(Colors.YELLOW + "\n" + "=" * 70 + Colors.RESET)

if __name__ == "__main__":
    main()