"""
Campbell's Soup Can #5280
Produced: 2026-11-27 02:10:20
Worker: Qwen: Qwen3.7 Max (qwen/qwen3.7-max)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"

# Colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright colors
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Background colors
BG_BLACK = "\033[40m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.04, color=""):
    """Print text with a typewriter effect."""
    if color:
        sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if color:
        sys.stdout.write(RESET)

def print_frame(lines, border_color=BRIGHT_YELLOW, text_color=BRIGHT_WHITE):
    """Print a beautifully framed box."""
    max_len = max(len(line) for line in lines)
    top = f"{'╔'}{'═' * (max_len + 4)}{'╗'}"
    bottom = f"{'╚'}{'═' * (max_len + 4)}{'╝'}"
    
    print(f"{border_color}{top}{RESET}")
    for line in lines:
        padding = max_len - len(line)
        print(f"{border_color}║{RESET}  {text_color}{line}{RESET}{' ' * padding}  {border_color}║{RESET}")
    print(f"{border_color}{bottom}{RESET}")

def animate_glasses():
    """Animate Woody Allen-style glasses appearing."""
    frames = [
        "         ",
        "    ○  ○ ",
        "   ─○──○─",
        "  ══○══○═",
        " ╔═○══○═╗",
        "║ ╔═○══○═╗",
    ]
    
    glasses_final = [
        r"    _______    _______",
        r"   |       |  |       |",
        r"   |  ◉    |──|  ◉    |",
        r"   |       |  |       |",
        r"    -------    -------",
        r"        \________/",
    ]
    
    for i, frame in enumerate(glasses_final):
        clear_screen()
        print()
        print()
        # Print frames revealed so far
        for j in range(i + 1):
            color = BRIGHT_CYAN if j == i else CYAN
            print(f"        {color}{glasses_final[j]}{RESET}")
        print()
        time.sleep(0.3)

def sparkle_text(text, colors):
    """Print text with alternating colors."""
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(f"{color}{char}")
        sys.stdout.flush()
    print(RESET)

def main():
    clear_screen()
    
    # Animated title
    print()
    title = "✦  EXISTENTIAL DREAD QUOTE OF THE DAY  ✦"
    sys.stdout.write(f"{BOLD}{BRIGHT_YELLOW}")
    for i, char in enumerate(title):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print(f"{RESET}")
    print()
    
    # ASCII art glasses animation
    animate_glasses()
    time.sleep(0.5)
    
    # The quote
    clear_screen()
    print()
    
    # Woody Allen ASCII art portrait (simplified)
    portrait = [
        r"          _______________",
        r"         /               \",
        r"        |    _________    |",
        r"        |   |  ○   ○  |   |",
        r"        |   |_________|   |",
        r"        |       ‿‿        |",
        r"        |    \_______/    |",
        r"         \_______________/",
        r"            |    |    |",
        r"           ╔════════════╗",
    ]
    
    for line in portrait:
        print(f"    {DIM}{BRIGHT_WHITE}{line}{RESET}")
    
    print()
    print()
    
    # Main quote with dramatic typewriter effect
    quote = "The universe is completely indifferent to human suffering."
    quote2 = "Which, honestly, is a relief — because I am also indifferent"
    quote3 = "to most things, except gluten, small talk, and the creeping"
    quote4 = "suspicion that my therapist is Googling me during sessions."
    
    quote_lines = [quote, quote2, quote3, quote4]
    
    print(f"    {BRIGHT_WHITE}{BOLD}\"", end="")
    for i, line in enumerate(quote_lines):
        typewriter(line, delay=0.035, color=BRIGHT_WHITE)
        if i < len(quote_lines) - 1:
            print()
            print(f"     ", end="")
    print(f"\"{RESET}")
    
    print()
    time.sleep(0.3)
    
    # Attribution with fancy formatting
    attr = "— Woody Allen (probably, on a Tuesday, after lunch)"
    typewriter(f"                    {ITALIC}{BRIGHT_BLACK}{attr}{RESET}", delay=0.04)
    
    print()
    print()
    
    # Decorative bottom
    stars = "·  ★  ·  ✦  ·  ★  ·  ✦  ·  ★  ·  ✦  ·  ★  ·  ✦  ·  ★  ·"
    colors_list = [BRIGHT_YELLOW, YELLOW, BRIGHT_YELLOW, YELLOW, DIM + YELLOW]
    
    print("    ", end="")
    sparkle_text(stars, colors_list)
    
    print()
    
    # Fun footer
    footer = "[ Life is a tale told by an idiot — and I should know, I'm telling this one. ]"
    print(f"    {DIM}{MAGENTA}{footer}{RESET}")
    
    print()
    
    # Animated thinking dots
    sys.stdout.write(f"    {BRIGHT_CYAN}Thinking about mortality")
    sys.stdout.flush()
    for i in range(3):
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
    
    print(f"{RESET}")
    time.sleep(0.3)
    
    # Final punchline
    punchline = "...maybe I should have been an accountant."
    print(f"    {BRIGHT_RED}{BOLD}{punchline}{RESET}")
    
    print()
    print()

if __name__ == "__main__":
    main()