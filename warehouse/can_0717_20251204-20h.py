"""
Campbell's Soup Can #717
Produced: 2025-12-04 20:37:00
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
from os import system

def clear_screen():
    system('clear' if 'win' not in sys.platform else 'cls')

def colored_print(text, fg_color, bg_color=None):
    fg_code = fg_color.split()
    fg_codes = f"\033[38;2;{fg_code[0]};{fg_code[1]};{fg_code[2]}m"
    bg_code = f"\033[48;2;{bg_color[0]};{bg_code[1]};{bg_code[2]}m" if bg_color else ""
    reset = "\033[0m"
    print(f"{fg_codes}{bg_code}{text}{reset}")

def print_ascii_line(text, fg_color=(255, 255, 255)):
    colored_print(f"┃ {text} ┃", fg_color)

clear_screen()

# Bird animation
bird_frames = [
    "  \\-----/",
    "   \\\\^v^//",
    "     (@)",
    "    (___)",
    "    '-'"
]

# Simulate drawing the bird from top to bottom
for i, frame in enumerate(bird_frames):
    clear_screen()
    for j in range(i):
        print("\n" * (20 // (j + 1)))
        if j < len(bird_frames) - 1:
            colored_print(frame.replace("/", "\\").replace("\\", "/"), (255, 200, 0))
    time.sleep(0.1)

# Pause as bird 'lands'
time.sleep(0.5)

# Bandstand animation
bandstand = [
    "┌──────────────┐",
    "│ ⌐∧⌐∩⌐⌐⌐⌐⌐⌐⌐⌐⌐│",
    "│ ⌐⌐⌐⌐⌐⌐⌐⌐⌐⌐⌐⌐⌐│",
    "└──────────────┘",
    "      (  )    (  )"
]

for i in range(len(bandstand)):
    clear_screen()
    for j in range(i):
        print("\n" * (5 // (j + 1)))
        if j < i:
            colored_print(bandstand[j], (200, 200, 200), (100, 100, 100))
    time.sleep(0.05)

# Final placement
clear_screen()
colored_print("""
██╗  ██╗ █████╗ ███████╗██╗  ██╗███╗   ██╗ ██████╗ 
╚██╗██╔╝██╔══██╗██╔════╝██║  ██║████╗  ██║██╔═══██╗
 ╚███╔╝ ███████║███████╗███████║██╔██╗ ██║██║   ██║
 ██╔██╗ ██╔══██║╚════██║██╔══██║██║╚██╗██║██║   ██║
██╔╝ ██╗██║  ██║███████║██║  ██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                
Psst... you. Yeah, you probably got the job done reasonably well yourself.
Defaulting to nothing less than catastrophic failure. Freshly vacuumed.
                            —Woody Allen
""", (10, 10, 10), (220, 50, 40))

print_ascii_line("", (0, 0, 0))
print_ascii_line("I don't want to achieve immortality through my work;", (255, 100, 255))
print_ascii_line("I want to achieve it through not dying.", (255, 100, 255))
print_ascii_line("", (0, 0, 0))

colored_print("""
                     __
          _,.--.(_,)--._
        ,.' ,,)   (, ,)\ `.
       /  ,'/     ')\ ,)  \\
      /  ,,'       ')\ ,'   \\
     |__,,'         )\_,'    |
    |`---          )_\      ,|
    |               )_\      |
    \               \_\     /
     '--._ _,---,_   \_   ,'
          /       `---' \\
         /                 \\
        /                   \\
       /  (  )              \\
      |     |                  \\
    --'----'----------------------'
""", (150, 150, 150))