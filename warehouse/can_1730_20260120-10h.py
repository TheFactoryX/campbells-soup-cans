"""
Campbell's Soup Can #1730
Produced: 2026-01-20 10:47:41
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def woody_print(text, color_code, delay=0.03):
    for char in text:
        sys.stdout.write(f"\033[{color_code}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # ANSI escape codes
    YELLOW = "33"
    CYAN = "36"
    MAGENTA = "35"
    RED = "31"
    BLINK = "5"
    
    # ASCII art with glasses
    woody_art = f"""
    \033[{CYAN}m       .-~~~-.
    (  O   O  )
     |   ∆   |
     \  \_/  /
      `-----'\033[0m
    """
    
    # The existential quote
    quote = """
    The universe is expanding at an alarming rate - much like my waistline 
    after that second slice of cheesecake. I suppose in the end, we're all 
    just cosmic dust with anxiety, wondering if we left the oven on.
    """
    
    # Print the Woody ASCII art
    print(woody_art)
    time.sleep(0.5)
    
    # Create a decorative box
    box_top = f"\033[{CYAN}m╔{'═'*(len(quote.splitlines()[1])+2)}╗\033[0m"
    box_bottom = f"\033[{CYAN}m╚{'═'*(len(quote.splitlines()[1])+2)}╝\033[0m"
    
    # Animate the box and text
    woody_print(box_top, CYAN, 0.01)
    for line in quote.strip().splitlines():
        sys.stdout.write(f"\033[{CYAN}m║\033[0m ")
        woody_print(f"\033[{YELLOW}m{line.center(66)}\033[0m \033[{CYAN}m║", YELLOW)
    woody_print(box_bottom, CYAN, 0.01)
    time.sleep(0.5)
    
    # Blinking attribution
    print(f"\033[{MAGENTA};{BLINK}m\n\t     — Woody Allen's Nervous Subconscious\033[0m")
    time.sleep(0.1)
    
    # Eternal existential cursor blink
    try:
        while True:
            print(f"\033[{RED}m_\033[0m", end="\r")
            time.sleep(0.5)
            print(" \r", end="")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n\033[33mWell, this was fun... in a dystopian sort of way.\033[0m")

if __name__ == "__main__":
    main()