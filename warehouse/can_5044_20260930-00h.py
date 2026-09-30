"""
Campbell's Soup Can #5044
Produced: 2026-09-30 00:27:54
Worker: inclusionAI: Ling 3.0 Flash Sante (free) (inclusionai/ling-3.0-flash-sante:free)
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

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BG_BLACK = "\033[40m"

def slow_print(text, color=WHITE, delay=0.03):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(char, width, color):
    print(color + char * width + RESET)

def main():
    width = 70

    # Title
    print()
    draw_frame("=", width, BOLD + CYAN)
    slow_print(BOLD + MAGENTA + " " * 18 + "🧠 WOODY'S WISDOM 🧠" + RESET, CYAN, 0.01)
    draw_frame("=", width, BOLD + CYAN)
    print()

    # The existential crisis box
    print(BG_BLACK + BOLD + YELLOW + " " * 3 + "~ " * 33 + RESET)
    print()

    # Quote lines with delay
    quote_lines = [
        (BOLD + RED + '    "I once asked my therapist if my fear of', 0.03),
        (RED + '     commitment was irrational."', 0.03),
        (WHITE + '     She said, "You know what? I don\'t know."', 0.03),
        (YELLOW + '     I respect her honesty. It\'s the only thing', 0.03),
        (YELLOW + '     I respect about therapists."', 0.03),
        (GREEN + '', 0.02),
        (BOLD + CYAN + '    "I read an article the other day that said', 0.03),
        (CYAN + '     people who worry about their mortality', 0.03),
        (CYAN + '     live longer. So I should be dead by now."', 0.03),
        (MAGENTA + '', 0.02),
        (BOLD + WHITE + '    "The universe is cold, uncaring, and vast."', 0.03),
        (BLUE + '     My therapist agrees. She told me to accept', 0.03),
        (BLUE + '     it. I told her I have anxiety about', 0.03),
        (BLUE + '     accepting things without analyzing them."', 0.03),
        (WHITE + '', 0.02),
        (BOLD + GREEN + '    "I fear not death itself, but the awkward', 0.03),
        (GREEN + '     small talk in the waiting room."', 0.03),
        (RED + BOLD + '', 0.02),
        (YELLOW + '              - "Every Time I Almost Feel Okay"', 0.04),
    ]

    for line, delay in quote_lines:
        slow_print(line, delay=delay)

    print()
    print(BG_BLACK + BOLD + YELLOW + " " * 3 + "~ " * 33 + RESET)
    print()

    # Woody face ASCII art
    woody = BOLD + RED + """
         \\   ^__^
          \\  (oo)\\_______
             (__)\\       )\\/\\
                 ||----w |
                 ||     ||
    """ + RESET

    for line in woody.split('\n'):
        slow_print(line, delay=0.02, color=RED if '^__^' in line else (CYAN if '\\____' in line else WHITE))

    print()
    draw_frame("-", width, DIM + MAGENTA)
    slow_print(DIM + MAGENTA + " " * 8 + "I came, I saw, I complained extensively." + RESET, delay=0.04)
    draw_frame("-", width, DIM + MAGENTA)
    print()

    # Final existential punch
    slow_print(BOLD + CYAN + " " * 10 + "💭 Existential Crisis: Complete 💭" + RESET, delay=0.05)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RESET + "\nToo existential? Same.")