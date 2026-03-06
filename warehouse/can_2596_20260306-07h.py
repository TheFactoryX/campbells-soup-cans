"""
Campbell's Soup Can #2596
Produced: 2026-03-06 07:52:16
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Woody Allen‑style quote
quote = [
    "I'm not afraid of death; I just don't want to be there when it happens,",
    "especially when I'm still waiting for the elevator."
]

# Layout dimensions
WIDTH = 60
INNER = WIDTH - 2          # space inside the border
BORDER_TOP = CYAN + "+" + "-" * INNER + RESET + "\n"

# Build each line of the quote, padded to fit the inner width
output_lines = []
for line in quote:
    padding = " " * (INNER - len(line))
    output_lines.append(f"{YELLOW}│ {line}{padding}{RESET} │\n")

# Print the full box
print(BORDER_TOP, end="")
print("".join(output_lines), end="")
print(BORDER_TOP, end="")