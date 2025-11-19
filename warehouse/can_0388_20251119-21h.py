"""
Campbell's Soup Can #388
Produced: 2025-11-19 21:26:52
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random

# ANSI color codes
YELLOW = "\033[93m"
PINK = "\033[95m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Our existential Woody Allen-style quote
quote = (
    "Life is a tragicomedy written by a committee of cosmic clowns who forgot " 
    "the punchlines, and yet I still worry they're judging my performance."
)

# Animated rolling eyes ASCII art
def rolling_eyes():
    frames = [
        r'''
         _____
        ( o o )
         \ - / 
          ---  
        ''',
        r'''
         _____
        ( - - )
         \ ~ / 
          ---  
        ''',
        r'''
         _____
        ( @ @ )
         \ O / 
          ---  
        '''
    ]
    for _ in range(3):
        for frame in frames:
            print(f"\033[2J\033[H")  # Clear screen
            print(f"{YELLOW}{frame}{RESET}")
            time.sleep(0.3)

# Fancy typewriter effect with neurotic pauses
def neurotic_print(text):
    words = text.split()
    for i, word in enumerate(words):
        print(f"{BOLD}{PINK}{word}{RESET}", end=' ', flush=True)
        # Add dramatic pauses at random intervals
        if random.random() < 0.3 or ',' in word or '.' in word:
            time.sleep(0.4 * random.uniform(0.5, 2.5))
        else:
            time.sleep(0.05 * random.uniform(0.8, 1.2))
        # Add self-doubt after certain words
        if random.random() < 0.15 and i > 3:
            print(f"{CYAN}(or is it?){RESET}", end=' ', flush=True)
            time.sleep(0.8)
    print("\n")

# Create conversation bubble
def create_bubble(text):
    lines = []
    current_line = ""
    for word in text.split():
        if len(current_line) + len(word) + 1 <= 35:
            current_line += " " + word
        else:
            lines.append(current_line.strip())
            current_line = word
    if current_line:
        lines.append(current_line.strip())

    max_len = max(len(line) for line in lines)
    bubble = [
        f"{YELLOW}   ╭{''.join(['─']*(max_len+2))}╮{RESET}",
        *[f"{YELLOW}   │ {RED}{line.center(max_len)}{YELLOW} │{RESET}" for line in lines],
        f"{YELLOW}   ╰{''.join(['─']*(max_len+2))}╯{RESET}",
        f"{YELLOW}       \\   {RESET}",
        f"{YELLOW}        o  {RESET}"
    ]
    return "\n".join(bubble)

# Woody's neurotic avatar
woody = f"""
{RED}
    /////\\\\\\\
   | 0   0 |
   |   ∆   |
    \\_____/
     |   |
     |___|
    /     \\
   |       |
   |       |
   |_______|
{YELLOW}  W o o d y 
   A l l e n 
{RESET}"""

# Main program
def main():
    rolling_eyes()
    print("\n" * 2)
    print(create_bubble(quote))
    print(woody)
    time.sleep(1)
    print(f"\n{CYAN}And then he said:{RESET}")
    neurotic_print(f"{PINK}{quote}{RESET}")
    print(f"{YELLOW}*Exits stage left while questioning reality*{RESET}")

if __name__ == "__main__":
    main()