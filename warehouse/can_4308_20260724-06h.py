"""
Campbell's Soup Can #4308
Produced: 2026-07-24 06:39:27
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
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def typewriter_effect(text, speed=0.05, color="\033[37m"):
    """Prints text character by character for dramatic effect."""
    for char in text:
        sys.stdout.write(color_code + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(speed)
    print()

def draw_frame(content_height, width=60):
    """Draws a neurotic-looking ASCII frame."""
    top = "┌" + "─" * (width - 2) + "┐"
    bottom = "└" + "─" * (width - 2) + "┘"
    side = "│"
    
    print(color_text(top, "\033[90m"))
    for _ in range(content_height):
        padding = " " * ((width - 2) // 2)
        # Adding some jitter/dots to represent anxiety
        jitter = "".join(random.choice([".", " ", " ", "~"]) for _ in range((width - 10) // 2))
        print(f"{side} {padding}{jitter}{padding} {side}")
    print(color_text(bottom, "\033[90m"))

def main():
    # ANSI Colors
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    MAGENTA = "\033[35m"
    RESET = "\033[0m"
    DIM = "\033[2m"

    clear_screen()

    # Intro Animation: The Neurotic Pulse
    for _ in range(3):
        clear_screen()
        print("\n\n\n" + color_text("LOADING EXISTENTIAL DREAD...", YELLOW, RESET))
        time.sleep(0.4)
        clear_screen()
        print("\n\n\n" + color_text("...OR MAYBE JUST A PANIC ATTACK.", MAGENTA))
        time.sleep(0.4)

    clear_screen()
    print("\n\n")
    
    # The Quote Content
    quote = "I'm not saying I'm looking for the meaning of life; I'm just suggesting that if I don't find it by Tuesday, I'm going to be very annoyed with the universe."
    
    # ASCII Art Title
    art = [
        "  _____  ____  _____  __  __  _____ ",
        " |  __ \|  _ \|  __ \|  \/  | |  __ |",
        " | |  | | | | | |  | | |\/| | | |  | |",
        " | |__| | |_| | |__| | |  | | | |__| |",
        " |_____/\____/|_____/|_|  |_| |_____/ "
    ]

    for line in art:
        print(color_text(line, CYAN))
    
    print("\n" + color_text("--- AN EXTREMELY UNCERTAIN THOUGHT ---", DIM))
    print("\n")

    # Typewrite the quote
    typewriter_effect(quote, speed=0.04, color=YELLOW)

    print("\n" + color_text("--- END OF THOUGHT (PROBABLY) ---", DIM))

    # Final visual flourish: A flickering "Anxiety Aura"
    try:
        for _ in range(10):
            sys.stdout.write("\r" + color_text("  [ Existentialism is exhausting. Please wait. ] ", MAGENTA))
            sys.stdout.flush()
            time.sleep(0.2)
            sys.stdout.write("\r" + color_text("  [ Existentialism is exhausting. Please wait. ] ", CYAN))
            sys.stdout.flush()
            time.sleep(0.2)
    except KeyboardInterrupt:
        pass

    print("\n")

if __name__ == "__main__":
    main()