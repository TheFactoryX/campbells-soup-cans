"""
Campbell's Soup Can #4963
Produced: 2026-09-14 23:07:59
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
RED = "\033[31m"

def slow_print(text, delay=0.05, color=RESET, end="\n"):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print(end, end="")

def create_border(text, color=BLUE):
    """Create a decorative border around text"""
    width = len(text) + 10
    border_top = "┌" + "─" * width + "┐"
    border_bottom = "└" + "─" * width + "┘"
    
    print(color + border_top + RESET)
    print(color + "│" + RESET, end="")
    print(text, end="")
    print(color + "│" + RESET)
    print(color + border_bottom + RESET)

def main():
    # Clear screen for dramatic effect
    print("\033[2J\033[H", end="")
    
    # Title with animation
    title = "WOODY ALLEN'S EXISTENTIAL CORNER"
    print("\n")
    for i, word in enumerate(title.split()):
        color = [YELLOW, BLUE, PURPLE, CYAN][i % 4]
        slow_print(word + " ", delay=0.1, color=color)
    
    print("\n")
    
    # Decorative separator
    separator = "◆" * 50
    slow_print(separator, delay=0.02, color=RED)
    
    # The quote with typewriter effect
    quote = ("I've been having a rather difficult time lately. "
             "Not with death, mind you, but with the terrifying realization "
             "that I've been living my entire life in a universe that doesn't care "
             "if I exist or not. And worse, I think my therapist might be having "
             "an affair with my analyst. It's enough to make you question "
             "whether any of it matters, or if we're all just cosmic jokes "
             "waiting to be told at a particularly bleak party.")
    
    print("\n")
    create_border(" QUOTE ", YELLOW)
    print()
    
    # Print quote with dramatic pauses
    sentences = quote.split(". ")
    for i, sentence in enumerate(sentences):
        if i < len(sentences) - 1:
            sentence += "."
        color = YELLOW if i % 2 == 0 else BLUE
        slow_print(sentence + " ", delay=0.03, color=color)
        if i < len(sentences) - 1:
            time.sleep(0.5)  # Pause between sentences
    
    print("\n\n")
    
    # Signature with existential footnote
    signature = "— A Neurotic Philosopher (probably me)"
    slow_print(signature, delay=0.08, color=ITALIC + PURPLE)
    
    print("\n")
    
    # Philosophical postscript
    postscript = [
        "P.S. I asked God why he made us so flawed.",
        "He said, 'To give you something to work on.'",
        "I said, 'That's not very comforting.'",
        "He shrugged. 'I'm not in the comfort business.'"
    ]
    
    for line in postscript:
        slow_print(line, delay=0.04, color=CYAN)
        time.sleep(0.3)
    
    # Final existential punchline
    print("\n")
    final_thought = "The universe is under no obligation to make sense to you."
    slow_print(final_thought, delay=0.06, color=BOLD + RED)
    
    # Exit with a philosophical shrug
    print("\n")
    shrug = "¯\\_(ツ)_/¯"
    slow_print(shrug, delay=0.15, color=YELLOW)
    print("\n" + RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + RED + "Even my existential crisis got interrupted..." + RESET)
        sys.exit(0)