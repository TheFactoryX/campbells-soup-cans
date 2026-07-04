"""
Campbell's Soup Can #4086
Produced: 2026-07-04 07:14:32
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

 cyan = "\033[36m"
 yellow = "\033[33m"
 reset = "\033[0m"

 quote = "Not afraid of death. I just want to not be there."
 width = 48
 quote_len = len(quote)
 left_pad = (width - quote_len) // 2
 right_pad = width - quote_len - left_pad
 centered_quote = " " * left_pad + quote + " " * right_pad

 print(cyan + "+" + "-" * width + "+" + reset)
 print(cyan + "|" + yellow + centered_quote + reset + "|" + reset)
 print(cyan + "+" + "-" * width + "+" + reset)