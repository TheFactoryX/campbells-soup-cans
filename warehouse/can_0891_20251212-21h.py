"""
Campbell's Soup Can #891
Produced: 2025-12-12 21:11:56
Worker: Perplexity: Sonar Pro (perplexity/sonar-pro)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
RESET = "\x1b[0m"BOLD = "\x1b[1m"RED = "\x1b[91m"YELLOW = "\x1b[93m"BLUE = "\x1b[94m"CYAN = "\x1b[96m"MAGENTA = "\x1b[95m"GREEN = "\x1b[92m"WHITE = "\x1b[97m"

def clear_screen():
    sys.stdout.write("\x1b[2J\x1b[H")    sys.stdout.flush()

def print_slow(text, color=RESET, delay=0.03):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)

def animate_cursor():
    for _ in range(3):
        sys.stdout.write("\x1b[?25l")  # Hide cursor
        time.sleep(0.1)
        sys.stdout.write("\x1b[?25h")  # Show cursor
        time.sleep(0.1)
    sys.stdout.write("\x1b[?25h")

# Clear screen and start
clear_screen()

# Title with animation
print_slow("🌹  WOODY ALLEN'S NEUROTIC WISDOM  🌹", YELLOW, 0.05)

print("\n" + MAGENTA + "╔" + "═" * 60 + "╗" + RESET)
print(MAGENTA + "║" + " " * 60 + "║" + RESET)

# The quote - Woody Allen style: neurotic, existential, self-deprecating
quote = """I'm not worried about the universe expanding... I'm worried it's expanding
faster than my therapist's availability, and when it all collapses, who will listen
to my complaints about existential dread and bad pastrami?"""

# Print quote with color and typewriter effect
print_slow(quote, BOLD + CYAN, 0.04)

print(MAGENTA + "║" + " " * 60 + "║" + RESET)
print(MAGENTA + "╚" + "═" * 60 + "╝" + RESET)

# Funny existential ASCII art
print("\n" + GREEN + r"""
          .-"""-.
         /       \
        |  O   O  |    "Life is full of misery...
         \   ^   /         ...and my existential crisis
          |||||           has a waiting list!"
          '-----'
""" + RESET)

# Pulsing signature
for _ in range(3):
    sig = f"{RED}-- Woody Allen's Anxious Soul --{RESET}"
    print("\r" + " " * 40 + "\r" + sig)
    sys.stdout.flush()
    time.sleep(0.5)
    sig2 = f"{BLUE}-- Woody Allen's Anxious Soul --{RESET}"
    print("\r" + " " * 40 + "\r" + sig2)
    sys.stdout.flush()
    time.sleep(0.5)

print("\n" + WHITE + "Press Enter to contemplate the void..." + RESET)
input()
clear_screen()
print(YELLOW + BOLD + "Thanks for laughing at the abyss!" + RESET)