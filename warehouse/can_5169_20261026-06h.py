"""
Campbell's Soup Can #5169
Produced: 2026-10-26 06:15:16
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def color(text, c):
    return f"\033[{c}m{text}\033[0m"

quote = """
"I've decided to become an existentialist, but I keep getting distracted by my anxiety about whether I'm doing it correctly. The problem with philosophy is that it makes everything worse unless you can somehow convince yourself that suffering is optional. Which, knowing my track record, I probably won't manage."
"""

def print_blinking(text, duration=2, rate=0.1):
    for _ in range(3):
        for _ in range(int(duration / rate)):
            print('\033[F' + color(text, "60;5;100") + color('   ', "60;5;235"), end='', flush=True)
            time.sleep(rate / 2)
            print('\033[F' + color(' ' * (len(text)+4), "60;5;235"), end='', flush=True)
            time.sleep(rate / 2)

print(color("\n\n╔══════════════════════════════════════════════════════════════════════╗", "31"))
print(color("║  Life is full of misery, loneliness, and suffering—fortunately,      ║", "33"))
print(color("║  according to philosophy, it also comes with a free existential      ║", "35"))
print(color("║  comedown button. Unfortunately, I can never find the user manual.  ║", "33"))
print(color("╚══════════════════════════════════════════════════════════════════════╝\n\n", "31"))

time.sleep(1.5)
print(color("                     \\\N{FACE WITH TROPICAL PLANT}  - ", "32"), end='', flush=True)
print(color("the universe’s cosmic version of 'are you sure?'", "36"))

time.sleep(2)
print(color("\n                               ~*~*~*~\n", "34"), end='', flush=True)
print_blinking(color("...just kidding!", "31"), duration=2.5)

time.sleep(1)
print(color("I'm not afraid of death; I just don't want to be there when it happens.", "35"), flush=True)