"""
Campbell's Soup Can #1011
Produced: 2025-12-18 08:45:27
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes for colors
colors = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m'
}

# ASCII art of Woody Allen
woody_ascii = f"""
{colors['bold']}{colors['cyan']}           ,;,
          // \\\\
         |  {colors['magenta']}O{colors['cyan']} ||   (Steve Martin's hat)
         |  {colors['magenta']}O{colors['cyan']} ||
         |_@_@_|
          \____/
         /      \\
        |        |
        \________/

              .-.
             (o.o)
    /\__(     )__/\         {colors['magenta']}( Woody Allen {colors['reset']}")
     {colors['cyan']}||    `{colors['reset']}'    ||    {colors['magenta']}'{colors['reset']}'   {colors['magenta']}"Neurotic genius{colors['reset']}"{
colors['reset']}
     ||__(._____.)__
{colors['reset']}
"""

quote_parts = [
    f"{colors['red']}Life{colors['reset']} {colors['yellow']}is{colors['reset']} {colors['green']}obsessed{colors['reset']} {colors['blue']}with{colors['reset']} {colors['magenta']}meaning,",
    f"but{colors['red']} I{colors['reset']} {colors['yellow']}never{colors['reset']} {colors['blue']}found{colors['reset']} {colors['magenta']}the{colors['reset']}",
    f"{colors['green']}meaning{colors['reset']} {colors['yellow']}of{colors['reset']} {colors['blue']}I{colors['reset']} {colors['magenta']}mean{colors['reset']},",
    f"{colors['green']}fitness{colors['reset']} {colors['yellow']}program{colors['reset']} {colors['blue']}that{colors['reset']} {colors['magenta']}burns{colors['reset']}",
    f"{colors['blue']}later{colors['reset']} {colors['yellow']}cheese{colors['reset']} {colors['blue']}burgers,{colors['reset']}",
    f"{colors['magenta']} and{colors['reset']} {colors['red']}so{colors['reset']} {colors['yellow']}does{colors['reset']} {colors['blue']}I,{colors['reset']}",
    f"{colors['cyan']}which{colors['reset']} {colors['green']}is{colors['reset']} {colors['blue']}supposed{colors['reset']} {colors['magenta']}to{colors['reset']}",
    f"{colors['magenta']}be{colors['reset']} {colors['yellow']}my{colors['reset']} {colors['blue']}cheeseburger{colors['reset']} {colors['magenta']}burger.tube{colors['reset']}"
]

# Clear screen (works in most terminals)
sys.stdout.write("\033[H\033[J")

print(woody_ascii)

# Animation function to display quote character by character
def animate_quote(quote):
    for char in quote:
        # Make wisdom words (are, the, is, etc.) flash
        if char.lower() in ['a', 'i', 'o', 'u', 'e', 's', 't', 'h', 'b', 'r']:
            sys.stdout.write(colors['blink'] + char + colors['reset'])
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# Main loop to display quote in sequence
print(f"{colors['bold']}{colors['green']}Philosophical Meltdown:{colors['reset']}")

# Break the quote into multiple segments and display them sequentially
for part in quote_parts:
    animate_quote(part)

# Final closing line
print(f"\n{colors['bold']}{colors['yellow']}Existence: It's What You Do... Not What You Emerge From...{colors['reset']}")