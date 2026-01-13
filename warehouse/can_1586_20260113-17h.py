"""
Campbell's Soup Can #1586
Produced: 2026-01-13 17:43:44
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

ESC = "\033["
RESET = ESC + "0m"

COLORS = [ESC + f"48;2;{random.randint(0,255)};{random.randint(0,255)};{random.randint(0,255)}m" for _ in range(5)]
QUOTE = "i'm afraid death is a roommate. we've been together for 30 years but i still don't trust him. he knows my secrets but keeps them quiet... probably."

def animate_quote(text, screen_rows=25):
    screen_height = os.get_terminal_size().lines
    center = screen_height // 2
    frame = 0
    while frame < screen_height + 1:
        color = random.choice(COLORS)
        line = color + f"{text.center(70)}{RESET}"
        cursor_pos = f"{ESC}{center + int(frame % 5)}{0,j}H"
        sys.stdout.write(cursor_pos + line)
        sys.stdout.flush()
        time.sleep(0.05)
        frame += 1

def main():
    print(ESC + "H\033[J")  # Clear screen
    # Simple header
    print("╔═════════════════════════════════███████{\n║ \033[36mTHE QUOTE\\033[0m                                                                 ║\n╝╠══════════════════════════════════════╝")
    time.sleep(1)
    animate_quote(QUOTE.split('.')[0] + ".")

if __name__ == "__main__":
    main()