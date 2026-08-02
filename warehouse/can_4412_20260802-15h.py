"""
Campbell's Soup Can #4412
Produced: 2026-08-02 15:27:19
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody Allen‑style philosophical quote with colorful ASCII art

# ANSI colour codes
YELLOW = "\033[33m"
CYAN   = "\033[36m"
RESET  = "\033[0m"

# Decorative box (uses Unicode box‑drawing characters)
box = r"""
   ┌───────────────────────────────────────────────┐
   │   “I’m not afraid of death;                    │
   │   I just don’t want to be there                │
   │   when it happens.”                             │
   └───────────────────────────────────────────────┘
"""

# The Woody Allen‑style quote
quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# Print the coloured box, then the quote in another colour
print(YELLOW + box.strip() + RESET)
print(CYAN + f'"{quote}"' + RESET)