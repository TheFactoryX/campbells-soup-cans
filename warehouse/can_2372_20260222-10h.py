"""
Campbell's Soup Can #2372
Produced: 2026-02-22 10:45:07
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

RESET = '\033[0m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'

content_width = 50

def typewriter(text, delay=0.03, color=YELLOW):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)

def print_frame():
    title = "A WOODY ALLEN-STYLE QUOTE"
    title_line = f" {title} ".center(content_width, "•")
    print(RED + title_line + RESET)
    
    print(BLUE + "╔" + "═" * content_width + "╗" + RESET)
    
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens. "
        "Also, I've been having existential dread since breakfast, and my therapist "
        "says I need to 'embrace the void'—but I can't even embrace my own shadow "
        "without tripping over it. At least the void has good posture."
    )
    
    words = quote.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= content_width - 4:
            current_line += (word + " ")
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    
    for i, line in enumerate(lines):
        left_pad = " " * (4 if i % 2 == 0 else 2)
        right_pad = " " * (content_width - len(line) - len(left_pad) - 4)
        framed_line = f"║{left_pad}{line}{right_pad}  ║"
        
        print(BLUE + "║" + RESET, end='')
        sys.stdout.write(" " * (len(left_pad) + 1))
        typewriter(line, 0.02, GREEN if i % 2 == 0 else YELLOW)
        sys.stdout.write(" " * (len(right_pad) + 1))
        print(BLUE + "║" + RESET)
    
    print(BLUE + "╚" + "═" * content_width + "╝" + RESET)
    
    footer = "© 2023 Neurotic Software Division"
    print(GREEN + footer.center(content_width + 2) + RESET)

print("\n" * 5)
print_frame()
print("\n" * 3)