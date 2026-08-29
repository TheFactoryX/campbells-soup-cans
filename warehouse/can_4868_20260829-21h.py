"""
Campbell's Soup Can #4868
Produced: 2026-08-29 21:44:31
Worker: MiniMax: MiniMax M3 (free) (minimax/minimax-m3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ANSI color codes
C = {
    'r': '\033[91m',
    'g': '\033[92m',
    'y': '\033[93m',
    'b': '\033[94m',
    'p': '\033[95m',
    'c': '\033[96m',
    'w': '\033[97m',
    'B': '\033[1m',
    'D': '\033[2m',
    'I': '\033[3m',
    'U': '\033[4m',
    'X': '\033[0m',
}

quote = '"I\'m not afraid of death. I just don\'t want to be\nthere when it happens... unlike my dentist\'s\nwaiting room, where I have NO choice."'

# ASCII art frame
art = f"""
{C['y']}        ╔══════════════════════════════════════════════╗
{C['y']}        ║  {C['c']}~ existential musings from a {C['p']}nervous wreck {C['c']}~{C['y']} ║
{C['y']}        ╚══════════════════════════════════════════════╝{C['X']}
"""

# Animated typing effect
def type_text(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Build the colored quote line by line
lines = [
    f"{C['B']}{C['w']}I'm not afraid of death.{C['X']} {C['D']}{C['w']}I just don't want to be{C['X']}",
    f"{C['B']}{C['w']}there when it happens...{C['X']} {C['I']}{C['c']}(unlike my dentist's{C['X']}",
    f"{C['I']}{C['c']}waiting room, where I have NO choice.){C['X']}",
]

# Animated philosophical pondering person
thinker_frames = [
    f"{C['y']}  () {C['w']}",
    f"{C['y']} (o) {C['w']}",
    f"{C['y']}  () {C['w']}",
    f"{C['y']} (.) {C['w']}",
]

print(C['B'] + C['p'] + "✨ Loading Neurotic Wisdom™ ..." + C['X'])
time.sleep(1)
clear()

# Show ASCII frame with animation
print(art)
time.sleep(0.5)

# Animated thinker head with floating thoughts
for i in range(3):
    print("\033[8;30H" + thinker_frames[i % len(thinker_frames)], end='')
    sys.stdout.flush()
    time.sleep(0.3)

print(C['y'] + "        ┌────────────────────────────────────────┐" + C['X'])
print(C['y'] + "        │                                        │" + C['X'])

# Type each line with color animation
for line in lines:
    print(C['y'] + "        │  " + C['X'], end='')
    type_text(line, 0.03)
    print(C['y'] + "        │" + C['X'])
    time.sleep(0.2)

print(C['y'] + "        │                                        │" + C['X'])
print(C['y'] + "        └────────────────────────────────────────┘" + C['X'])

# Attribution with flair
time.sleep(0.5)
print()
print(f"  {C['I']}{C['c']}                  ~ Woody Allen ~{C['X']}")
print()

# A tiny existential flourish
flourish = f"{C['p']}        ✦  \033[5m(and my therapist agrees)\033[0m  ✦{C['X']}"
print(flourish)
print()

# Bottom philosophizing signature
sig = f"""
{C['D']}{C['b']}    ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
     "If you're not haunted by existence,
      are you even really living?"
                              — me, just now, in therapy{C['X']}
"""
print(sig)