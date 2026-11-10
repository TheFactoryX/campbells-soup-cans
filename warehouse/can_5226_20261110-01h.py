"""
Campbell's Soup Can #5226
Produced: 2026-11-10 01:31:38
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# ANSI color codes
class Colors:
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def print_slow(text, delay=0.03, color=Colors.YELLOW):
    """Print text with a typewriter effect"""
    for char in text:
        print(color + char + Colors.RESET, end='', flush=True)
        time.sleep(delay)
    print()

def create_box(text, width=70):
    """Create a fancy ASCII box around text"""
    lines = []
    # Top border
    top = "    " + "┌" + "─" * (width - 2) + "┐"
    lines.append(Colors.BLUE + top + Colors.RESET)
    
    # Empty line
    lines.append(Colors.BLUE + "    │" + " " * (width - 2) + "│" + Colors.RESET)
    
    # Text lines
    words = text.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= width - 6:
            current_line += word + " "
        else:
            # Center the text
            padding = (width - 2 - len(current_line)) // 2
            line = "    │" + " " * padding + current_line.strip() + " " * (width - 2 - padding - len(current_line.strip())) + "│"
            lines.append(Colors.YELLOW + line + Colors.RESET)
            current_line = word + " "
    
    # Last line
    if current_line:
        padding = (width - 2 - len(current_line)) // 2
        line = "    │" + " " * padding + current_line.strip() + " " * (width - 2 - padding - len(current_line.strip())) + "│"
        lines.append(Colors.YELLOW + line + Colors.RESET)
    
    # Empty line
    lines.append(Colors.BLUE + "    │" + " " * (width - 2) + "│" + Colors.RESET)
    
    # Bottom border
    bottom = "    " + "└" + "─" * (width - 2) + "┘"
    lines.append(Colors.BLUE + bottom + Colors.RESET)
    
    return "\n".join(lines)

def woody_allen_quote():
    """Generate a Woody Allen style quote with visual flair"""
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens. But then again, given my track record with punctuality, I'll probably show up late and miss the whole thing.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon. At least the coffee at the diner is decent, and the waitress calls me 'hon', which is more affection I've gotten in years.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying. But since that's not working out, I suppose I'll settle for being