"""
Campbell's Soup Can #481
Produced: 2025-11-24 04:04:31
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

def print_ansi(text, color):
    print(f"\033[{color}{text}\033[0m", end='')

# Woody Allen-style quotes (neurotic, self-deprecating, existentially funny)
woody_quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "If I'm not back in five minutes, just wait, I'll be longer.",
    "For the sake of argument, let's suppose there is no God. What difference would it make?",
    "I used to think I was indecisive, but now I'm not so sure.",
    "People see me in films and tell me I'm great. They don't know what they're missing.",
    "The most important thing in baseball is hitting. All the rest is聊天."
]

# Colors (ANSI escape codes)
colors = [
    "31",  # Red
    "33",  # Yellow
    "36",  # Cyan
    "35",  # Magenta
    "32"   # Green
]

# ASCII art of Woody Allen
woody_woodpecker = """
\033[1;33m
       _..._
     .'     '.
    /   .-.   \\
   |   /   \   |
   |  |() | |  |
    \  \___/  /
     '.=o.='.
       '---'
\033[0m
"""

def main():
    # Clear screen and move cursor to top
    print("\033[2J\033[H", end='')
    
    # Print title with flair
    print("\033[1;1H" + "==" * 30)
    print("\033[1;21H WOODY WOODPECKER'S PHILOSOPHICAL TRUTH ")
    print("\033[1;21H" + "==" * 30)
    
    # Show Woody's sketch with animation
    sketch = [
        "Straight jaw and thick frame",
        "owI ddowe ysr o llo  t",
        "       d  e    n       e",
        "  wro ohkpe  oo    e  ive",
        "  yry  enp  no  .  w  ings",
        "    e       t         r:."
    ]
    for i, line in enumerate(sketch):
        print_ansi(f"\033[{15+i};1H", random.choice(colors))
        print(line)
    
    print("\n" * 2)
    
    # Progress animation with Woody's face
    eyes = ["o", "0", "°", "©s", "☃"]
    beak = ["^", ">", "]", "#", "*"]
    for _ in range(5):
        print_ansi("\033[1HW", random.choice(colors) + "3")
        print_ansi("o", random.choice(colors))
        print_ansi(f"Io{random.choice(eyes)}", random.choice(colors))
        print_ansi(f" {random.choice(beak)}", random.choice(colors))
        print_ansi("oldf岁", random.choice(colors))
        print()
        time.sleep(0.3)
        print("\033[11A", end=' ')  # Move cursor up
    
    # Clear Woody faces
    print("\033[11A" + " " * 30)
    
    # Print the quote
    quote = random.choice(woody_quotes)
    print("\n\n\033[2J\033[H", end='')  # Clear screen
    
    # Fancy box with quote
    box_width = 40
    print("\033[3;1H\033[1m" + "┌" + "─"*(box_width) + "┐\033[0m")
    
    # Get reduced font size (for proportional display)
    reduced = quote.replace(" ", "~").replace(".", "~").replace(",", "~")
    for i in range(3):
        color_code = random.choice(colors)
        line = reduced[i*10:(i+1)*10]
        print_ansi(f"\033[{5+i};1H│ ", color_code)
        print_ansi(line.ljust(box_width-3), color_code + "1")
        print_ansi("│", color_code)
    
    print("\033[8;1H\033[33;1m" + f"│ {random.choice(woody_woodpecker.strip())}│\033[0m")
    print("\033[10;1H│ " + " "*(box_width-2) + "│")
    print("\033[11;1H" + "\033[33m┌─" + "┴"*box_width + "─┐", end='')
    print("\033[13;1H\033[1;36mM IS FOR MISERY, YOUNG MAN\033[0m")
    
    # Final punchline reveal
    for i in range(box_width):
        print_ansi(f"\033[7;{3+i}H", random.choice(colors) + "41")
        print(" ", end='')
        time.sleep(0.03)
    print("\033[0J", end='')  # Clear screen area

if __name__ == "__main__":
    main()