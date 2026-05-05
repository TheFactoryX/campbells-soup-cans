"""
Campbell's Soup Can #3578
Produced: 2026-05-05 23:12:13
Worker: Google: Gemma 4 26B A4B  (free) (google/gemma-4-26b-a4b-it:free)
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

# --- ANSI COLOR CONSTANTS ---
class Colors:
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def typewriter(text, delay=0.05, color=Colors.CYAN):
    """Simulates a neurotic, hesitating typing effect."""
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        # Random hesitation to mimic Allen's neurosis
        time.sleep(delay + random.uniform(0, 0.1))

def draw_frame(width, content, border_color=Colors.MAGENTA):
    """Draws a fancy border around the content."""
    top = border_color + "╔" + "═" * (width - 2) + "╗" + Colors.END
    bottom = border_color + "╚" + "═" * (width - 2) + "╝" + Colors.END
    
    print(top)
    # Center the content
    padding = (width - 2 - len(content)) // 2
    if padding < 0: padding = 0
    
    line = " " * padding + content
    # Fill remaining space to keep border straight
    line += " " * (width - 2 - len(line))
    
    print(border_color + "║" + Colors.END + line + border_color + "║" + Colors.END)
    print(bottom)

def clear_screen():
    """Clears the terminal."""
    print("\033[H\033[J", end="")

def main():
    clear_screen()
    
    # The "Neurotic" Intro Animation
    intro_text = ["Searching for meaning...", "Checking pulse...", "Panic levels: Moderate...", "Searching for meaning..."]
    for i in range(3):
        for text in intro_text:
            sys.stdout.write(f"\r{Colors.YELLOW}{text}{Colors.END}")
            sys.stdout.flush()
            time.sleep(0.4)
    
    clear_screen()
    
    # ASCII Art "Neurotic Brain"
    brain_art = [
        "       ______",
        "    .-'      '-.",
        "  .'            '.",
        " /                \\",
        "|    (?)    (!)    |",
        "|  (Panic) (Exist) |",
        " \\                /",
        "  '.            .'",
        "    '-.______.-'",
    ]
    
    print(Colors.BLUE + "\n" * 2)
    for line in brain_art:
        print(f"{Colors.BLUE}{line.center(50)}{Colors.END}")
    print(Colors.BLUE + "\n" * 2)
    time.sleep(1)
    
    clear_screen()

    # The Grand Quote
    quote = "I find that my greatest fear isn't the void of the infinite cosmos, " \
            "it's the possibility that I'll spend my entire life worrying about " \
            "the void, only to find out it's actually just a very small, " \
            "uncomfortable room with bad lighting."

    # Visual Presentation
    width = 60
    
    # Break quote into lines for the box
    words = quote.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 < width - 4:
            current_line += (word + " ")
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())

    # Print the box with an animated reveal
    print(Colors.MAGENTA + "╔" + "═" * (width - 2) + "╗" + Colors.END)
    for line in lines:
        sys.stdout.write(f"{Colors.MAGENTA}║{Colors.END} ")
        typewriter(line.ljust(width - 4), delay=0.03, color=Colors.YELLOW)
        print(f" {Colors.MAGENTA}║{Colors.END}")
    print(Colors.MAGENTA + "╚" + "═" * (width - 2) + "╝" + Colors.END)

    # Final neurosis
    print("\n")
    typewriter("...Now, where did I put my medication?", delay=0.08, color=Colors.RED)
    print("\n" * 2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Existential crisis aborted.{Colors.END}")