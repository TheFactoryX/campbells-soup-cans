"""
Campbell's Soup Can #2543
Produced: 2026-03-03 11:46:56
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_slow(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# ANSI color codes
RESET = "\033[0m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
BLUE = "\033[94m"
RED = "\033[91m"
GREEN = "\033[92m"
BOLD = "\033[1m"

# Neurotic Woody Allen quote
quote = "I'm not afraid of death; I'm afraid of the checkout line at the supermarket when it happens. Why must the universe be so inefficient? Now I have to wait for the next cosmic bus while contemplating my inevitable cosmic lateness."

# ASCII art of Woody Allen (neurotic face)
woody_art = [
    f"{YELLOW}        (o)_(o)      {RESET}",
    f"{YELLOW}          |  |        {RESET}",
    f"{YELLOW}          |  |        {RESET}",
    f"{YELLOW}        __|__        {RESET}",
    f"{YELLOW}       /     \\       {RESET}",
    f"{YELLOW}      /       \\      {RESET}",
    f"{YELLOW}     /         \\     {RESET}",
    f"{YELLOW}    /           \\    {RESET}",
    f"{YELLOW}   /             \\   {RESET}",
    f"{YELLOW}  /               \\  {RESET}",
    f"{YELLOW} /                 \\ {RESET}",
    f"{YELLOW}/                   \\{RESET}"
]

# Create a dynamic "existential crisis" background
def draw_background():
    for i in range(15):
        line = ""
        for j in range(80):
            if j % 5 == 0:
                line += f"{RED}*{RESET}"
            elif j % 7 == 0:
                line += f"{BLUE}•{RESET}"
            elif j % 3 == 0:
                line += f"{GREEN}+{RESET}"
            else:
                line += " "
        print(line, end='\r')
        time.sleep(0.05)
    print(" " * 80, end='\r')

# Print the title with animation
print(f"{BOLD}{YELLOW}")
print_slow("          EXISTENTIAL CRISES R US", 0.05)
print(f"{RESET}\n")

# Draw the neurotic background
draw_background()

# Print Woody's face
for line in woody_art:
    print(line)
    time.sleep(0.05)

# Print quote in a thought bubble
bubble_width = 50
print(f"{BOLD}{YELLOW}  {'_' * (bubble_width-2)}")
print(f" /{WHITE}{' ' * (bubble_width-2)}{YELLOW}\\")

# Format quote into bubble
words = quote.split()
lines = []
current_line = ""
for word in words:
    if len(current_line) + len(word) + 1 <= bubble_width - 4:
        current_line += word + " "
    else:
        lines.append(current_line.strip())
        current_line = word + " "
if current_line:
    lines.append(current_line.strip())

# Animate quote typing in the bubble
for line in lines:
    print(f"{YELLOW}| {WHITE}", end='')
    print_slow(line, 0.03)
    print(f"{' ' * (bubble_width - len(line) - 5)}{YELLOW}|")
    time.sleep(0.2)

print(f"{YELLOW} \\{'_' * (bubble_width-2)}/")
print(f"{RESET}")

# Add neurotic footer
print(f"{BOLD}{RED}This quote has an expiration date: 5 minutes after reading{RESET}")
print(f"{BLUE}If you're still thinking about it, you've already missed your bus to the afterlife{RESET}")
print(f"{GREEN}System 7.9 - Running since 1925 - Last reboot: the Big Bang{RESET}")