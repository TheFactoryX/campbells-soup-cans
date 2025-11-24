"""
Campbell's Soup Can #483
Produced: 2025-11-24 05:36:01
Worker: Qwen: Qwen3 Coder 480B A35B (free) (qwen/qwen3-coder:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def typewriter_effect(text, delay=0.03):
    """Simulate typewriter effect for text display"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_border():
    """Print a decorative border"""
    print("\033[90m" + "─" * 60 + "\033[0m")

def print_centered(text, color="\033[0m"):
    """Print text centered with optional color"""
    padding = (60 - len(text)) // 2
    print(" " * padding + color + text + "\033[0m")

def print_thought_bubble(quote):
    """Display quote in a thought bubble"""
    lines = quote.split('\n')
    max_length = max(len(line) for line in lines)
    width = max_length + 4
    
    print(" " * 20 + "\033[96m" + "┌" + "─" * (width-2) + "┐\033[0m")
    
    for line in lines:
        padding = (width - 2 - len(line)) // 2
        print(" " * 20 + "\033[96m│\033[0m" + " " * padding + line + " " * (width - 2 - len(line) - padding) + "\033[96m│\033[0m")
    
    print(" " * 20 + "\033[96m" + "└" + "─" * (width-2) + "┘\033[0m")
    print(" " * 25 + "\033[96m◢◣\033[0m")
    print(" " * 26 + "\033[96m◥◤\033[0m")

def print_anxious_brain():
    """Display a worried brain"""
    brain = [
        "    \033[95m    ___    \033[0m",
        "   \033[95m  /   \\   \033[0m",
        "  \033[95m  | ( ) |  \033[0m",
        "   \033[95m  \\___/   \033[0m",
        "  \033[95m  /  |  \\  \033[0m",
        " \033[95m  |   |   | \033[0m",
        "\033[95m   \\__|__/  \033[0m",
        "\033[91m    (___)   \033[0m ← \033[93mThis is where my thoughts live\033[0m"
    ]
    
    for line in brain:
        print(line)

def main():
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Title
    print("\033[1;93m")
    title = "WOODY ALLEN'S ANXIOUS PHILOSOPHY"
    print_centered("=" * len(title))
    print_centered(title)
    print_centered("=" * len(title))
    print("\033[0m")
    
    # Pause for effect
    time.sleep(1)
    
    # Anxious brain
    print_anxious_brain()
    print()
    
    # Pause
    time.sleep(1.5)
    
    # Philosophical quote in thought bubble
    quote = "I don't fear death itself—\nit's the thought of spending\neternity in line at the\nDMV that really terrifies me."
    
    print_thought_bubble(quote)
    print()
    
    # Author attribution with typewriter effect
    print("\033[90m" + " " * 25 + "~ Woody Allen (probably)\033[0m")
    print()
    
    # Bottom border with existential footnote
    print_border()
    print("\033[2;90m")
    footnotes = [
        "P.S. I wanted to make a profound statement about the human condition,",
        "but I'm too worried about my parking meter expiring to focus.",
        "",
        "P.P.S. This quote might be completely made up, just like my confidence.",
        "",
        "P.P.P.S. If you're not confused by now, you're not paying attention."
    ]
    
    for note in footnotes:
        print("  " + note)
    
    print("\033[0m")
    print_border()
    
    # Final existential crisis animation
    print("\n\033[91m")
    crisis = "QUICK! PANIC ABOUT THE MEANING OF LIFE..."
    typewriter_effect(crisis, 0.05)
    time.sleep(0.5)
    print("\033[92m...just kidding, it's probably fine.\033[0m")
    print("\033[90m(But seriously, what if it's not?)\033[0m")

if __name__ == "__main__":
    main()