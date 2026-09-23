"""
Campbell's Soup Can #5010
Produced: 2026-09-23 05:59:04
Worker: inclusionAI: Ling 3.0 Flash Sante (free) (inclusionai/ling-3.0-flash-sante:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import math

# ANSI escape codes
class C:
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
    BG_DARK = "\033[40m"

def colored(text, color):
    return f"{color}{text}{C.RESET}"

def typewriter(text, color=C.WHITE, delay=0.03):
    for char in text:
        sys.stdout.write(color + char + C.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_frame(lines, border_color=C.CYAN):
    width = max(len(line) for line in lines) + 4
    print()
    print(colored("╔" + "═" * (width - 2) + "╗", border_color))
    for line in lines:
        padding = width - len(line) - 4
        print(colored("║  ", border_color) + line + colored(" " * padding + "║", border_color))
    print(colored("╚" + "═" * (width - 2) + "╝", border_color))
    print()

# Title with ASCII art
def draw_head():
    head = [
        "       .---.''---.",
        "      /  _   _   \\",
        "     |  (_) (_)  |",
        "     |  _     _  |",
        "      \\ '.__.' /",
        "       '------'",
        "        |    |",
        "        |    |",
    ]
    for line in head:
        print(colored(line, C.YELLOW))

# Main animation
def main():
    # Clear-ish effect
    print("\n" * 2)

    # Draw Woody's head
    draw_head()
    time.sleep(0.3)

    # Title
    title = colored("  ~ WOODY ALLEN'S EXISTENTIAL CRISIS ~ ", C.BOLD + C.MAGENTA)
    print(f"\n{title:^50}\n")
    time.sleep(0.5)

    # The quote
    quote_lines = [
        colored('"I don\'t mind dying, I just don\'t', C.YELLOW),
        colored(' want to be there when it happens...', C.YELLOW),
        colored(' mainly because of the dress code."', C.YELLOW),
    ]
    print_frame(quote_lines, C.CYAN)

    time.sleep(0.5)

    # Signature with animation
    sig = colored("         -- Woody Allen", C.RED + C.BOLD)
    for i, char in enumerate(sig):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

    time.sleep(0.8)

    # Fun extras
    extras = [
        colored("🔍  Existential question: Does my neurosis", C.GREEN),
        colored("     count as therapy if I pay myself?", C.GREEN),
        colored("💭  I'm not superstitious, but I'm", C.BLUE),
        colored('     a little stitious.', C.BLUE),
        colored("🧟  I'm not afraid of death — I just", C.MAGENTA),
        colored("     don't want to be there when it happens.", C.MAGENTA),
    ]
    print_frame(extras, C.GREEN)

    # Final message
    time.sleep(0.5)
    end = colored("\n  Remember: If life gives you lemons...", C.CYAN + C.BOLD)
    print(f"\n{end:^50}")
    time.sleep(0.3)
    end2 = colored("  ...make grape juice and watch the world wonder.\n", C.CYAN + C.BOLD)
    print(f"{end2:^50}")

    # Little celebration
    print("\n" + colored("🎬  🎭  🎬  🎭  🎬", C.YELLOW + C.BOLD))
    print()

if __name__ == "__main__":
    main()