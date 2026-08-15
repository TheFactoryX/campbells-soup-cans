"""
Campbell's Soup Can #4602
Produced: 2026-08-15 09:41:17
Worker: Google: Gemma 4 26B A4B  (free) (google/gemma-4-26b-a4b-it:free)
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

def animate_text(text, color_code):
    """Animates text appearing character by character with a typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color_code}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(0.04)
    print()

def draw_scene():
    """Renders a dramatic, neurotic existentialist frame."""
    # ANSI Color Codes
    RED = "\033[91m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"
    GRAY = "\033[90m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    # The Quote (Woody Allen Style)
    quote = "I'm not saying life is a meaningless void of cosmic indifference... " \
            "but if it were, it's certainly doing a very convincing job of it."

    # The Visual Elements
    box_width = 70
    
    # Clear screen
    print("\033[2J\033[H", end="")

    # 1. Draw a "neurotic" border
    print(MAGENTA + "╔" + "═" * (box_width-2) + "╗" + RESET)
    
    # 2. The "Brain/Cloud" of Anxiety (ASCII Art)
    cloud = [
        f"║ {CYAN}   (o)   (o)   (o)   {RESET}{MAGENTA}  ║",
        f"║  (  )  (  )  (  )  (  )  {RESET}{MAGENTA} ║",
        f"║    {YELLOW}??  ANXIETY  ?{RESET}{MAGENTA}       ║",
        f"║ {GRAY}~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}{MAGENTA} ║"
    ]
    
    for line in cloud:
        # Add random "jitter" to the cloud to represent neurosis
        jitter = " " * random.randint(0, 1)
        print(f"{MAGENTA}║{RESET}{jitter}{line[2:-2]}{jitter}{MAGENTA}║{RESET}")

    # 3. The Quote Container
    quote_text = f"{BOLD}{WHITE}{quote}{RESET}"
    
    # Print the quote lines with a typing effect
    print(MAGENTA + "╠" + "═" * (box_width-2) + "╣" + RESET)
    
    # Split quote into chunks for formatting
    words = quote.split()
    line_length = 50
    current_line = ""
    lines_to_print = []
    
    for word in words:
        if len(current_line) + len(word) < line_length:
            current_line += word + " "
        else:
            lines_to_print.append(current_line.strip())
            current_line = word + " "
    lines_to_print.append(current_line.strip())

    for line in lines_to_print:
        print(f"{MAGENTA}║{RESET} {WHITE}{line.center(box_width-4)}{RESET} {MAGENTA}║{RESET}")

    print(MAGENTA + "╚" + "═" * (box_width-2) + "╝" + RESET)

    # 4. Footer/Atmosphere
    time.sleep(1)
    print(f"\n{GRAY}      [ Status: Existentially Dreadful ]{RESET}")
    time.sleep(0.5)
    print(f"{GRAY}      [ Coffee: Cold | Soul: Lost ]{RESET}")

if __name__ == "__main__":
    try:
        draw_scene()
    except KeyboardInterrupt:
        print("\n\nEven you can't escape the void that quickly.")