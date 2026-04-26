"""
Campbell's Soup Can #3461
Produced: 2026-04-26 13:41:25
Worker: inclusionAI: Ling-2.6-1T (free) (inclusionai/ling-2.6-1t:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def typewriter(text, delay=0.03, color="\033[93m"):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
    sys.stdout.write("\033[0m")

def flicker(text, times=3):
    for _ in range(times):
        sys.stdout.write("\033[2m" + text + "\033[0m")
        sys.stdout.flush()
        time.sleep(0.15)
        sys.stdout.write("\033[2K\r")
        sys.stdout.flush()
        time.sleep(0.1)

def neurotic_box(quote):
    width = 62
    top = "\033[95m╭" + "─" * width + "╮\033[0m"
    bottom = "\033[95m╰" + "─" * width + "╯\033[0m"
    empty = "\033[95m│" + " " * width + "│\033[0m"
    
    lines = []
    words = quote.split()
    line = ""
    for word in words:
        if len(line) + len(word) + 1 <= width - 6:
            line += word + " "
        else:
            lines.append(line.strip())
            line = word + " "
    if line:
        lines.append(line.strip())
    
    print("\n\033[?25l", end="")
    
    # Anxiety particles
    for _ in range(8):
        x = random.randint(10, 50)
        y = random.randint(0, 10)
        sys.stdout.write(f"\033[{y};{x}H\033[91m✕\033[0m")
    sys.stdout.flush()
    time.sleep(0.3)
    
    print(f"\033[5;20H{top}")
    print(f"\033[6;20H{empty}")
    
    y = 7
    for i, line in enumerate(lines):
        padding = (width - len(line)) // 2
        left = " " * padding
        right = " " * (width - len(line) - padding)
        if i == len(lines) // 2:
            flicker(f"\033[{y};20H│\033[93m{left}『 {line} 』{right}\033[95m│\033[0m")
        else:
            print(f"\033[{y};20H│\033[97m{left}  {line}  {right}\033[95m│\033[0m")
        y += 1
        time.sleep(0.15)
    
    print(f"\033[{y};20H{empty}")
    print(f"\033[{y+1};20H{bottom}")
    
    # Signature doodle
    time.sleep(0.5)
    sig = "  ― W.A. ∿ neurotic & hungry"
    print(f"\033[{y+2};{20+width//2-len(sig)//2}H\033[90m{sig}\033[0m")
    
    # Breathing brackets
    for breath in range(6):
        size = 10 + abs(5 - breath)
        bracket = "⟪" if breath < 3 else "⟫"
        color = "\033[91m" if breath % 2 else "\033[92m"
        print(f"\033[{y+3};{20+width//2}H{color}{bracket}\033[0m", end="")
        sys.stdout.flush()
        time.sleep(0.4)
    
    print(f"\033[{y+3};{20+width//2}H  \033[0m")
    
    # Final sparkle
    sparkles = ["✦", "✧", "☆", "★", "✨"]
    for _ in range(5):
        sx = random.randint(20, 20+width)
        sy = random.randint(5, y+2)
        print(f"\033[{sy};{sx}H{random.choice(sparkles)}\033[0m", end="")
        sys.stdout.flush()
    
    print(f"\033[{y+5};20H\033[90m(⌐□_□) existential dread loading... ✓\033[0m")
    print(f"\033[{y+6};1H\033[?25l", end="")

quote = ("I've come to realize that my only chance at immortality is to "
         "die before my plants do, because at least they have the decency "
         "to pretend they're listening when I talk to them.")

sys.stdout.write("\033[2J\033[H")  # Clear screen
sys.stdout.write("\033[?25l")  # Hide cursor

# Background noise
for _ in range(30):
    print(f"\033[{random.randint(1,40)};{random.randint(1,100)}H\033[2m{random.choice(['·','∙','⁃',' '])}\033[0m", end="")

print("\n")
typewriter("  ⟳  parsing meaning.exe  ⟳  \n\n", 0.08, "\033[94m")
time.sleep(0.5)

neurotic_box(quote)

print(f"\033[{40};1H\033[90m", end="")
typewriter("  [press ENTER to dissolve into cosmic uncertainty]", 0.02)
print("\033[0m")

try:
    input()
except:
    pass

# Dissolve effect
print("\033[?25h\033[0m", end="")
for y in range(1, 45):
    print(f"\033[{y};1H\033[96m", end="")
    for x in range(1, 100):
        if random.random() < 0.3:
            print(random.choice(" .,:;ox%#@"), end="")
    print("\033[0m", end="")
    sys.stdout.flush()
    time.sleep(0.03)

print(f"\033[45;30H\033[91m✓  void accepted\033[0m")
print(f"\033[46;30H\033[0m", end="")
time.sleep(1)
print(f"\033[?25h\033[0m")