"""
Campbell's Soup Can #3612
Produced: 2026-05-09 00:09:55
Worker: Poolside: Laguna XS.2 (free) (poolside/laguna-xs.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"

def typewriter(text, delay=0.03, color=""):
    """Prints text with typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_box():
    """Print decorative box"""
    width = 50
    print(f"{CYAN}╔{'═' * (width-2)}╗{RESET}")
    print(f"{CYAN}║{' ' * (width-2)}║{RESET}")

# Opening
print()
print(f"{YELLOW}{BOLD}   ☆•﹏•☆  WOODY ALLEN-ESQUE PHILOSOPHY  ☆•﹏•☆{RESET}")
print()

# Print top border
print(f"{MAGENTA}{BOLD}╔════════════════════════════════════════════════════════╗{RESET}")
print(f"{MAGENTA}{BOLD}║                                                        ║{RESET}")

# The quote with typewriter effect
quote_lines = [
    f"{RED}  I told my therapist I was feeling existential dread,",
    f"{YELLOW}  She said I should embrace it. I replied that I",
    f"{GREEN}  couldn't embrace anything smaller than my anxiety.",
    f"{BLUE}  Now I'm having an existential crisis about my",
    f"{CYAN}  ability to have existential crises. It's very",
    f"{MAGENTA}  meta. And terrifying.{RESET}"
]

for line in quote_lines:
    print(f"{MAGENTA}{BOLD}║{RESET} {line}{RESET}")
    time.sleep(0.3)

# Print bottom border
print(f"{MAGENTA}{BOLD}║                                                        ║{RESET}")
print(f"{MAGENTA}{BOLD}╚════════════════════════════════════════════════════════╝{RESET}")

print()
print(f"{WHITE}                         - A Neurotic Thought{RESET}")
print()
print(f"{YELLOW}    💭 {RED}To be or not to be... that is the question.{RESET}")
print(f"{YELLOW}    💭 {GREEN}But what if the answer is 'maybe' and you're okay with that?{RESET}")
print()

# Final touch
time.sleep(0.5)
print(f"{CYAN}{BOLD}    (pause for philosophical contemplation... or panic){RESET}")
print()