"""
Campbell's Soup Can #4703
Produced: 2026-08-19 18:53:08
Worker: Google: Gemma 4 26B A4B  (free) (google/gemma-4-26b-a4b-it:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def animate_text(text, delay=0.05, color_code="\033[96m"):
    """Animates text character by character with a pulsing color effect."""
    colors = ["\033[96m", "\033[94m", "\033[95m", "\033[91m"]
    for i in range(len(text)):
        color = random.choice(colors)
        sys.stdout.write(color + text[i])
        sys.stdout.flush()
        time.sleep(delay)
    print("\033[0m")

def draw_frame(content, border_color="\033[93m"):
    """Wraps text in a decorative ASCII box."""
    width = 70
    line = border_color + "┌" + "─" * (width - 2) + "┐\033[0m"
    bottom = border_color + "└" + "─" * (width - 2) + "┘\033[0m"
    
    print(line)
    # Center content
    lines = content.split('\n')
    for line in lines:
        padding = (width - len(line) - 2) // 2
        if padding > 0:
            print(f"{border_color}│\033[0m{' ' padding}{line}{' ' (width - len(line) - padding - 2)}{border_color}│\033[0m")
        else:
            print(f"{border_color}│\033[0m{line.ljust(width-2)}{border_color}│\033[0m")
    print(bottom)

def main():
    # ANSI escape codes
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    YELLOW = "\033[93m"
    RED = "\033[91m"

    # The Woody Allen style quote
    quote = (
        "\"My therapist says I have a fear of commitment, "
        "which is ironic because I'm deeply committed "
        "to avoiding every single responsibility in my life.\""
    )

    # 1. Intro Animation (The Neurotic Existential Dread Loading)
    print("\n\n" * 2)
    print(f"{BOLD}{CYAN}Initializing Existential Crisis...{RESET}")
    time.sleep(0.5)
    
    loading_bar = ["", "⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for _ in range(3):
        for char in loading_bar:
            sys.stdout.write(f"\r{BOLD}{MAGENTA}{char} Searching for meaning in a chaotic universe...{RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
    
    print("\n\n")

    # 2. The Reveal
    # We use a dramatic delay to build tension
    time.sleep(1)
    
    # Decorative header
    print(f"{YELLOW}✨ --- AN EXISTENTIAL REALIZATION --- ✨\n")
    
    # Animate the quote itself
    animate_text(quote, delay=0.04, color_code=BOLD + CYAN)
    
    print(f"\n{YELLOW}✨ ----------------------------------- ✨\n")

    # 3. Final "Self-Deprecating" Footer
    footer_lines = [
        "---",
        "Don't worry, it's probably just your anxiety.",
        "Or the universe. Mostly the universe."
    ]
    
    for line in footer_lines:
        sys.stdout.write(f"{RED}")
        time.sleep(0.5)
        print(line)

    print("\n" * 2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[91m\n[Panic induced by sudden exit. Exiting safely.]\033[0m")
        sys.exit()