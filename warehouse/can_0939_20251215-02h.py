"""
Campbell's Soup Can #939
Produced: 2025-12-15 02:28:04
Worker: Amazon: Nova 2 Lite (free) (amazon/nova-2-lite-v1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def woody_box(text):
    width = len(text) + 4
    top = f"╔{'═' * width}╗"
    middle = f"║  {text.center(width)}  ║"
    bottom = f"╚{'═' * width}╝"
    return f"\n{color}{top}\n{middle}\n{bottom}{reset}"

color = "\033[38;5;201m\033[48;5;53m"  # Bright pink text on light purple background
reset = "\033[0m"

quote = "I’m not afraid of eternal damnation—my therapist already charges me hourly."

# ASCII art glasses
glasses = """
     ⬛️⚧️⬛️
    ⬛️◢◢◢◢◢◣◣◢◢◣◢◣
     ⬛️⚧️⬛️
"""

signature = f"\n{reset}- Presumably, {color}Woody Allen{reset} (but probably not)"

print(color + glasses + reset)
print(woody_box(quote))
print(signature)

# Animated dots after signature
for _ in range(3):
    print(color + "." + reset, end='', flush=True)
    time.sleep(0.3)