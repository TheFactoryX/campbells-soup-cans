"""
Campbell's Soup Can #4646
Produced: 2026-08-17 08:03:10
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def c(text, code): return f"\033[{code}m{text}\033[0m"

quote = [
    "I’m a neurotic, existential clown who spends his whole life wondering",
    "why the chicken crossed the road — for a purpose or just for fun?",
    "Life’s a joke, and the punchline is that we’re all just waiting for the",
    "lights to go out."
]

border = c("╔" + "═"*58 + "═╗", 97)
bottom = c("╚" + "═"*58 + "╝", 97)

print(border)
for i, line in enumerate(quote):
    print(c(f"║  {line.center(58)}  ║", [93, 92, 96, 91][i]))
print(bottom)

time.sleep(0.6)