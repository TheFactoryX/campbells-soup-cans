"""
Campbell's Soup Can #1124
Produced: 2025-12-23 11:31:00
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# Woody Allen philosophical quote in a colorful ASCII box
CYAN_BG = "\033[46m"   # cyan background
YELLOW = "\033[33m"    # yellow foreground
RESET = "\033[0m"      # reset ANSI codes

quote = "I am not afraid of death; I just don't want to be there when it happens."

# Box dimensions
WIDTH = 72  # interior width
TOP = "╔" + "═" * WIDTH + "╗"
BOTTOM = "╚" + "═" * WIDTH + "╝"

# Pad the quote to fit the box width
pad_len = WIDTH - len(quote)
left = pad_len // 2
right = pad_len - left
middle = " " * left + quote + " " * right
MID_LINE = "║" + middle + "║"

# Print the colored box
print(f"{CYAN_BG}{TOP}{RESET}")
print(f"{CYAN_BG}║{' ' * WIDTH}║{RESET}")
print(f"{YELLOW}{MID_LINE}{RESET}")
print(f"{CYAN_BG}{BOTTOM}{RESET}")

# Ensure terminal colors are reset
print(RESET, end="")