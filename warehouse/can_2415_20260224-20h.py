"""
Campbell's Soup Can #2415
Produced: 2026-02-24 20:56:27
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI color codes - making it extra Woody with neurotic colors
NEUROTIC_GRAY = '\033[38;5;246m'
ANXIETY_RED = '\033[38;5;196m'
EXISTENTIAL_BLUE = '\033[38;5;33m'
SELF_DEPRECATING_YELLOW = '\033[38;5;226m'
PHILOSOPHICAL_PURPLE = '\033[38;5;129m'
RESET = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'

def neurotic_type(text, color, delay=0.03, jitter=True):
    """Type text with Woody Allen's signature neurotic hesitation"""
    for char in text:
        if jitter and random.random() < 0.1:  # 10% chance of neurotic pause
            time.sleep(0.15)
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def philosophical_annehilation():
    """The ultimate existential crisis in a box"""
    width = 70
    
    # Build the box with existential dread
    print(f"{EXISTENTIAL_BLUE}" + "═" * width + f"{RESET}")
    
    # Top padding
    print(f"{EXISTENTIAL_BLUE}║{' ' * (width-2)}║{RESET}")
    
    # Woody's face in ASCII (barely holding it together)
    woody_face = [
        "   ╭──────────────╮   ",
        "   │  👁️   👁️    │   ",
        "   │      👃     │   ",
        "   │    ╱   ╲    │   ",
        "   │   ╱     ╲   │   ",
        "   ╰──────────────╯   "
    ]
    
    for line in woody_face:
        padding = (width - len(line) - 4) // 2
        print(f"{EXISTENTIAL_BLUE}║{' ' * padding}{ANXIETY_RED}{line}{EXISTENTIAL_BLUE}{' ' * (width - len(line) - padding - 4)}║{RESET}")
    
    print(f"{EXISTENTIAL_BLUE}║{' ' * (width-2)}║{RESET}")
    
    # The quote itself, with proper Wooden self-deprecation
    quote_lines = [
        f"{PHILOSOPHICAL_PURPLE}{BOLD}{ITALIC}“I'm not afraid of death;{RESET}",
        f"{PHILOSOPHICAL_PURPLE}{BOLD}{ITALIC}I just don't want to be there{RESET}",
        f"{PHILOSOPHICAL_PURPLE}{BOLD}{ITALIC}when it happens.”{RESET}"
    ]
    
    for line in quote_lines:
        padding = (width - len(line) - 4) // 2
        print(f"{EXISTENTIAL_BLUE}║{' ' * padding}{line}{' ' * (width - len(line) - padding - 4)}║{RESET}")
    
    # Woody's commentary in smaller, nervous text
    commentary = f"{SELF_DEPRECATING_YELLOW}(He says this while checking his pulse){RESET}"
    padding = (width - len(commentary) - 4) // 2
    print(f"{EXISTENTIAL_BLUE}║{' ' * padding}{commentary}{' ' * (width - len(commentary) - padding - 4)}║{RESET}")
    
    # Bottom padding with existential footnotes
    print(f"{EXISTENTIAL_BLUE}║{' ' * (width-2)}║{RESET}")
    
    footnote = f"{NEUROTIC_GRAY}*Footnote: This quote brought to you by insomnia, anxiety,{RESET}"
    padding = (width - len(footnote) - 4) // 2
    print(f"{EXISTENTIAL_BLUE}║{' ' * padding}{footnote}{' ' * (width - len(footnote) - padding - 4)}║{RESET}")
    
    footnote2 = f"{NEUROTIC_GRAY} and a profound sense that nothing we do matters.{RESET}"
    padding = (width - len(footnote2) - 4) // 2
    print(f"{EXISTENTIAL_BLUE}║{' ' * padding}{footnote2}{' ' * (width - len(footnote2) - padding - 4)}║{RESET}")
    
    print(f"{EXISTENTIAL_BLUE}" + "═" * width + f"{RESET}")
    
    # Final nervous blink
    print(f"\n{NEUROTIC_GRAY}", end="")
    neurotic_type("...but what if I AM there when it happens? That would be SO embarrassing...", NEUROTIC_GRAY, delay=0.04)
    print(f"{RESET}")

if __name__ == "__main__":
    try:
        # Clear screen for dramatic effect (works on most terminals)
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()
        
        # Build tension with dramatic pause
        print(f"{NEUROTIC_GRAY}", end="")
        neurotic_type("Ahem... Woody Allen once pondered...", NEUROTIC_GRAY, delay=0.06)
        print()
        
        time.sleep(0.5)
        philosophical_annehiliation()
        
    except KeyboardInterrupt:
        print(f"\n{ANXIETY_RED}Oh, sorry! Did I bore you? You can leave anytime. I don't mind. Really.{RESET}")
    except Exception as e:
        print(f"\n{SELF_DEPRECATING_YELLOW}Even my code is neurotic and failing. Typical.{RESET}")