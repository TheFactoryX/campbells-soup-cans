"""
Campbell's Soup Can #597
Produced: 2025-11-29 09:31:11
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys

# ANSI escape codes
PINK = '\033[95m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def typewriter(text, color=END, delay=0.03):
    for char in text:
        sys.stdout.write(color + char + END)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def blinking_cursor(duration=3):
    for _ in range(duration * 5):
        sys.stdout.write(YELLOW + '✘ ' + END + '\r')
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('  \r')
        sys.stdout.flush()
        time.sleep(0.1)

art = [
    f"{PINK}╔═════════════════════════════════════════════════╗{END}",
    f"{PINK}║{END}                                               {PINK}║{END}",
    f"{PINK}║{END}    {BOLD}{CYAN}» {YELLOW}WOODY ALLEN'S EXISTENTIAL HOTLINE {CYAN}« {END}    {PINK}║{END}",
    f"{PINK}║{END}                                               {PINK}║{END}",
    f"{PINK}╚═════════════════════════════════════════════════╝{END}"
]

quote = (
    f"{BOLD}{BLUE}I can prove God exists - the proof is due Friday.{END}\n"
    f"{GREEN}The real question is: Will He grade on a curve?{END}\n"
    f"{RED}And does He accept late work from the Pleistocene era?{END}"
)

for line in art[:3]:
    print(line)
    time.sleep(0.2)
print(art[3])
print(art[4])

typewriter("\n" + " "*10 + "« ", YELLOW, 0.1)
typewriter(quote.split('\n')[0], delay=0.04)
typewriter(quote.split('\n')[1], delay=0.04)
typewriter(quote.split('\n')[2] + " »", YELLOW, 0.04)

print(f"\n{UNDERLINE}{PINK}~ The Cosmic Anxiety Hotline is always busy ~{END}")
blinking_cursor()