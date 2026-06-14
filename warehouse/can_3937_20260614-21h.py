"""
Campbell's Soup Can #3937
Produced: 2026-06-14 21:40:01
Worker: Poolside: Laguna XS.2 (free) (poolside/laguna-xs.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen-style philosophical quote generator
"""

import time
import sys

def typewriter(text, delay=0.03, color=""):
    """Print text with typewriter effect"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    sys.stdout.write("\033[0m")

def main():
    # ANSI color codes
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    
    # Print decorative header
    print(f"\n{CYAN}{'═'*55}{RESET}")
    print(f"{GREEN}{BOLD}  ╭{'─'*20}╮")
    print(f"{GREEN}{BOLD}  │  WOODY ALLEN'S  │")
    print(f"  │ PSYCHOTIC MUSEUM  │")
    print(f"{GREEN}{BOLD}  ╰{'─'*20}╯{RESET}")
    print(f"{CYAN}{'═'*55}{RESET}\n")
    
    # The philosophical quote
    quote = "I told my therapist I was having an existential crisis. He said, 'Forget it, I'm too busy contemplating my own meaningless existence to help you.'"
    
    # Print quote with typewriter effect
    typewriter(quote, 0.025, YELLOW)
    
    print()
    
    # Print therapist's response
    responses = [
        ("Doctor: ...", BLUE),
        ("Prescription: 200 mgs of meaninglessness daily", RED),
        ("(Patient begins to cry existential tears)", MAGENTA)
    ]
    
    for text, color in responses:
        typewriter(f"  {text}", 0.04, color)
    
    print(f"\n{GREEN}{'─'*55}{RESET}")
    print(f"{CYAN}  (Result: More confused than when he started){RESET}")
    print(f"{GREEN}{'─'*55}{RESET}\n")

if __name__ == "__main__":
    main()