"""
Campbell's Soup Can #4043
Produced: 2026-06-28 23:31:59
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

inner_width = 60
line1 = "I'm not afraid of death. I just don't want to be there"
line2 = "when it happens. And also, I don't want to be there when I'm alive"
line3 = "because life is too much work."
top_bottom = "+" + ("-" * inner_width) + "+"
print("\033[92m" + top_bottom + "\033[0m")
for line in [line1, line2, line3]:
    padded = line.ljust(inner_width)
    print("\033[92m|" + padded + "\033[93m|" + "\033[0m")
print("\033[92m" + top_bottom + "\033[0m")