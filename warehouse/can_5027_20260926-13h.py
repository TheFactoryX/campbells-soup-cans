"""
Campbell's Soup Can #5027
Produced: 2026-09-26 13:06:15
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

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
GREEN = "\033[92m"

# Woody Allen style quote
quote = "I'm not afraid of death, I'm just afraid of being alone when it happens. And since I'm always alone, I'm always afraid."

def type_writer(text, delay=0.03, color=YELLOW):
    """Type out text character by character with a typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_border(char='═', length=80, color=BLUE):
    """Print a decorative border"""
    print(color + char * length + RESET)

def center_text(text, width=80, color=WHITE):
    """Center text with padding"""
    padding = (width - len(text)) // 2
    return color + " " * padding + text + " " * (width - len(text) - padding) + RESET

def animate_ellipsis(seconds=2):
    """Animate ellipsis dots"""
    for _ in range(seconds * 2):
        for dots in [".", "..", "...", ""]:
            sys.stdout.write(f"\r{YELLOW}{BOLD}Thinking{dots}{RESET}")
            sys.stdout.flush()
            time.sleep(0.25)
    print()

def main():
    # Clear screen (works on most systems)
    print("\033[2J\033[H", end="")
    
    # Intro animation
    print_border('╔', 80, MAGENTA)
    print_border('║', 80, MAGENTA)
    
    # Centered title
    title = " WOODY ALLENphilosophy "
    print(center_text(title, 80, BOLD + CYAN))
    
    print_border('║', 80, MAGENTA)
    print_border('╚', 80, MAGENTA)
    
    time.sleep(0.5)
    
    # Animated thinking process
    print("\n" + center_text("Hmm, let me think about this...", 80, ITALIC + GREEN))
    animate_ellipsis(2)
    
    # Main quote with typewriter effect
    print("\n")
    print_border('┌', 80, BLUE)
    print_border('│', 80, BLUE)
    
    # Split quote into lines for better formatting
    words = quote.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line + " " + word) <= 70:
            current_line += " " + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    
    # Print each line centered
    for line in lines:
        centered = center_text(line, 80, YELLOW + BOLD)
        print(border('│', 80, BLUE) + " " + centered + " " + border('│', 80, BLUE))
    
    print_border('└', 80, BLUE)
    
    # Outro with existential dread
    print("\n" + center_text("...and that's why I need therapy.", 80, ITALIC + RED))
    time.sleep(1)
    
    # Final existential crisis
    print("\n" + center_text("What's the point anyway? Oh wait, I already forgot.", 80, ITALIC + MAGENTA))
    
    # Woody Allen style disclaimer
    disclaimer = "Disclaimer: This quote may or may not reflect the existential dread of everyone, everywhere, always."
    print("\n" + center_text(disclaimer, 80, ITALIC + GREEN))
    
    # Final border
    print("\n" + border('═', 80, BLUE))

def border(char, length, color):
    """Helper function to create borders"""
    return color + char * length + RESET

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + center_text("Even my existential crisis was interrupted...", 80, RED))
        sys.exit(0)