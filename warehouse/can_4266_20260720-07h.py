"""
Campbell's Soup Can #4266
Produced: 2026-07-20 07:29:40
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# Define ANSI color codes
red = '\033[31m'
white = '\033[37m'
blue = '\033[34m'
magenta = '\033[35m'
reset = '\033[0m'

# Woody Allen-style quote split into lines
line1 = "I'm not afraid of death; I just don't want to be there when it happens."
line2 = "But I do worry about the afterlife—if there isn't one, at least I'll die with dignity."
line3 = "If there is, well, that's a whole other existential crisis."

# Calculate box dimensions
max_length = max(len(line1), len(line2), len(line3))
border_length = max_length + 2  # Add 2 for the | characters

# Create top and bottom borders with red color
top_border = red + '*' * border_length + reset
bottom_border = top_border

# Print with animation delay
print(top_border)
time.sleep(0.3)
print(f"|{magenta}{line1.ljust(max_length)}{reset}|")
time.sleep(0.3)
print(f"|{white}{line2.ljust(max_length)}{reset}|")
time.sleep(0.3)
print(f"|{blue}{line3.ljust(max_length)}{reset}|")
time.sleep(0.3)
print(bottom_border)

# Add some extra flair at the bottom
time.sleep(0.5)
print(f"{magenta}  /\\_/\\  {reset}")
print(f"{magenta}( o.o ) {reset}")
print(f"{magenta} > ^ <   {reset}")