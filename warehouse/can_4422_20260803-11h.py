"""
Campbell's Soup Can #4422
Produced: 2026-08-03 11:43:46
Worker: Google: Gemma 4 26B A4B  (free) (google/gemma-4-26b-a4b-it:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def animate_text(text, delay=0.05, color_code="\033[37m"):
    """Prints text with a typewriter effect and color."""
    for char in text:
        sys.stdout.write(f"{color_code}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(text, border_color="\033[94m"):
    """Draws a stylized box around the text."""
    lines = text.strip().split('\n')
    width = max(len(line) for line in lines) + 4
    
    # Border top
    print(border_color + "╔" + "═" * (width - 2) + "╗" + "\033[0m")
    
    # Content lines
    for line in lines:
        padding = width - len(line) - 2
        print(f"{border_color}║\033[0m {line} {' ' padding}{border_color}║\033[0m")
        
    # Border bottom
    print(f"{border_color}╚" + "═" * (width - 2) + "╝\033[0m")

def main():
    # ANSI Escape Codes
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    RED = "\033[91m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    # The Existential Crisis Frame
    frames = [
        f"{MAGENTA}Thinking about the void...{RESET}",
        f"{YELLOW}Analyzing my neuroses...{RESET}",
        f"{CYAN}Questioning my therapist's credentials...{RESET}",
        f"{RED}Avoidance of mortality in progress...{RESET}"
    ]

    # 1. Intro Animation
    print("\n" * 2)
    for _ in range(2):
        for frame in frames:
            sys.stdout.write(f"\r{frame}")
            sys.stdout.flush()
            time.sleep(0.4)
    print("\n")

    # 2. The Reveal
    quote = (
        "\"I finally decided to seek enlightenment,\n"
        "but then I realized the light at the end of the tunnel\n"
        "might just be an oncoming train, and quite frankly,\n"
        "I'm not ready for that kind of commitment.\""
    )

    # 3. ASCII Art Header
    print(CYAN + r"""
     _____  _    _  _____  _____  _    _ 
    |  __ \| |  | |/ ____||  __ \| |  | |
    | |  | | |  | | |     | |  | | |  | |
    | |  | | |  | | |     | |  | | |  | |
    | |__| | |__| | |____ | |__| | |__| |
     _____| \____/ \_____||_____/ \____/ 
    """ + RESET)
    
    print(f"{YELLOW}--- EXISTENTIAL DREAD SIMULATOR v1.0 ---{RESET}\n")
    time.sleep(1)

    # 4. Print the Quote
    draw_box(quote, border_color=CYAN)

    # 5. Footer
    print(f"\n{MAGENTA}{BOLD}— An Inquiry into the Meaninglessness of it All —{RESET}")
    print(f"{YELLOW}Press Ctrl+C to give up on existence.{RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n\033[91m[System]: Sudden existential exit detected. Much like life.\033[0m")