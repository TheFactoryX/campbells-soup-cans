"""
Campbell's Soup Can #4872
Produced: 2026-08-30 17:30:03
Worker: Google: Gemini 3.5 Flash (google/gemini-3.5-flash)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random
import textwrap

# ANSI Color Codes
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"
GOLD = "\033[38;5;214m"
GRAY = "\033[38;5;244m"
DARK_GRAY = "\033[38;5;238m"
ITALIC = "\033[3m"

def clear_screen():
    """Clears the terminal screen and resets cursor position."""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def center_print(text, color=WHITE, delay=0.0):
    """Prints text centered to the terminal width."""
    terminal_width = 80
    try:
        import os
        terminal_width = os.get_terminal_size().columns
    except Exception:
        pass

    lines = text.split("\n")
    for line in lines:
        stripped = line.strip()
        padding = (terminal_width - len(stripped)) // 2
        sys.stdout.write(" " * max(0, padding) + color + stripped + RESET + "\n")
    sys.stdout.flush()
    if delay > 0:
        time.sleep(delay)

def neurotic_typewriter_box(text_lines, width=58, color=GRAY):
    """Draws a cinematic box and types out the quote with nervous, erratic timing."""
    terminal_width = 80
    try:
        import os
        terminal_width = os.get_terminal_size().columns
    except Exception:
        pass
    
    padding_left = (terminal_width - width) // 2
    pad_str = " " * max(0, padding_left)

    # Top border of the screen frame
    print(pad_str + color + "┌" + "─" * (width - 2) + "┐" + RESET)
    
    for line in text_lines:
        inner_width = width - 4  # Accounts for borders and inner padding
        padded_line = line.center(inner_width)
        
        # Print left border
        sys.stdout.write(pad_str + color + "│ " + RESET)
        sys.stdout.flush()
        
        # Typewriter effect for the inner line with "neurotic" micro-pauses
        for char in padded_line:
            sys.stdout.write(WHITE + char + RESET)
            sys.stdout.flush()
            
            # Simulated erratic typing speed (mimicking anxious hesitation)
            r = random.random()
            if r > 0.98:
                time.sleep(0.25)  # Sudden existential pause
            elif r > 0.92:
                time.sleep(0.12)  # Mild hesitation
            else:
                time.sleep(random.uniform(0.01, 0.04))  # Rapid burst
                
        # Print right border
        sys.stdout.write(color + " │\n" + RESET)
        sys.stdout.flush()
        time.sleep(0.15)

    # Bottom border of the screen frame
    print(pad_str + color + "└" + "─" * (width - 2) + "┘" + RESET)

def main():
    # 1. Vintage Cinematic Intro (Woody Allen's iconic Windsor font titles)
    clear_screen()
    time.sleep(1.0)
    
    # Sound cue simulator
    center_print("\n\n\n\n[ *Soft, melancholic jazz clarinet begins to play* ]\n\n", DARK_GRAY, 2.0)
    clear_screen()

    # Title Card 1: Producers
    center_print("\n\n\n\n\n\n")
    center_print("A", BOLD + WHITE)
    center_print("JACK ROLLINS - CHARLES H. JOFFE", BOLD + WHITE)
    center_print("PRODUCTION", BOLD + WHITE)
    time.sleep(2.2)
    clear_screen()

    # Title Card 2: Movie Title
    center_print("\n\n\n\n\n\n")
    center_print("AN EXCRUCIATING", BOLD + WHITE)
    center_print("EXISTENTIAL CRISIS", BOLD + WHITE)
    time.sleep(2.2)
    clear_screen()

    # Title Card 3: Credits
    center_print("\n\n\n\n\n\n")
    center_print("WRITTEN AND DIRECTED BY", BOLD + WHITE)
    center_print("THE PYTHON INTERPRETER", BOLD + WHITE)
    time.sleep(2.5)
    clear_screen()

    # 2. Main Scene Layout
    terminal_width = 80
    try:
        import os
        terminal_width = os.get_terminal_size().columns
    except Exception:
        pass

    print("\n\n")
    
    # Elegant minimalist Woody Allen glasses ASCII
    glasses = [
        r"      .-----------------.         .-----------------.",
        r"     /   _____________   \       /   _____________   \ ",
        r"    |   /             \   |-----|   /             \   |",
        r"    |  |     (O)       |  |     |  |     (O)       |  |",
        r"    |   \             /   |-----|   \             /   |",
        r"     \   '-----------'   /       \   '-----------'   /",
        r"      '-----------------'         '-----------------'"
    ]

    for line in glasses:
        pad = (terminal_width - len(line)) // 2
        # Highlight lenses in gold, frames in bold gray
        colored_line = line.replace("O", f"{GOLD}O{GRAY}").replace("-", f"{GRAY}-").replace(".", f"{GRAY}.")
        print(" " * max(0, pad) + BOLD + GRAY + line + RESET)
        time.sleep(0.08)

    print("\n")

    # The Philosophical Quote (Custom, highly neurotic/theological Woody Allen style)
    quote = (
        "I've often wondered if God exists. And if He does, I seriously hope "
        "He has a good therapist. Because frankly, creating a universe where "
        "we are forced to age, pay taxes, and wear heavy corduroy trousers "
        "in August feels like an incredibly hostile cry for help."
    )

    # Format and wrap quote to fit aesthetically inside our vintage screen border
    wrapped_lines = textwrap.wrap(quote, width=54)

    # Typewriter animation within the frame
    neurotic_typewriter_box(wrapped_lines, width=58, color=GRAY)

    print("\n")
    # Fade in final sign-off
    center_print("- Woody (or a simulated projection of his neurosis) -", ITALIC + DARK_GRAY)
    print("\n\n")
    time.sleep(1.0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Graceful exit for impatient existentialists
        print(RESET + "\n[ Session aborted. Returning to default reality... ]\n")