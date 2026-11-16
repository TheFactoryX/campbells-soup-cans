"""
Campbell's Soup Can #5250
Produced: 2026-11-16 22:02:48
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

# Enable ANSI colors on older Windows terminals
if os.name == "nt":
    os.system("")

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[31m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

QUOTE = (
    "I don't believe in an afterlife, but I'm packing a sweater just in case "
    "it's chilly and my mother is there to tell me I'm wearing it wrong."
)

def wrap(text, width):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        if len(cur) + len(word) + (1 if cur else 0) <= width:
            cur = (cur + " " + word).strip()
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines

def type_it(s, delay=0.04):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    W = 58
    IN = W - 4  # content width between borders

    type_it(f"{DIM}Initializing Woody Allen persona...{RESET}", 0.05)
    time.sleep(0.4)
    print()

    # Top border
    print(f"{CYAN}{BOLD}╭{'─' * (W - 2)}╮{RESET}")

    # Title line
    title_text = "WOODY ALLEN'S EXISTENTIAL CORNER"
    title_colored = f"{MAGENTA}{BOLD}{title_text}{RESET}"
    print(
        f"{CYAN}{BOLD}│{RESET} {title_colored}"
        f"{' ' * (IN - len(title_text))} "
        f"{CYAN}{BOLD}│{RESET}"
    )

    # Divider
    print(f"{CYAN}{BOLD}├{'─' * (W - 2)}┤{RESET}")

    # Quote lines
    for line in wrap(QUOTE, IN):
        print(
            f"{CYAN}{BOLD}│{RESET} {YELLOW}{line}{RESET}"
            f"{' ' * (IN - len(line))} {CYAN}{BOLD}│{RESET}"
        )

    # Divider
    print(f"{CYAN}{BOLD}├{'─' * (W - 2)}┤{RESET}")

    # Neurotic face
    face_text = "  (>.<)  "
    face_colored = f"{RED}{face_text}{RESET}"
    print(
        f"{CYAN}{BOLD}│{RESET} {face_colored}"
        f"{' ' * (IN - len(face_text))} {CYAN}{BOLD}│{RESET}"
    )

    # Bottom border
    print(f"{CYAN}{BOLD}╰{'─' * (W - 2)}╯{RESET}")
    print()

    # Footer
    type_it(f"{DIM}(I'm not a philosopher. I'm just a guy with a lot of unresolved childhood issues.){RESET}", 0.03)

if __name__ == "__main__":
    main()