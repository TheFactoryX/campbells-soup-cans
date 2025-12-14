"""
Campbell's Soup Can #936
Produced: 2025-12-14 21:29:53
Worker: Amazon: Nova 2 Lite (free) (amazon/nova-2-lite-v1:free)
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

# ANSI escape codes
RESET = "\033[0m"
GREEN_BG = "\033[42m"
WHITE_FG = "\033[37m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

def spinning_cursor(duration):
    chars = "◧◧◧◧"  # Wooden spinning effect
    end_time = time.time() + duration
    index = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{YELLOW}☕ {chars[index]} {RESET} Brewing existential dread...")
        sys.stdout.flush()
        time.sleep(0.1)
        index = (index + 1) % len(chars)
    sys.stdout.write("\r" + " " * 40 + "\r")

def draw_wooden_frame(text, width):
    border_top = f"{GREEN_BG}{WHITE_FG}╔{'═' * (width - 2)}╗{RESET}"
    border_mid = f"{GREEN_BG}{WHITE_FG}║ {text.center(width - 2)} ║{RESET}"
    border_bot = f"{GREEN_BG}{WHITE_FG}╚{'═' * (width - 2)}╝{RESET}"
    return [border_top, border_mid, border_bot]

def main():
    spinning_cursor(2)
    
    quote = "I'd love to avoid responsibility, but even my couch judges me."
    
    try:
        terminal_width = shutil.get_terminal_size().columns
    except:
        terminal_width = 80
    
    frame_width = min(terminal_width - 4, 60)
    frame = draw_wooden_frame(quote, frame_width)
    
    # Woody Allen glasses ASCII art
    glasses = f"{CYAN}  __  {RESET}"
    nose = f"{CYAN} /  \\ {RESET}"
    
    print("\n")
    print(glasses)
    print(nose)
    print("\n")
    for line in frame:
        print(line)
    print("\n")
    print(f"{CYAN}✨ Remember: The only thing worse than being pursued by meaning is being caught.✨{RESET}")

if __name__ == "__main__":
    main()