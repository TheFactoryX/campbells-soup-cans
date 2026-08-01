"""
Campbell's Soup Can #4396
Produced: 2026-08-01 09:20:44
Worker: Ling-3.0-flash (free) (inclusionai/ling-3.0-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import math

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BG_BLACK = "\033[40m"
BG_BLUE = "\033[44m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"

def slow_print(text, color=WHITE, delay=0.025, end="\n"):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)

def slow_print_centered(text, color=WHITE, delay=0.025, width=70):
    """Print centered text with typewriter effect."""
    padded = text.center(width)
    for char in padded:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay * 0.7)
    sys.stdout.write("\n")

def print_box(title, lines, title_color=CYAN, border_color=BLUE, bg_color=BG_BLACK):
    """Print a decorative ASCII box."""
    width = max(len(title) + 4, max(len(l) for l in lines) + 4, 50)
    top = "╔" + "═" * (width - 2) + "╗"
    bottom = "╚" + "═" * (width - 2) + "╝"
    side = "║"
    
    print(bg_color + border_color + top + RESET)
    
    # Title
    title_line = "║ " + title.center(width - 4) + " ║"
    print(bg_color + border_color + title_line + RESET)
    
    # Separator
    sep = "╠" + "═" * (width - 2) + "╣"
    print(bg_color + border_color + sep + RESET)
    
    # Content lines
    for line in lines:
        content = side + " " + line.ljust(width - 4) + " " + side
        print(bg_color + content + RESET)
    
    print(bg_color + border_color + bottom + RESET)

def print_brain():
    """Print a colorful ASCII brain."""
    brain = [
        (RED, "    .-''''''-."),
        (CYAN, "   /  ~ ~ ~  \\"),
        (GREEN, "  |  (o o o)  |"),
        (YELLOW, "  |  \\_^_^_/  |"),
        (BLUE, "   \\  ~ ~ ~  /"),
        (MAGENTA, "    '-.____.-'"),
        (RED, "     ||||||||"),
        (CYAN, "    / ~~~~~ \\"),
        (GREEN, "   | ~ ~ ~ ~|"),
        (YELLOW, "    \\_~_~_~/"),
        (BLUE, "     '~~~~'"),
    ]
    for color, line in brain:
        print(f"  {color}{line}{RESET}")

def print_woody_hat():
    """Print a simple Woody Allen hat."""
    hat = [
        (CYAN, "        .---."),
        (CYAN, "       /     \\"),
        (CYAN, "      | () () |"),
        (YELLOW, "       \\  ^  /"),
        (YELLOW, "        |---|"),
        (WHITE, "        |   |"),
        (WHITE, "       /     \\"),
        (WHITE, "      |       |"),
    ]
    for color, line in hat:
        print(f"  {color}{line}{RESET}")

def print_neurotic_face():
    """Print a neurotic face."""
    face = [
        (WHITE, "      .-\"\"\"\"\"-. "),
        (WHITE, "     /  o  o  \\ "),
        (YELLOW, "    |    __    |"),
        (YELLOW, "    |   '--'   |"),
        (RED, "     \\  \\__/  / "),
        (RED, "      '-.  .-' "),
        (RED, "        |||||  "),
        (RED, "        |||||  "),
        (RED, "       /    \\  "),
        (RED, "      |      | "),
        (RED, "      |  ()  | "),
        (RED, "       \\    /  "),
        (RED, "        '--'   "),
    ]
    for color, line in face:
        print(f"  {color}{line}{RESET}")

def animated_divider(char="~", width=70, color=CYAN, speed=0.003):
    """Print an animated divider line."""
    line = char * width
    for i in range(len(line)):
        sys.stdout.write(color + line[:i+1] + RESET)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def print_soul_searching():
    """Print animated soul-searching dots."""
    dots = ["...", "....", ".....", "......", ".....", "....", "...", "..", "."]
    colors = [YELLOW, CYAN, MAGENTA, GREEN, BLUE, WHITE]
    for i, d in enumerate(dots):
        c = colors[i % len(colors)]
        sys.stdout.write(f"\r{c}{' '*20}{d}{RESET}")
        sys.stdout.flush()
        time.sleep(0.15)
    sys.stdout.write("\r" + " " * 30 + "\r")

def print_spiral():
    """Print a colorful spiral animation."""
    colors = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]
    for i in range(3):
        for j, c in enumerate(colors):
            angle = (i * 60 + j * 60) * math.pi / 180
            r = 3
            x = int(r * math.cos(angle))
            y = int(r * math.sin(angle))
            offset = " " * max(0, 35 + x)
            sys.stdout.write(f"\r{offset}{c}*{RESET}")
            sys.stdout.flush()
            time.sleep(0.05)
    sys.stdout.write("\r" + " " * 50 + "\r")

def main():
    # Clear screen (optional, works on most terminals)
    print("\033[2J\033[H")
    
    # Animated spiral entrance
    print_spiral()
    
    # Print brain art
    print()
    print_brain()
    print()
    
    # Animated divider
    animated_divider("~", 70, CYAN)
    print()
    
    # Title
    slow_print_centered("🍂  THE EXISTENTIAL MUSINGS  🍂", YELLOW, 0.02, 70)
    slow_print_centered("         by your friendly neighborhood neurotic", DIM, 0.01, 70)
    print()
    
    animated_divider("~", 70, MAGENTA)
    print()
    
    # The main quote in a box
    quote = (
        "I spent my entire life analyzing the meaning of existence, "
        "and I finally realized the meaning of life is that there "
        "is no meaning — which IS the meaning, which means nothing, "
        "which is exactly how I feel about my tax return."
    )
    
    # Word-wrap the quote
    words = quote.split()
    lines = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 <= 60:
            current = (current + " " + word).strip()
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    
    print_box("💭 A PHILOSOPHICAL REVELATION 💭", lines, CYAN, BLUE, BG_BLACK)
    print()
    
    # Animated soul searching
    slow_print("  *twitch*  ", RED, 0.05)
    slow_print("  *sweat*  ", YELLOW, 0.05)
    slow_print("  *stares into void*  ", BLUE, 0.05)
    print()
    print_soul_searching()
    slow_print_centered("  ...I think I need a sandwich.", GREEN, 0.03)
    print()
    
    # Woody hat
    print_woody_hat()
    print()
    
    # Second quote - shorter punchier one
    animated_divider("~", 70, GREEN)
    print()
    
    punchline = "I don't want to achieve immortality through my work. I want to achieve it through not dying. Preferably while eating pasta."
    
    punch_lines = []
    words2 = punchline.split()
    current2 = ""
    for word in words2:
        if len(current2) + len(word) + 1 <= 60:
            current2 = (current2 + " " + word).strip()
        else:
            punch_lines.append(current2)
            current2 = word
    if current2:
        punch_lines.append(current2)
    
    print_box("🔥 THE SECOND THOUGHT 🔥", punch_lines, YELLOW, RED, BG_BLACK)
    print()
    
    # Neurotic face
    print_neurotic_face()
    print()
    
    # Final animated divider
    animated_divider("~", 70, MAGENTA)
    print()
    
    # Credits
    slow_print_centered("© Woody Allen's Ghost (probably)  •  All existential dread reserved", DIM, 0.01, 70)
    slow_print_centered("  Press Enter to exit...", CYAN, 0.02)
    
    input()

if __name__ == "__main__":
    main()