"""
Campbell's Soup Can #4539
Produced: 2026-08-11 18:08:14
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time, random

# ANSI escape codes
RESET = '\033[0m'
BOLD = '\033[1m'
CYAN = '\033[36m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
COLORS = [CYAN, YELLOW, MAGENTA]

def typewriter_line(line, delay=0.05):
    for ch in line:
        color = random.choice(COLORS)
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def print_box(lines, delay=0.05):
    width = max(len(line) for line in lines)
    border = '*' * (width + 4)
    sys.stdout.write(f"{YELLOW}{border}\n")
    for line in lines:
        sys.stdout.write("* ")
        typewriter_line(line, delay)
        sys.stdout.write(" *\n")
    sys.stdout.write(f"{border}{RESET}\n")

def main():
    header = f"{BOLD}{CYAN}Woody's Existential Musings:{RESET}"
    sys.stdout.write(header + "\n\n")
    quote = ("I think the universe is a cosmic joke, "
             "and I'm the punchline that keeps asking why.")
    print_box([quote], delay=0.07)

if __name__ == "__main__":
    main()
