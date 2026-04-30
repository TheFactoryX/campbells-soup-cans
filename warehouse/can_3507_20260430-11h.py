"""
Campbell's Soup Can #3507
Produced: 2026-04-30 11:53:30
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

def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_line():
    sys.stdout.write("\033[K")

def cursor_up(n=1):
    sys.stdout.write(f"\033[{n}A")

def cursor_down(n=1):
    sys.stdout.write(f"\033[{n}B")

def hide_cursor():
    sys.stdout.write("\033[?25l")

def show_cursor():
    sys.stdout.write("\033[?25h")

def cls():
    sys.stdout.write("\033[2J\033[H")

# Colors
BOLD = "\033[1m"
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
GRAY = "\033[90m"

def animated_frame():
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for _ in range(20):
        f = random.choice(frames)
        color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN])
        sys.stdout.write(f"\r{color}{BOLD}{f}  Existential crisis loading...{RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
    clear_line()
    cursor_up(1)

def draw_brain():
    brain = [
        "        .-----.      ",
        "      .'   o   '.    ",
        "     /   o   o   \\   ",
        "    |    \\___/    |  ",
        "    |   /     \\   |  ",
        "    |  | () () |  |  ",
        "    |   \\  _  /   |  ",
        "     \\   '---'   /   ",
        "      '.  ooo  .'    ",
        "        '-----'      ",
    ]
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, RED, GREEN, YELLOW, BLUE]
    y, x = 5, 55
    for i, line in enumerate(brain):
        sys.stdout.write(f"\033[{y+i};{x}H{colors[i]}{line}{RESET}")
    sys.stdout.flush()

def draw_coffee():
    cup = [
        "        .-------.    ",
        "      .'       '.  ",
        "     /           \\ ",
        "    |  ~   ~   ~  | ",
        "    |  ~   ~   ~  | ",
        "    |  ~   ~   ~  | ",
        "     \\           / ",
        "      '._______.'   ",
        "         | | |      ",
        "         | | |      ",
        "        /| | |\\     ",
        "       / | | | \\    ",
    ]
    y, x = 3, 10
    for i, line in enumerate(cup):
        sys.stdout.write(f"\033[{y+i};{x}H{YELLOW}{line}{RESET}")
    sys.stdout.flush()

def draw_wallpaper():
    # Background dots
    for _ in range(30):
        ry = random.randint(1, 30)
        rx = random.randint(1, 110)
        c = random.choice([GRAY, BLUE, MAGENTA])
        sys.stdout.write(f"\033[{ry};{rx}H{c}·{RESET}")
    sys.stdout.flush()

def main():
    hide_cursor()
    cls()
    
    # Draw subtle wallpaper
    draw_wallpaper()
    
    # Title
    title = "🫠 WOODY'S EXISTENTIAL CRISIS GENERATOR 3000 🧠"
    sys.stdout.write(f"\033[2;20H{BOLD}{CYAN}{title}{RESET}")
    sys.stdout.flush()
    
    # Draw decorations
    draw_brain()
    draw_coffee()
    
    # Animated loading
    sys.stdout.write(f"\033[18;30H")
    animated_frame()
    
    # Box around quote
    quote_lines = [
        "  I told my psychiatrist I get anxious                  ",
        "  every time I think about the infinite void of         ",
        "  nothingness that awaits us all, and he said,         ",
        "  'That's normal. I bill extra for existential dread.' ",
        "                                                         ",
        "  So now I'm anxious about the bill AND the void,       ",
        "  which means I'm paying double to worry about          ",
        "  absolutely nothing. It's very cost-effective.         ",
    ]
    
    box_top = "   " + "╭" + "─" * 68 + "╮"
    box_bottom = "   " + "╰" + "─" * 68 + "╯"
    
    y_start = 22
    
    # Print box with animation
    sys.stdout.write(f"\033[{y_start};1H{BOLD}{MAGENTA}{box_top}{RESET}")
    for i, line in enumerate(quote_lines):
        sys.stdout.write(f"\033[{y_start+1+i};1H{BOLD}{MAGENTA}│{RESET} {GRAY}{line}{RESET} {BOLD}{MAGENTA}│{RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write(f"\033[{y_start+len(quote_lines)+1};1H{BOLD}{MAGENTA}{box_bottom}{RESET}")
    sys.stdout.flush()
    
    # Signature with sparkle
    sparkle = random.choice(["✨", "⭐", "🌟", "💫", "❇"])
    signature = f"    — Woody (probably) {sparkle}"
    sys.stdout.write(f"\033[{y_start+len(quote_lines)+3};20H{BOLD}{YELLOW}{signature}{RESET}")
    sys.stdout.flush()
    
    # Floating particles animation
    particles = ["*", ".", "o", "·", "∙"]
    for _ in range(40):
        py = random.randint(1, 35)
        px = random.randint(1, 115)
        pc = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA])
        pp = random.choice(particles)
        sys.stdout.write(f"\033[{py};{px}H{pc}{pp}{RESET}")
        sys.stdout.flush()
        time.sleep(0.03)
    
    # Footer pulse
    footer = "  (The void is still there. Have a nice day. 💔)"
    for i in range(6):
        color = [RED, MAGENTA, CYAN, BLUE][i % 4]
        sys.stdout.write(f"\033[37;25H{color}{BOLD}{footer}{RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
    
    sys.stdout.write(f"\033[37;1H\n")
    show_cursor()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        cls()
        print("Fled from existential dread. Smart move.")