"""
Campbell's Soup Can #5129
Produced: 2026-10-18 18:06:26
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
import random

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ANSI color codes
class Colors:
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# Woody Allen style quote
quote = "I'm not afraid of dying, I'm just not enthusiastic about the process. It's like being forced to attend a mandatory staff meeting that lasts eternity - and the coffee is terrible."

# Split quote into lines for better formatting
def split_text(text, width=50):
    words = text.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= width:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    
    if current_line:
        lines.append(current_line.strip())
    
    return lines

# Create a fancy box around the text
def create_box(lines, width=60):
    border_top = "┌" + "─" * (width - 2) + "┐"
    border_bottom = "└" + "─" * (width - 2) + "┘"
    
    box_lines = [border_top]
    
    # Empty line at top
    box_lines.append("│" + " " * (width - 2) + "│")
    
    # Text lines
    for line in lines:
        padding = width - 2 - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        box_lines.append("│" + " " * left_pad + line + " " * right_pad + "│")
    
    # Empty line at bottom
    box_lines.append("│" + " " * (width - 2) + "│")
    box_lines.append(border_bottom)
    
    return box_lines

# Typewriter effect
def typewriter_print(text, delay=0.03, color=Colors.YELLOW):
    for char in text:
        print(color + char + Colors.RESET, end='', flush=True)
        time.sleep(delay)
    print()

# Blinking cursor effect
def blinking_cursor(duration=1.0):
    start_time = time.time()
    while time.time() - start_time < duration:
        print(Colors.CYAN + "█" + Colors.RESET, end='', flush=True)
        time.sleep(0.5)
        print("\r ", end='', flush=True)
        time.sleep(0.5)

# Main function
def main():
    clear_screen()
    
    # Print title
    print(Colors.BOLD + Colors.MAGENTA)
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                  WOODY ALLEN'S EXISTENTIAL CORNER           ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print(Colors.RESET)
    
    time.sleep(1)
    
    # Blinking cursor
    print(Colors.GREEN + "Thinking" + Colors.RESET, end='')
    blinking_cursor(1.5)
    print()
    
    # Split and format quote
    lines = split_text(quote)
    box = create_box(lines)
    
    # Print box with typewriter effect
    for i, line in enumerate(box):
        if i == 0 or i == len(box) - 1:  # Borders
            print(Colors.BLUE + line + Colors.RESET)
        elif line.strip() == "│" + " " * (len(line) - 2) + "│":  # Empty lines
            print(Colors.BLUE + line + Colors.RESET)
        else:  # Text lines
            print(Colors.BLUE + "│" + Colors.RESET, end='')
            typewriter_print(line[1:-1], delay=0.02)
            print(Colors.BLUE + "│" + Colors.RESET)
        
        time.sleep(0.1)
    
    # Add some Woody Allen style commentary
    print()
    print(Colors.RED + "─" * 60 + Colors.RESET)
    print(Colors.BOLD + "According to my therapist:" + Colors.RESET)
    print(Colors.YELLOW + "\"You're projecting your fear of mortality onto existential philosophy.\"" + Colors.RESET)
    print(Colors.RED + "─" * 60 + Colors.RESET)
    
    # Final existential thought
    print()
    print(Colors.CYAN + "P.S. I wrote this quote during a particularly existential bout of insomnia. "
                       "At least I think I wrote it. Maybe it wrote me." + Colors.RESET)
    
    # Random existential fact
    facts = [
        "Fact: The average person spends 30 years of their life sleeping. That's basically a third of your existence spent in a coma-like state.",
        "Fact: There are more trees on Earth than stars in the Milky Way. But somehow, we still feel alone.",
        "Fact: Your body replaces every cell in your body every 7 years. So technically, you're not the same person who started reading this.",
        "Fact: The universe is expanding. Eventually, all stars will burn out. But don't worry, we'll probably destroy ourselves long before that."
    ]
    
    print(Colors.MAGENTA + random.choice(facts) + Colors.RESET)

if __name__ == "__main__":
    main()