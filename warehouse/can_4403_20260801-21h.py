"""
Campbell's Soup Can #4403
Produced: 2026-08-01 21:09:04
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

width = 70
quote = "I'm not afraid of death; I just don't want to be."
quote_len = len(quote)

print("\033[32m+" + "-" * width + "+\033[0m")
print("\033[33m|" + " " * width + "\033[0m")
print("\033[33m|{}{}{}|".format(quote, " " * (width - quote_len), "\033[0m"))
print("\033[33m|" + " " * width + "\033[0m")
print("\033[32m+" + "-" * width + "\033[0m")