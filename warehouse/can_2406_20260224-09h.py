"""
Campbell's Soup Can #2406
Produced: 2026-02-24 09:07:24
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# ANSI color codes
RESET = "\033[0m"
RED   = "\033[31m"
GREEN = "\033[32m"
YELLOW= "\033[33m"
BLUE  = "\033[34m"
MAGENTA = "\033[35m"
CYAN  = "\033[36m"
BOLD  = "\033[1m"

# Philosophical quote in Woody Allen's neurotic style
quote = """\
If there is no God, then I'm responsible for my own jokes,
and that's terrifying.
"""

# Window size for the little ASCII-frame
WIDTH = 60
BORDER = f"{BLUE}+{'-'*(WIDTH-2)}{RESET}+"

def pad(line, extra=34):
    """Add left/right spaces so the line fits inside the frame."""
    return " " * (WIDTH-2-extra) + line + " " * (WIDTH-2-extra)

def colored(text, color):
    return f"{color}{text}{RESET}"

def fade_print(lines, color):
    """Print each line of `lines` with a tiny delay for a flicker effect."""
    for line in lines:
        print(colored(line, color))
        time.sleep(0.55)

def main():
    # Top border with a fun heading
    heading = colored(" ***  WOODY'S GUILT TRIP  *** ", YELLOW)
    print("\n", BORDER)
    for i in range(WIDTH-2):
        sys.stdout.write(colored("| " + " " * (WIDTH-4), CYAN), end="")
    print(colored(" |", CYAN))
    print(colored(f"| {heading} |", CYAN))
    for i in range(WIDTH-2):
        sys.stdout.write(colored("| " + " " * (WIDTH-4), CYAN), end="")
    print(colored(" |", CYAN))

    # Print each line of the quote, each in its own color to keep it lively
    lines = quote.splitlines()
    colors = [MAGENTA, GREEN]  # alternating colors
    for idx, line in enumerate(lines):
        line_colored = colored(line, colors[idx % len(colors)])
        framed = f"| {line_colored} |"
        print(colored(framed, MAGENTA))
        time.sleep(0.45)

    # Bottom border to close the frame
    print(BORDER)
    print("\n")

if __name__ == "__main__":
    main()