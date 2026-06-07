"""
Campbell's Soup Can #3882
Produced: 2026-06-07 14:20:20
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import itertools

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
FG_CYAN = "\033[36m"
FG_MAGENTA = "\033[35m"
FG_YELLOW = "\033[33m"
BG_BLACK = "\033[40m"

# The Woody‑Allen‑style quote
quote = (
    "I think the universe is like a bad therapist: "
    "it listens to all my problems, but never offers a cure—"
    "just a slightly sarcastic nod and a bill."
)

# Build a simple box around the text
def make_box(text, pad=2):
    lines = text.split("\n")
    width = max(len(line) for line in lines) + pad * 2
    top = f"{FG_CYAN}" + "┌" + "─" * width + "┐" + RESET
    bottom = f"{FG_CYAN}" + "└" + "─" * width + "┘" + RESET
    boxed = [top]
    for line in lines:
        padded = " " * pad + line.ljust(width - pad * 2) + " " * pad
        boxed.append(f"{FG_CYAN}│{RESET}{FG_YELLOW}{padded}{RESET}{FG_CYAN}│{RESET}")
    boxed.append(bottom)
    return "\n".join(boxed)

# Typewriter animation for the quote
def typewriter(text, speed=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # slightly randomize speed for a more "human" feel
        time.sleep(speed + (0.02 * (ord(char) % 5)))
    sys.stdout.write("\n")

def main():
    # Clear screen (works on most terminals)
    sys.stdout.write("\033[2J\033[H")
    # Print the boxed, colored header
    header = f"{BOLD}{FG_MAGENTA}╔═╗  Woody Allen Meets Existential Angst  ╔═╗{RESET}"
    print(header)
    print()
    # Animate the quote inside the box
    boxed = make_box("")
    # Print the top of the box first
    lines = boxed.split("\n")
    sys.stdout.write(lines[0] + "\n")          # top border
    sys.stdout.flush()
    # Type the quote line‑by‑line inside the box
    inner_width = len(lines[1]) - 4            # subtract border chars and colors
    for part in quote.split(" "):
        # Build up a line until we reach the inner width
        # (simple greedy line wrap)
        if not hasattr(main, "current_line"):
            main.current_line = ""
        if len(main.current_line) + len(part) + 1 > inner_width:
            # print the built line
            sys.stdout.write(f"{FG_CYAN}│{RESET}{FG_YELLOW}  {main.current_line.ljust(inner_width)}  {RESET}{FG_CYAN}│{RESET}\n")
            sys.stdout.flush()
            main.current_line = part
        else:
            main.current_line += (" " if main.current_line else "") + part
        time.sleep(0.03)  # slight pause between words
    # print the final line
    sys.stdout.write(f"{FG_CYAN}│{RESET}{FG_YELLOW}  {main.current_line.ljust(inner_width)}  {RESET}{FG_CYAN}│{RESET}\n")
    # Print bottom border
    sys.stdout.write(lines[-1] + "\n")
    sys.stdout.flush()
    # Pause before exiting
    time.sleep(1.5)

if __name__ == "__main__":
    main()