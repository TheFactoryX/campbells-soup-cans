"""
Campbell's Soup Can #5099
Produced: 2026-10-13 00:40:55
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# Single Python file – run it directly!
# A Woody Allen‑style philosophical quote, dressed up with colorful ASCII art.

quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# Top and bottom frame (green)
frame_top    = "\033[32m╔" + "═" * 55 + "\033[0m╗"
frame_bottom = "\033[32m╚" + "═" * 55 + "\033[0m╝"

# The quote itself (magenta)
quote_line   = "\033[35m║  " + quote + "  ║\033[0m"

# Attribution (yellow)
attrib_line  = "\033[33m║ — Woody Allen\033[0m"

# Print the whole thing with a couple of newlines for spacing
print("\n" + frame_top)
print(quote_line)
print(attrib_line)
print(frame_bottom + "\n")