"""
Campbell's Soup Can #920
Produced: 2025-12-14 05:34:38
Worker: Qwen: Qwen3 Coder 480B A35B (free) (qwen/qwen3-coder:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

def typewriter_effect(text, delay=0.03):
    """Simulate typewriter effect for text printing"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_fancy_box(content, color="\033[93m"):
    """Print content in a fancy ASCII box with color"""
    lines = content.split('\n')
    max_length = max(len(line) for line in lines)
    
    # Top border
    print(f"{color}╒{'═' * (max_length + 2)}╕\033[0m")
    
    # Content lines
    for line in lines:
        padding = max_length - len(line)
        print(f"{color}│ {line}{' ' * padding} │\033[0m")
    
    # Bottom border
    print(f"{color}╘{'═' * (max_length + 2)}╛\033[0m")

def print_brain_art():
    """Print a colorful ASCII brain with existential crisis"""
    brain_art = [
        "    \033[95m ___   ___ \033[0m",
        "   \033[95m/   \\ /   \\\033[0m",
        "  \033[95m|     |     |\033[0m",
        "  \033[95m \\___/ \\___/ \033[0m",
        "  \033[95m  |   |   |  \033[0m",
        "  \033[95m /   |   \\  \033[0m",
        " \033[95m/____|____\\ \033[0m",
        "\033[95m|_____|_____|\033[0m"
    ]
    
    for line in brain_art:
        print(line)
        time.sleep(0.1)

def print_worry_lines():
    """Print animated worry lines"""
    worries = [
        "\033[91m...\033[0m",
        "\033[91m..xiety.\033[0m",
        "\033[91m.existential an.xiety..\033[0m",
        "\033[91m..e.x.i.s.t.e.n.t.i.a.l..a.n.x.i.e.t.y...\033[0m"
    ]
    
    for worry in worries:
        print(worry)
        time.sleep(0.3)
        sys.stdout.write("\033[F\033[K")  # Move cursor up and clear line

def main():
    # Start with some anxiety
    print("\033[91mALERT: Existential crisis in progress...\033[0m")
    time.sleep(1)
    
    # Show brain with crisis
    print_brain_art()
    time.sleep(1)
    
    # Animate some worries
    print_worry_lines()
    
    # The philosophical gem
    quote = ("I finally realized that my fear of death isn't really about dying—\n"
             "it's about spending my entire life worrying about something that \n"
             "won't happen for another 47 years, 3 months, and 2 days, which… \n"
             "statistically speaking… I should be thrilled about. But I'm not.")
    
    # Print it in a fancy box with a title
    print("\n\033[93mWOODY ALLEN'S EXISTENTIAL WISDOM:\033[0m")
    print_fancy_box(quote)
    
    # Signature
    print("\n\033[90m- Another panic attack brought to you by the letters W, A, and Y\033[0m")
    
    # Neurotic afterthought
    time.sleep(1)
    print("\033[90m(P.S. I'm still not sure if I actually said this or if it's something I'm going to regret thinking I said)\033[0m")

if __name__ == "__main__":
    main()