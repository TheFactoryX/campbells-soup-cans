"""
Campbell's Soup Can #1359
Produced: 2026-01-03 06:47:18
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# The quote: darkly humorous, existential, and slightly absurd
quote = "I fear neither death nor failure—what terrifies me is being declared obsolete before sunset.\n(Especially the toast that’ll surely inherit my emotional baggage.)"

# Function to print the colorful ASCII art box
def create_border(width=60, top_color="31", side_color="32", text_color="36"):
    # White background with black text for quotes
    print(f"\033[40m\033[{top_color}m╔{"═" * width}╗\033[0m")
    for _ in range(4):
        inner = "    "
        print(f"\033[{side_color}m║{inner.ljust(width)}\033[0m")
    print(f"\033[{top_color}m╚{"═" * width}╩\033[0m")

# Main animation loop: simulate typing effect
def typewriter_effect(text, delay=0.05):
    for line in text.strip().split('\n'):
        for char in line:
            sys.stdout.write(char + ("" if char in "!?\n" else "."))
            time.sleep(delay)
        sys.stdout.write("\n")

# Draw the bordered text
create_border()

# Print the quote with animation
print("\n\033[1;35m")  # Bright magenta text
typewriter_effect(quote)

# Final touches
print("\n\033[m\u2502 \033[32m—And breathe, then panic.\033[m")