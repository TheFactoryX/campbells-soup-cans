"""
Campbell's Soup Can #3950
Produced: 2026-06-17 11:16:41
Worker: Google: Gemma 4 31B (free) (google/gemma-4-31b-it:free)
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

def typewriter_effect(text, delay=0.05, color="\033[0m"):
    """Prints text with a typewriter animation and color."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")

def draw_frame():
    """Draws a neurotic, slightly crooked border."""
    width = 80
    print("\033[94m" + "╮" + "─" * (width - 2) + "╭")
    print("│" + " " * (width - 2) + "│")
    print("\033[0m")

def draw_bottom_frame():
    width = 80
    print("\033[94m" + "╰" + "─" * (width - 2) + "╯" + "\033[0m")

def main():
    # Woody Allen style original quote
    quote = (
        "I've spent my entire life preparing for a crisis that I'm now \n"
        "entirely too anxious to actually encounter, which is why I've \n"
        "decided to spend the rest of my days worrying about the \n"
        "fact that I'm worrying. It's a very efficient system."
    )
    
    # ANSI Colors
    BOLD = "\033[1m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    RESET = "\033[0m"

    # Neurotic loading sequence
    loading_messages = [
        "Checking existential dread levels...",
        "Analyzing irrational fears...",
        "Adjusting glasses...",
        "Questioning the meaning of this script...",
        "Panic attack in progress... 40%",
        "Sighing heavily...",
        "Ready to be moderately disappointed."
    ]

    print("\n")
    for msg in loading_messages:
        sys.stdout.write(f"\r{YELLOW}{msg}{RESET}")
        sys.stdout.flush()
        time.sleep(random.uniform(0.3, 0.8))
    
    print("\n\n")
    
    # The "Visual" Presentation
    draw_frame()
    
    # The attribution
    typewriter_effect("   💭 A Moment of Pure Neurosis:", 0.08, CYAN + BOLD)
    print("\n" + " " * 3 + "─" * 30)
    
    # The Quote
    typewriter_effect(f"   {quote}", 0.06, YELLOW)
    
    print("\n" + " " * 3 + "─" * 30)
    
    # The Signature
    time.sleep(0.5)
    typewriter_effect("   — Woody (probably)", 0.1, RED + BOLD)
    
    draw_bottom_frame()
    
    # Final touch: a lingering thought
    time.sleep(1)
    print(f"\n{CYAN} (Wait, did I leave the stove on?){RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[31mAborted! Just like my childhood dreams!\033[0m")