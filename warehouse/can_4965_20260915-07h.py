"""
Campbell's Soup Can #4965
Produced: 2026-09-15 07:45:24
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random
import math

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'

def type_text(text, delay=0.03, color=Colors.WHITE):
    """Animate text typing effect with color."""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_centered(text, color=Colors.WHITE):
    """Print centered text in the terminal."""
    try:
        width = shutil.get_terminal_size().columns
    except:
        width = 60
    print(color + text.center(width) + Colors.RESET)

def thinking_dots(duration=2):
    """Animate thinking dots."""
    for i in range(duration * 4):
        dots = "." * (i % 4)
        sys.stdout.write(Colors.YELLOW + "   Woody is thinking" + dots + "  " + Colors.RESET)
        sys.stdout.flush()
        time.sleep(0.25)
        sys.stdout.write("\r" + " " * 40 + "\r")
        sys.stdout.flush()

def draw_border(text_lines, color=Colors.CYAN):
    """Draw a decorative box around text."""
    max_len = max(len(line) for line in text_lines)
    width = max_len + 4
    
    print(color + "╔" + "═" * width + "╗" + Colors.RESET)
    for line in text_lines:
        padded = line.ljust(max_len)
        print(color + "║  " + padded + "  ║" + Colors.RESET)
    print(color + "╚" + "═" * width + "╝" + Colors.RESET)

def neurotic_spiral():
    """Draw a neurotic ASCII spiral."""
    colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.MAGENTA]
    spiral = [
        "        .-~~~~~-.",
        "      .'         '.",
        "     /   O     O   \\",
        "    |      \\___/    |",
        "     \\  \\___/___/  /",
        "      '.         .'",
        "        '-...-'"
    ]
    for i, line in enumerate(spiral):
        print(colors[i % len(colors)] + line.center(50) + Colors.RESET)
        time.sleep(0.1)

def main():
    # Clear screen (works on most terminals)
    print("\033[2J\033[H")
    
    # Header with colors
    print(Colors.BOLD + Colors.MAGENTA)
    print("╔══════════════════════════════════════════════════╗")
    print("║     🎭  WOODY ALLEN'S EXISTENTIAL CRISIS  🎭    ║")
    print("╚══════════════════════════════════════════════════╝" + Colors.RESET)
    print()
    
    # Woody Allen's neurotic face
    neurotic_spiral()
    print()
    
    # Collection of Woody Allen style quotes
    quotes = [
        ("I'm not afraid of death; I just don't want to be there when it happens.", Colors.RED),
        ("Life is full of misery, loneliness, and suffering - and it's all over much too soon.", Colors.YELLOW),
        ("I don't want to achieve immortality through my work; I want to achieve it through not dying.", Colors.GREEN),
        ("The subconscious is the subconscious. It doesn't change its mind. There is no point in fighting it.", Colors.CYAN),
        ("I would not want to belong to any club that would have someone like me for a member.", Colors.MAGENTA),
        ("I'm not depressed, I'm just in a bad mood... permanently.", Colors.BLUE),
        ("To you, I'm an atheist; to God, I'm the Loyal Opposition.", Colors.RED),
        ("Love is the answer, but while you're waiting for the answer, sex raises some pretty interesting questions.", Colors.YELLOW),
        ("I'm against animal testing. I'm against all testing, period. Mice and rats, people, Asians - it's all the same.", Colors.GREEN),
        ("Eighty percent of success is showing up. The other twenty percent is showing up sober.", Colors.CYAN),
    ]
    
    # Pick a random quote
    quote, color = random.choice(quotes)
    
    # Animated thinking
    thinking_dots(1.5)
    
    # Print the quote with box
    print()
    quote_lines = quote.split('. ')
    wrapped = []
    for q in quote_lines:
        if len(q) > 50:
            # Simple word wrap
            words = q.split()
            line = ""
            for word in words:
                if len(line + " " + word) <= 50:
                    line += (" " if line else "") + word
                else:
                    wrapped.append(line)
                    line = word
            if line:
                wrapped.append(line)
        else:
            wrapped.append(q)
    
    draw_border(wrapped, Colors.DIM + Colors.CYAN)
    print()
    
    # Animate the quote character by character with color cycling
    print("  " + Colors.BOLD + "💭  Quote of the moment:" + Colors.RESET)
    print()
    
    color_cycle = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.MAGENTA, Colors.BLUE]
    for i, char in enumerate(quote):
        c = color_cycle[i % len(color_cycle)]
        sys.stdout.write(c + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(0.02)
    print()
    print()
    
    # Footer
    print(Colors.DIM + "─" * 50 + Colors.RESET)
    type_text("  - Woody Allen (probably overthinking this)", 0.05, Colors.YELLOW)
    print()
    print(Colors.DIM + "  Press Enter to exit..." + Colors.RESET)
    input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + Colors.RED + "See? Even interrupting is existential crisis!")