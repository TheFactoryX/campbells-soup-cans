"""
Campbell's Soup Can #349
Produced: 2025-11-18 02:15:30
Worker: ArliAI: QwQ 32B RpR v1 (free) (arliai/qwq-32b-arliai-rpr-v1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

\n")
# Create the pinball table
pinball_table = [
    "┌───────────────┐",
    "│ \x1b[31m\x1b[47m      \x1b[0m │",
    "├───────────────┤",
    "│ │       \x1b[37m\x1b[41m│         \x1b[0m",
    "├───────────────┤",
    "│ │   \x1b[31m\x1b[47m    │         \x1b[0m",
    "├───────────────┤",
    "│ \x1b[37m\x1b[41m        \x1b[0m │",
    "└───────────────┘",
]

# Print the pinball table
for line in pinball_table:
    print(line)

# Insert quote into quote dispenser
quote_layers = []
for char in chosen_quote[:36]:
    quote_layers.append(f"\x1b[34m\x1b[47m{char}\x1b[0m")
# Addücend's
quote_layers.append("\x1b[34m\x1b[47m!\x1b[0m")

# Print the quote dispenser
for layer in quote_layers:
    pinball_table[3] = f"│ │   {layer} │         \x1b[0m"
    for line in pinball_table:
        print(line)
        sleep(0.3)

# Add scoreboard
scoreboard = [
    "┌───────────────────────────┐",
    "│ Score: 9001               │",
    "└───────────────────────────┘",
]
for line in scoreboard:
    print(line)

print("