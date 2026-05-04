"""
Campbell's Soup Can #3560
Produced: 2026-05-04 07:24:23
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

QUOTE = "I went to therapy because I was afraid of death. My therapist said, 'That's just fear.' I said, 'No, it's existential dread!' He charged me $200. I wonder if he's afraid of his own fees."

def print_colored(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def animate_dots(message, duration=2):
    sys.stdout.write(message)
    sys.stdout.flush()
    end_time = time.time() + duration
    while time.time() < end_time:
        for dot in range(3):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(0.3)
        sys.stdout.write('\b\b\b   \b\b\b')
        sys.stdout.flush()
        time.sleep(0.3)

print("\n")
animate_dots(print_colored(" Calculating Woody-esque wisdom", "1;35"))
time.sleep(0.5)

# Create colorful box
border_color = "1;34"
text_color = "1;32"
width = len(QUOTE) + 4

print("\n" + " " * 10 + print_colored("╔" + "═" * width + "╗", border_color))
print(" " * 10 + print_colored("║" + " " * width + "║", border_color))
print(" " * 10 + print_colored(f"║  {QUOTE}  ║", text_color))
print(" " * 10 + print_colored("║" + " " * width + "║", border_color))
print(" " * 10 + print_colored("╚" + "═" * width + "╝", border_color))

print("\n" + " " * 15 + print_colored(" — Woody Allen (probably)", "1;33") + "\n")