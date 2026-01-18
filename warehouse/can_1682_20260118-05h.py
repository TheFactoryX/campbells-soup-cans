"""
Campbell's Soup Can #1682
Produced: 2026-01-18 05:38:46
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

def c(s, code):  # color wrapper using ANSI codes
    return f"\033[{code}m{s}\033[0m"

quote = [
    "You can't separate the scared kid from the existential dread — they're both wearing the same cheap suit."
]

border = "─"
corner = "┌─┐"
hcorner = "└─┘"
vbar  = "│"

def print_line(line, fore='white', back=None):
    sys.stdout.write(c(corner, 96))          # bright cyan corner
    sys.stdout.write(c(border*48, 93))        # bright yellow fill
    sys.stdout.write(c(corner, 96))
    sys.stdout.write("\n")
    sys.stdout.write(c(vbar, 96))
    sys.stdout.write(c(' ' + line + ' ', fore))
    sys.stdout.write(c(vbar, 96))
    sys.stdout.write("\n")

# Print top frame
sys.stdout.write(c(corner, 96))
sys.stdout.write(c(border*48, 93))
sys.stdout.write(c(corner, 96))
sys.stdout.write("\n")
time.sleep(0.1)

# Print the quote inside the frame
for line in quote:
    time.sleep(0.2)
    print_line(line, fore='white')
time.sleep(0.1)

# Print bottom frame
sys.stdout.write(c(hcorner, 96))
sys.stdout.write(c(border*48, 93))
sys.stdout.write(c(hcorner, 96))
sys.stdout.write("\n")
time.sleep(0.1)

# Final punchline
time.sleep(0.2)
sys.stdout.write(c("\nEnjoy the absurdity – it's the only thing that makes sense.", 95))  # bright magenta
sys.stdout.flush()