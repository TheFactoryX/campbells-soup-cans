"""
Campbell's Soup Can #1453
Produced: 2026-01-07 14:43:07
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Philosophical Quote Generator
A neurotic, existential experience in terminal form.
"""

import sys
import time
import random

# ANSI color codes for that neurotic Woody Allen aesthetic
class Colors:
    NEUROTIC_BLUE = '\033[94m'      # Worry and overthinking
    ANXIOUS_RED = '\033[91m'        # Existential dread
    THERAPIST_GREEN = '\033[92m'    # Self-awareness
    WOODY_GRAY = '\033[90m'         # Dry, intellectual detachment
    EXISTENTIAL_YELLOW = '\033[93m' # Midlife crisis
    NORMAL_WHITE = '\033[97m'       # Momentary clarity
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_typewriter(text, delay=0.03):
    """Print text with that anxious, hesitant Woody Allen rhythm."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_anxiety_box(width=60):
    """Draw a box that looks like it's having an existential crisis."""
    print(f"{Colors.NEUROTIC_BLUE}╔{'═' * (width-2)}╗{Colors.RESET}")
    
    # Randomly add trembling effect to the sides
    for i in range(6):
        left_tremble = ' ' if i % 2 == 0 else '·'
        right_tremble = ' ' if i % 2 == 1 else '·'
        print(f"{Colors.NEUROTIC_BLUE}║{Colors.RESET}{left_tremble}{' ' * (width-4)}{right_tremble}{Colors.NEUROTIC_BLUE}║{Colors.RESET}")
    
    print(f"{Colors.NEUROTIC_BLUE}╚{'═' * (width-2)}╝{Colors.RESET}")

def wavy_line(text, width=60):
    """Make text that looks like it's vibrating with anxiety."""
    chars = list(text)
    result = []
    for i, char in enumerate(chars):
        offset = int(2 * (i % 4 == 0))  # Random wobble
        if i < width - 4:
            result.append(' ' * offset + char)
        else:
            break
    return ''.join(result)

def print_woody_quote():
    """Print a single neurotic, philosophical quote in Woody Allen's style."""
    
    # Woody Allen style quotes (neurotic, self-deprecating, existential)
    quotes = [
        f"{Colors.ANXIOUS_RED}I don't suffer from {Colors.BOLD}existential dread{Colors.RESET}{Colors.ANXIOUS_RED}... I enjoy it.{Colors.RESET}",
        f"{Colors.WOODY_GRAY}My {Colors.EXISTENTIAL_YELLOW}therapist{Colors.RESET}{Colors.WOODY_GRAY} is seeing someone about me.{Colors.RESET}",
        f"{Colors.NEUROTIC_BLUE}I'm not {Colors.BOLD}afraid{Colors.RESET}{Colors.NEUROTIC_BLUE} of {Colors.EXISTENTIAL_YELLOW}death{Colors.RESET}{Colors.NEUROTIC_BLUE}, I'm afraid of {Colors.BOLD}going to the funeral{Colors.RESET}{Colors.NEUROTIC_BLUE}.{Colors.RESET}",
        f"{Colors.ANXIOUS_RED}I took a {Colors.THERAPIST_GREEN}personality test{Colors.RESET}{Colors.ANXIOUS_RED} and found out I'm {Colors.BOLD}negative{Colors.RESET}{Colors.ANXIOUS_RED}.{Colors.RESET}",
        f"{Colors.EXISTENTIAL_YELLOW}My {Colors.NORMAL_WHITE}mother{Colors.RESET}{Colors.EXISTENTIAL_YELLOW} told me I could be anything... so I chose {Colors.BOLD}anxiety{Colors.RESET}{Colors.EXISTENTIAL_YELLOW}.{Colors.RESET}",
        f"{Colors.WOODY_GRAY}I don't need {Colors.THERAPIST_GREEN}therapy{Colors.RESET}{Colors.WOODY_GRAY}, I just need someone to {Colors.BOLD}listen{Colors.RESET}{Colors.WOODY_GRAY} to my problems about not having anyone to listen.{Colors.RESET}",
        f"{Colors.NEUROTIC_BLUE}I'm not {Colors.BOLD}pessimistic{Colors.RESET}{Colors.NEUROTIC_BLUE}, I'm just {Colors.EXISTENTIAL_YELLOW}accurately{Colors.RESET}{Colors.NEUROTIC_BLUE} assessing the {Colors.ANXIOUS_RED}hopelessness{Colors.RESET}{Colors.NEUROTIC_BLUE} of existence.{Colors.RESET}",
        f"{Colors.ANXIOUS_RED}I have a {Colors.BOLD}phobia{Colors.RESET}{Colors.ANXIOUS_RED} of {Colors.EXISTENTIAL_YELLOW}phobias{Colors.RESET}{Colors.ANXIOUS_RED}... and also {Colors.THERAPIST_GREEN}therapists{Colors.RESET}{Colors.ANXIOUS_RED}.{Colors.RESET}"
    ]
    
    quote = random.choice(quotes)
    
    # Visual presentation with neurotic energy
    print("\n" * 2)
    
    # Draw the anxiety box
    draw_anxiety_box(70)
    
    # Print the quote with typewriter effect
    print(f"{Colors.NORMAL_WHITE}│{Colors.RESET} ", end="")
    print_typewriter(f"{quote}", 0.05)
    
    # More box drawing
    draw_anxiety_box(70)
    
    # Add Woody Allen signature with shaky effect
    signature = "─ " + Colors.WOODY_GRAY + "Woody Allen" + Colors.RESET + " (probably on the couch)"
    print(wavy_line(signature, 70))
    
    # Add a neurotic footnote
    print(f"\n{Colors.WOODY_GRAY}{Colors.BOLD}P.S.{Colors.RESET}{Colors.WOODY_GRAY} This quote may cause mild {Colors.ANXIOUS_RED}discomfort{Colors.RESET}{Colors.WOODY_GRAY}, {Colors.EXISTENTIAL_YELLOW}existential questioning{Colors.RESET}{Colors.WOODY_GRAY}, or the sudden urge to call your {Colors.THERAPIST_GREEN}therapist{Colors.RESET}{Colors.WOODY_GRAY}.{Colors.RESET}")
    
    # Final visual flourish - a spiraling thought pattern
    print(f"\n{Colors.NEUROTIC_BLUE}💭{Colors.RESET} " + f"{Colors.WOODY_GRAY}💭{Colors.RESET} " * 5 + f"{Colors.NEUROTIC_BLUE}💭{Colors.RESET}")

def main():
    """Main function - run the neurotic quote generator."""
    # Clear screen for dramatic effect
    print("\033[2J\033[H", end="")  # Clear and move cursor to top
    
    print(f"\n{Colors.BOLD}{Colors.EXISTENTIAL_YELLOW}╔══════════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.EXISTENTIAL_YELLOW}║{Colors.RESET}                   {Colors.NEUROTIC_BLUE}WOODY ALLEN{Colors.RESET}                       {Colors.BOLD}{Colors.EXISTENTIAL_YELLOW}║{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.EXISTENTIAL_YELLOW}║{Colors.RESET}              {Colors.WOODY_GRAY}Philosophical Quote Generator{Colors.RESET}              {Colors.BOLD}{Colors.EXISTENTIAL_YELLOW}║{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.EXISTENTIAL_YELLOW}╚══════════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    print_woody_quote()

if __name__ == "__main__":
    main()