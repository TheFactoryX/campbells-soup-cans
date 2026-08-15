"""
Campbell's Soup Can #4595
Produced: 2026-08-15 03:04:43
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
import math

def animate_text(text, delay=0.05, color_code="\033[96m"):
    """Prints text with a typewriter effect and color."""
    for char in text:
        sys.stdout.write(f"{color_code}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(quote, name):
    """Draws a neurotic-looking ASCII frame around the text."""
    width = len(quote) + 4
    border = "┌" + "─" * width + "┐"
    bottom = "└" + "─" * width + "┘"
    
    # Colors
    cyan = "\033[96m"
    magenta = "\033[95m"
    yellow = "\033[93m"
    reset = "\033[0m"
    
    print(f"\n{cyan}{border}")
    print(f"│ {magenta}{quote}{cyan} │")
    print(f"{border}{reset}")
    print(f"      {yellow}-{name}-{reset}\n")

def brain_animation():
    """Animate a pulsing, neurotic 'brain' using math."""
    frames = [
        "  ( o )  ",
        " (  o  ) ",
        "(   o   )",
        " (  o  ) ",
        "  ( o )  "
    ]
    for i in range(15):
        # Create a pulsing effect via math
        scale = math.sin(i * 0.5)
        padding = " " * int(abs(scale) * 5)
        brain_char = frames[i % len(frames)]
        print(f"\r{padding}\033[91m{brain_char}\033[0m", end="", flush=True)
        time.sleep(0.15)
    print("\n")

def main():
    # ANSI escape codes for colors
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    # Clear screen (works on most terminals)
    print("\033[2J\033[H", end="")

    print(f"\n{BOLD}{BLUE}Initializing Existential Dread Engine...{RESET}")
    time.sleep(1)
    
    # The Neurotic Brain Animation
    brain_animation()
    
    time.sleep(0.5)
    print(f"{RED}ERROR: Meaning of life not found.{RESET}")
    time.sleep(1)
    print(f"{RED}RETRYING VIA NEUROSIS...{RESET}")
    time.sleep(1.5)
    
    # The Quote
    quote = "My therapist says I have a fear of commitment, but I think I'm just afraid of the universe's " \
            "unbearable lack of attention to my specific neuroses."
    
    # Final Presentation
    print(f"\n{GREEN}--- SYSTEM LOG: PHILOSOPHICAL OUTPUT DETECTED ---\n{RESET}")
    
    draw_frame(quote, "A Neurotic New Yorker")
    
    print(f"{CYAN} [Status: Undetected by God ]{RESET}")
    print(f"{CYAN} [Mood: Slightly Anxious ]{RESET}")
    print(f"{CYAN} [Coffee: Cold         ]{RESET}")
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[91m\nEven your sudden exit is a metaphor for the void.\033[0m")