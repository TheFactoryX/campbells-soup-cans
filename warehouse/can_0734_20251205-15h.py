"""
Campbell's Soup Can #734
Produced: 2025-12-05 15:35:30
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import random

# ANSI color codes for that Woody Allen neurotic aesthetic
class Colors:
    NEUROTIC_BLUE = '\033[94m'
    ANXIOUS_YELLOW = '\033[93m'
    THERAPY_GREEN = '\033[92m'
    EXISTENTIAL_RED = '\033[91m'
    NEURO_GREEN = '\033[92m'
    WOODY_WHITE = '\033[97m'
    WOODY_GRAY = '\033[90m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def typewriter_print(text, delay=0.05):
    """Neurotic typing effect - like Woody thinking out loud"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_thought_bubble():
    """ASCII thought bubble with anxious spirals"""
    bubble = f"""
{Colors.NEUROTIC_BLUE}          ╭─────────────────────────────────────╮
{Colors.NEUROTIC_BLUE}          │  {Colors.ANXIOUS_YELLOW}┬─┬  {Colors.WOODY_WHITE}I've had {Colors.EXISTENTIAL_RED}deep thoughts{Colors.WOODY_WHITE} since   {Colors.NEUROTIC_BLUE}   │
{Colors.NEUROTIC_BLUE}          │  {Colors.ANXIOUS_YELLOW}└┬┘  {Colors.WOODY_WHITE}breakfast. Most of them involve   {Colors.NEUROTIC_BLUE}  │
{Colors.NEUROTIC_BLUE}          │     {Colors.WOODY_WHITE}my {Colors.THERAPY_GREEN}mortality{Colors.WOODY_WHITE}, some involve      {Colors.NEUROTIC_BLUE}   │
{Colors.NEUROTIC_BLUE}          │     {Colors.WOODY_WHITE}my {Colors.EXISTENTIAL_RED}inadequacies{Colors.WOODY_WHITE}, a few about     {Colors.NEUROTIC_BLUE}  │
{Colors.NEUROTIC_BLUE}          │     {Colors.WOODY_WHITE}whether I locked the door.           {Colors.NEUROTIC_BLUE}  │{Colors.RESET}
"""
    print(bubble)

def print_woody_face():
    """ASCII Woody Allen - looking appropriately worried"""
    face = f"""
{Colors.EXISTENTIAL_RED}                ╭───╮   ╭───╮
{Colors.EXISTENTIAL_RED}                │ · · │   │ · · │
{Colors.EXISTENTIAL_RED}                ╰┬───╯   ╰┬───╯
{Colors.EXISTENTIAL_RED}                 │  ╭───╮  │
{Colors.EXISTENTIAL_RED}                 │  ╰─┬─╯  │
{Colors.EXISTENTIAL_RED}                ╱│   │   │╲
{Colors.EXISTENTIAL_RED}               ╱ ╰───┴───╯ ╲
{Colors.EXISTENTIAL_RED}              ╱             ╲
{Colors.EXISTENTIAL_RED}             ╱   {Colors.WOODY_WHITE}Brooklyn   {Colors.EXISTENTIAL_RED}   ╲
{Colors.EXISTENTIAL_RED}            ╱   {Colors.NEURO_GREEN}neuroses  {Colors.EXISTENTIAL_RED}    ╲
{Colors.EXISTENTIAL_RED}            ╲   {Colors.THERAPY_GREEN}hereabouts{Colors.EXISTENTIAL_RED}    ╱
{Colors.EXISTENTIAL_RED}             ╲             ╱
{Colors.EXISTENTIAL_RED}              ╲ ╭───────╮ ╱
{Colors.EXISTENTIAL_RED}               ╰─╯       ╰─╯{Colors.RESET}
"""
    print(face)

def print_quotation_box(quote):
    """Fancy box for the neurotic wisdom"""
    width = max(len(quote) + 4, 50)
    
    # Top border with anxious dots
    top = f"{Colors.NEUROTIC_BLUE}╔" + "·" * (width - 2) + "╗"
    
    # Side borders with worried dashes
    sides = f"{Colors.NEUROTIC_BLUE}║  {Colors.WOODY_WHITE}"
    end_sides = f"  {Colors.NEUROTIC_BLUE}║"
    
    # Bottom border with exhausted dots
    bottom = f"{Colors.NEUROTIC_BLUE}╚" + "·" * (width - 2) + "╝"
    
    print(top)
    print(sides + f"{Colors.BOLD}{quote}{Colors.RESET}" + end_sides)
    print(bottom)

def main():
    # Clear screen for maximum neurotic focus
    print('\033[2J\033[H', end='')
    
    # Opening neurotic monologue
    typewriter_print(f"{Colors.ANXIOUS_YELLOW}You know, I've been thinking...{Colors.RESET}", 0.1)
    time.sleep(0.5)
    typewriter_print(f"{Colors.THERAPY_GREEN}About existence. About meaning. About whether{Colors.RESET}", 0.08)
    time.sleep(0.3)
    typewriter_print(f"{Colors.EXISTENTIAL_RED}this coffee is decaf and if that makes me{Colors.RESET}", 0.08)
    time.sleep(0.3)
    typewriter_print(f"{Colors.NEUROTIC_BLUE}some kind of philosophical coward...{Colors.RESET}", 0.1)
    time.sleep(1)
    
    # Show the anxious thought process
    print_thought_bubble()
    
    # Reveal Woody looking appropriately worried
    print_woody_face()
    
    # The moment of truth... dramatic pause
    time.sleep(1.5)
    
    # Print the quote with maximum visual flair
    quote = "I don't mind dying, I just don't want to be there when it happens... and frankly, I'm worried I'll complain about the service."
    
    print(f"\n{Colors.BOLD}{Colors.THERAPY_GREEN}And then it hit me:{Colors.RESET}\n")
    time.sleep(0.8)
    
    print_quotation_box(quote)
    
    # Closing neurotic afterthought
    time.sleep(1.2)
    typewriter_print(f"\n{Colors.WOODY_GRAY}...Do you think they serve espresso in the afterlife?{Colors.RESET}", 0.12)
    typewriter_print(f"{Colors.WOODY_GRAY}Because if not, this whole 'mortality' thing{Colors.RESET}", 0.08)
    typewriter_print(f"{Colors.WOODY_GRAY}seems rather poorly planned.{Colors.RESET}", 0.08)
    
    # Final flourish
    print(f"\n{Colors.NEUROTIC_BLUE}─" * 60 + f"{Colors.RESET}")

if __name__ == "__main__":
    main()