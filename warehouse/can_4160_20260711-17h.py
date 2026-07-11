"""
Campbell's Soup Can #4160
Produced: 2026-07-11 17:16:30
Worker: Tencent: Hy3 (free) (tencent/hy3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import shutil

RESET = "\033[0m"
BOLD = "\033[1m"
BLINK = "\033[5m"
DIM = "\033[2m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RED = "\033[91m"

def typing_effect(text, delay=0.025, colors=None):
    if colors is None:
        colors = [CYAN, MAGENTA, "\033[94m", "\033[92m"]
    for i, char in enumerate(text):
        sys.stdout.write(colors[i % len(colors)] + char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")

def print_fancy_box(text, color):
    try:
        term_width = shutil.get_terminal_size().columns
    except:
        term_width = 80
    
    box_width = min(term_width - 4, 75)
    words = text.split()
    lines = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 <= box_width - 4:
            current = (current + " " + w).strip()
        else:
            lines.append(current)
            current = w
    if current:
        lines.append(current)
    
    max_len = max(len(l) for l in lines)
    print(color + "\n╔" + "═" * (max_len + 2) + "╗" + RESET)
    for l in lines:
        print(color + "║ " + RESET + l.ljust(max_len) + color + " ║" + RESET)
    print(color + "╚" + "═" * (max_len + 2) + "╝" + RESET)

if __name__ == "__main__":
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    
    sys.stdout.write(YELLOW + BLINK + BOLD + "\n        EXISTENTIAL CRISIS v1.0        \n" + RESET)
    time.sleep(1.2)
    sys.stdout.write("\033[2K")
    
    quote = ("I told the universe I was looking for meaning, but it just gave me a "
             "lactose intolerance and a parking ticket—which confirms my suspicion "
             "that existence is just God's way of saying, 'I, too, have commitment issues.'")
    
    print(DIM + "\n[Initiating neurotic rambling...]\n" + RESET)
    time.sleep(0.8)
    
    typing_effect(quote, delay=0.03)
    
    time.sleep(0.7)
    print_fancy_box("— Woody Allen (hiding from the void)", MAGENTA)
    
    time.sleep(0.3)
    sys.stdout.write(RED + BLINK + "\n<End of transmission. Please take your existential dread and exit.>\n" + RESET)