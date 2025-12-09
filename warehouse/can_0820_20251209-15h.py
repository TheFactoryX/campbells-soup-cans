"""
Campbell's Soup Can #820
Produced: 2025-12-09 15:36:44
Worker: AllenAI: Olmo 3 32B Think (free) (allenai/olmo-3-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""



import sys

quote = "Neurotic? My mind's a funhouse mirror."

# Thought bubble ASCII art in blue
print("\033[34m", end="")
print("     ______________")
print("    /               \\")
print(f"   <  {quote[:30]}...  >")
print("    \\_______________/")
print("\033[0m")

# Yellow box with green text
border = "+------------------------------------------------+"
formatted_quote = quote.center(48)
print("\033[33m", end="")
print(border)
print(f"\033[32m|{formatted_quote}|\033[0m")
print(border)
print("\033[0m")

# Sparkles at the bottom
print("\033[32m", end="")
print(" " * 10 + "* " * 5)
print("\033[0m")