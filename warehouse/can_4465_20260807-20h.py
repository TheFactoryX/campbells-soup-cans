"""
Campbell's Soup Can #4465
Produced: 2026-08-07 20:01:32
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

def clear_screen():
    print("\033[2J\033[H", end="")

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def typewriter(text, delay=0.05, color="\033[37m"):
    """Prints text with a typing effect."""
    for char in text:
        sys.stdout.write(color + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(width, height, color="\033[36m"):
    """Draws a stylized border."""
    print(color + "╔" + "═" * (width - 2) + "╗")
    for _ in range(height - 2):
        print(color + "║" + " " * (width - 2) + "║")
    print(color + "╚" + "═" * (width - 2) + "╝\033[0m")

def run_performance():
    # ANSI Colors
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"
    YELLOW = "\033[33m"
    WHITE = "\033[37m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    # The Quote: Neurotic, Existential, Woody Allen-esque
    quote = [
        "\"I have a deep, spiritual dread of the void,",
        "but a much more immediate, practical dread",
        "of having to explain my neuroses at a dinner party.\""
    ]

    # Animation sequence
    clear_screen()
    
    # 1. Intro flicker
    for _ in range(3):
        sys.stdout.write(f"\r\033[K{color_text('LOADING EXISTENTIAL DREAD...', YELLOW, BOLD)}")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write("\r\033[K")
        sys.stdout.flush()
        time.sleep(0.2)

    clear_screen()
    
    # 2. The ASCII "Cigarette Smoke" / Existential Fog effect
    fog_lines = [
        "   (  )  (  ) ",
        "    ) (  ) (  ",
        "   (  )  (  ) ",
        "    ) (  ) (  "
    ]
    
    for _ in range(2):
        for line in fog_lines:
            print(color_text(line.center(60), MAGENTA))
            time.sleep(0.1)

    print("\n" + "="*60 + "\n")

    # 3. The main event: The Typewriter Quote inside a box
    frame_width = 55
    
    # Print the top border
    print(color_text("╔" + "═"*(frame_width-2) + "╗", CYAN))

    # Print the text lines
    for line in quote:
        # Create padding to center text within the frame
        padding = (frame_width - len(line) - 2) // 2
        if padding < 1: padding = 1
        
        line_str = " " * padding + line + " " * (frame_width - len(line) - padding - 2)
        
        # Typewrite the content
        # We use a slightly faster delay for the "nervous" feel
        sys.stdout.write(color_text("║  ", CYAN))
        for char in line_str:
            # Add a slight jitter to the color for "neurotic" effect
            jitter_color = random.choice([CYAN, WHITE, MAGENTA])
            sys.stdout.write(f"{jitter_color}{char}\033[0m")
            sys.stdout.flush()
            time.sleep(0.03)
        sys.stdout.write(color_text("  ║", CYAN))
        print()

    # Print the bottom border
    print(color_text("╚" + "═"*(frame_width-2) + "╝", CYAN))
    
    print("\n")
    typewriter("— A Musician's Mid-Life Crisis", delay=0.1, color=YELLOW)
    print("\n")
    
    # Final dramatic exit
    time.sleep(1)
    print(color_text("[Press Ctrl+C to succumb to the void]", "\033[90m"))
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n" + color_text("Suddenly, nothingness.", MAGENTA))
        time.sleep(1)
        clear_screen()

if __name__ == "__main__":
    # Ensure terminal is cleaned up if interrupted
    try:
        run_performance()
    except Exception:
        print("\033[0m")
        sys.exit(0)