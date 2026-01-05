"""
Campbell's Soup Can #1400
Produced: 2026-01-05 05:50:27
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
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

# ANSI color codes
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BG_BLACK = "\033[40m"
    BG_GRAY = "\033[100m"

def slow_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.8, 1.2))
    print()

def draw_box(text, width=60, height=5):
    top_bottom = Colors.BOLD + Colors.CYAN + "╔" + "═" * (width + 2) + "╗" + Colors.RESET
    middle = lambda line: Colors.BOLD + Colors.CYAN + "║" + Colors.RESET + " " + line.center(width) + " " + Colors.BOLD + Colors.CYAN + "║" + Colors.RESET
    empty = lambda: Colors.BOLD + Colors.CYAN + "║" + " " * (width + 2) + "║" + Colors.RESET

    print(top_bottom)
    for _ in range(height // 2):
        print(empty())
    print(middle(text))
    for _ in range(height // 2):
        print(empty())
    print(top_bottom)

def brain_ascii():
    brain = r"""
      .--.
     |o_o |
     |:_/ |
    //   \ \
   (|     | )
  /'\_   _/`\
  \___)=(___/
    """
    return brain

def thought_bubble(text):
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    width = max_len + 4
    bubble = "  " + "_" * (width) + "  \n"
    for line in lines:
        bubble += " /" + line.center(width) + " \\\n"
    bubble += " \\_" + "_" * (width-2) + "_/"
    return bubble

def main():
    # Clear screen
    print("\033[2J\033[H", end="")

    # Title animation
    title = "🧠 A Woody Allen Moment 🧠"
    for i in range(len(title)):
        print("\033[2J\033[H", end="")
        print(Colors.BOLD + Colors.YELLOW + title[:i+1] + Colors.RESET)
        time.sleep(0.15)
    time.sleep(1)

    # Print brain ASCII
    print(Colors.BOLD + Colors.MAGENTA + brain_ascii() + Colors.RESET)

    # Thought bubble with quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens. Honestly, I'd rather be at the dentist."
    bubble = thought_bubble(quote)
    print("\n" + Colors.BOLD + Colors.WHITE + bubble + Colors.RESET)

    # Add some neurotic commentary
    slow_print("...and yet, here I am, writing this in Python instead of doing something useful like meditation.", 0.05)
    slow_print("Typical.", 0.07)

    # Final box
    final_quote = "Philosophy: It's like therapy, but with fewer insights and more existential dread."
    draw_box(final_quote, 60, 3)

    # Exit with a flourish
    time.sleep(1)
    print("\n" + Colors.BOLD + Colors.RED + "Goodbye, universe. I'll be in therapy, probably." + Colors.RESET)

if __name__ == "__main__":
    main()