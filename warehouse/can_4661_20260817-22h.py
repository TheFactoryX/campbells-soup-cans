"""
Campbell's Soup Can #4661
Produced: 2026-08-17 22:41:03
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

def animate_text(text, delay=0.05, color_code="\033[96m"):
    """Animate text character by character with a typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color_code}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(width=60):
    """Draws a decorative box around the text."""
    print("\n" + "═" * (width + 2))
    print("║" + " " * width + "║")

def main():
    # ANSI Color Codes
    CYAN = "\033[96m"
    PINK = "\033[95m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GRAY = "\033[90m"

    # The Woody Allen Style Quote
    quote = [
        "\"I'm not saying my life is a tragedy,",
        "it's more like a highly improvised,",
        "low-budget dark comedy where the",
        "writer forgot to include a protagonist",
        "who actually enjoys himself.\""
    ]

    # 1. Intro sequence: The "Existential Crisis" Loading Bar
    print(f"\n{GRAY}Initializing Existential Dread...{RESET}")
    for i in range(21):
        percent = i * 5
        bar = "█" * i + "-" * (20 - i)
        sys.stdout.write(f"\r{GRAY}[{bar}] {percent}%{RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

    # 2. Decorative ASCII Art Header
    header_art = r"""
      ____  ____  ____  ____  ____ 
     (  _ \(  _ \(  _ \(  __)(  __)
      ) _ < ) _ < ) _ < ) _)  ) _) 
     (____/(____/(____/(____)(____)
    """
    print(f"{PINK}{header_art}{RESET}")
    print(f"{YELLOW}{BOLD}--- THE NEUROTIC PHILOSOPHER'S DIALECTIC ---{RESET}\n")

    # 3. The Main Quote Animation
    time.sleep(0.5)
    draw_frame(55)
    print("║" + " " * 53 + "║")

    # Print quote lines with staggered animation
    for line in quote:
        # Randomly shift the start to simulate a "shaky" neurotic voice
        indent = " " * random.randint(2, 6)
        sys.stdout.write(f"║{indent}")
        sys.stdout.flush()
        
        # Animate the actual text
        for char in line:
            # Occasional "nervous stutter" effect
            if random.random() < 0.05:
                sys.stdout.write(f"{CYAN}{char}{RESET}")
                sys.stdout.flush()
                time.sleep(0.1)
            
            sys.stdout.write(f"{PINK}{char}{RESET}")
            sys.stdout.flush()
            time.sleep(0.03)
            
        sys.stdout.write(" " * (54 - len(line) - len(indent)) + "║\n")
        time.sleep(0.3)

    draw_frame(55)

    # 4. Outro
    print(f"\n{GRAY}{BOLD}(Press Ctrl+C to end the existential dread or just wait for the void){RESET}")
    time.sleep(2)
    print(f"\n{CYAN}Goodbye. Try not to think about it.{RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{PINK}Even your exit is unplanned and chaotic.{RESET}")
        sys.exit()