"""
Campbell's Soup Can #4804
Produced: 2026-08-24 05:53:32
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A delightfully neurotic philosophical moment, Woody Allen style.
"""

import time
import sys
import random

# ANSI color codes because life needs more color (and so do our anxieties)
class Colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ORANGE = '\033[91m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def typewriter(text, delay=0.03):
    """Prints text with a dramatic, existential pause between each character."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_with_color(text, color=Colors.CYAN, delay=0.02):
    """Colorful neurosis in motion."""
    colored_text = f"{color}{text}{Colors.RESET}"
    typewriter(colored_text, delay)

def animated_box(text_lines, border_color=Colors.PURPLE, inner_color=Colors.YELLOW):
    """Creates a box around text - like being trapped, but with pretty colors."""
    # Find the longest line for proper box sizing
    max_len = max(len(line) for line in text_lines)
    
    # Top border - approaching like dread
    top_border = f"{border_color}╔{'═' * (max_len + 2)}╗{Colors.RESET}"
    bottom_border = f"{border_color}╚{'═' * (max_len + 2)}╝{Colors.RESET}"
    empty_line = f"{border_color}║{Colors.RESET}{inner_color}{' ' * (max_len + 2)}{border_color}║{Colors.RESET}"
    
    # Print the box with dramatic pauses
    time.sleep(0.3)
    typewriter(top_border, 0.05)
    
    for i, line in enumerate(text_lines):
        padding = max_len - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        line_text = f"{border_color}║{Colors.RESET} {inner_color}{' ' * left_pad}{line}{' ' * right_pad} {border_color}║{Colors.RESET}"
        typewriter(line_text, 0.04)
    
    typewriter(bottom_border, 0.05)

def print_quote():
    """The main event: a beautifully anxious existential crisis."""
    
    # Dramatic title
    title = f"{Colors.BOLD}{Colors.RED}─── A Moment of Profound {Colors.YELLOW}Neurosis {Colors.RED}───{Colors.RESET}"
    print(title)
    print()
    
    # Build the quote with layered anxieties
    quote_lines = [
        "I went to a philosopher once...",
        "He said, 'What's the meaning of life?'",
        "I said, 'I don't know, that sounds like a lot of work.'",
        "Then I worried I was being lazy about existential dread.",
        "So I became anxious about my anxiety.",
        "Which made me anxious about being anxious...",
        "",
        "And suddenly I realized:",
        "",
        "Life is like a sandwich...",
        "You're the bread,",
        "existence is the filling,",
        "and Death is that sad mayo",
        "that expires two weeks ago",
        "but you eat anyway because",
        "you're already halfway through",
        "and what else is there to do?",
        "",
        "- Some guy sitting on a couch, probably"
    ]
    
    # Print each line with varying colors and delays for maximum neurotic effect
    colors = [Colors.CYAN, Colors.GREEN, Colors.YELLOW, Colors.ORANGE, Colors.BLUE, Colors.PURPLE]
    
    for i, line in enumerate(quote_lines):
        if line == "":
            print()
        elif line.startswith("-"):
            # Author attribution in a special color
            typewriter(f"{Colors.ITALIC if hasattr(Colors, 'ITALIC') else ''}{Colors.ORANGE}{line}{Colors.RESET}", 0.05)
            time.sleep(0.5)
        else:
            color = colors[i % len(colors)]
            typewriter(f"{color}{line}{Colors.RESET}", 0.03)
            time.sleep(0.2)  # Existential pause
    
    print()
    
    # Final box of wisdom/despair
    final_thoughts = [
        "In conclusion:",
        "We're all just mayonnaise",
        "waiting to expire.",
        "But hey,",
        "at least we're expired together!",
        "(That's what friends are for.)"
    ]
    
    animated_box(final_thoughts)

def main():
    """Main existential loop."""
    # Clear screen for maximum dramatic effect
    print("\033[2J\033[H", end="")
    
    print_quote()
    
    # Subtle blinking cursor of uncertainty
    time.sleep(1)
    print(f"\n{Colors.BOLD}{Colors.RED}Is that... is that funny?{Colors.RESET}", end="")
    for _ in range(3):
        time.sleep(0.8)
        print(".", end="", flush=True)
    print()

if __name__ == "__main__":
    main()