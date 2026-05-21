"""
Campbell's Soup Can #3741
Produced: 2026-05-21 05:19:22
Worker: Z.ai: GLM 5.1 (z-ai/glm-5.1)
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

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BG_BLACK = "\033[40m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"

def typewriter(text, delay=0.03, color=WHITE):
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        if char in '.!?—':
            time.sleep(0.4)
        elif char == ',':
            time.sleep(0.15)
        else:
            time.sleep(delay)

def draw_neurotic_border(width, height):
    frames = [
        [CYAN, MAGENTA, YELLOW],
        [MAGENTA, YELLOW, CYAN],
        [YELLOW, CYAN, MAGENTA],
    ]
    colors = random.choice(frames)
    
    top = f"{colors[0]}╔{'═' * width}╗{RESET}"
    mid = f"{colors[1]}║{' ' * width}║{RESET}"
    bot = f"{colors[2]}╚{'═' * width}╝{RESET}"
    return top, mid, bot

def nervous_twitch():
    twitches = ["┬─┬", "╯°□°)╯", "┻━┻", "(╯°□°)╯︵ ┻━┻", "┬─┬ノ(º_ºノ)", "...sorry"]
    for t in twitches:
        sys.stdout.write(f"\r  {DIM}{RED}{t}{RESET}   ")
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\r" + " " * 30 + "\r")
    sys.stdout.flush()

def main():
    # Clear screen
    sys.stdout.write("\033[2J\033[H")
    
    # Dramatic pause with flickering glasses
    glasses = [
        f"{DIM}    ∪   ∪{RESET}",
        f"{DIM}   ○   ○{RESET}",
        f"{DIM}   ∩   ∩{RESET}",
    ]
    
    for _ in range(3):
        for g in glasses:
            sys.stdout.write(f"\r{g}")
            sys.stdout.flush()
            time.sleep(0.15)
    
    sys.stdout.write("\n\n")
    
    # Shaking intro
    intro_lines = [
        f"{DIM}{ITALIC}  (clears throat nervously){RESET}",
        "",
    ]
    for line in intro_lines:
        print(line)
        time.sleep(0.5)
    
    # The quote
    quote = "I've finally figured out the meaning of life — it's a test, and I forgot to study, and the proctor is my mother, and she's very disappointed."
    
    # Build the bordered box
    inner_width = len(quote) + 4
    top, mid, bot = draw_neurotic_border(inner_width, 1)
    
    # Print top border with animation
    print(f"  {top}")
    time.sleep(0.3)
    
    # Print the quote line by line inside the box
    print(f"  {mid}")
    sys.stdout.write(f"  {CYAN}║ {RESET}")
    
    # Typewriter the quote with nervous energy
    typewriter(quote, delay=0.025, color=BOLD + YELLOW)
    
    sys.stdout.write(f"{CYAN} ║{RESET}")
    print()
    print(f"  {mid}")
    print(f"  {bot}")
    
    time.sleep(0.8)
    
    # Attribution
    print()
    time.sleep(0.3)
    sys.stdout.write(f"      {DIM}{ITALIC}— Probably Woody Allen{RESET}")
    sys.stdout.flush()
    time.sleep(0.5)
    
    # Nervous afterthought
    print()
    print()
    time.sleep(1.0)
    
    # The twitch
    nervous_twitch()
    
    # Bonus anxious footer
    time.sleep(0.5)
    footers = [
        f"    {DIM}{RED}(I should call my therapist.){RESET}",
        f"    {DIM}{BLUE}(Is it hot in here?){RESET}",
        f"    {DIM}{MAGENTA}(I knew I should've stayed in bed.){RESET}",
    ]
    chosen = random.choice(footers)
    
    for char in chosen:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    
    print()
    print()
    
    # One final existential shrug in ASCII
    shrug = f"    {DIM}¯\\_(ツ)_/¯{RESET}"
    print(shrug)
    print()

if __name__ == "__main__":
    main()