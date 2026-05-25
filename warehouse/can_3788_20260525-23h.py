"""
Campbell's Soup Can #3788
Produced: 2026-05-25 23:32:13
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# ANSI colorcodes for fun visual effect
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
MAGENTA= "\033[35m"
CYAN   = "\033[36m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

# The Woody Allen‑style philosophical quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Decorative box dimensions
box_width = len(quote) + 4
top_line    = f"{BOLD}{YELLOW}┌{'─'*box_width}┐{RESET}"
quote_line  = f"│ {BOLD}{MAGENTA}{quote}{RESET} │"
attr_line   = f"│ {BOLD}{GREEN}— Woody Allen{RESET} │"
bottom_line = f"{BOLD}{YELLOW}└{'─'*box_width}┘{RESET}"

# Optional little ASCII doodle to add whimsy
doodle = """
      .-""""-.
     / -   - )
    | — ( ) — |
     \\_`---'/_ 
"""

print(top_line)
print(quote_line)
print(attr_line)
print(bottom_line)
print(doodle)