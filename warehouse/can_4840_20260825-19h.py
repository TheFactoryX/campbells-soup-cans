"""
Campbell's Soup Can #4840
Produced: 2026-08-25 19:45:42
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen style — neurotic, funny, existential."""

# The quote — classic Woody: mortality mixed with trivial neurorosis
quote = "I'm not afraid of death. I just don't want to be the one who has to explain to God why I spent my whole life worrying about whether the toaster was unplugged."

# ANSI escape sequences (reset, bold, colors)
RS = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
YELLOW = "\033[33m"
RED = "\033[31w"

# Layout width
W = 68

# Print a colorful ASCII-framed header
print(f"{MAGENTA}+{'-'*W}+{RS}")
# Quote line in bold cyan, framed
print(f"{MAGENTA}| {BOLD}{CYAN}{quote}{RS} {MAGENTA}|{RS}")
print(f"{MAGENTA}+{'-'*W}+{RS}")

# A tiny neurotic footer
print(f"{YELLOW}... and somewhere, a mother is waiting for a call, not a tech support ticket.{RS}")