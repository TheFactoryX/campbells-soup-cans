"""
Campbell's Soup Can #815
Produced: 2025-12-09 10:42:20
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

# ANSI color codes for that Woody Allen neurotic vibe
class Colors:
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    RESET = '\033[0m'
    DIM = '\033[2m'

def typewriter(text, delay=0.03, color=Colors.WHITE):
    """Type out text like a neurotic playwright at 3 AM"""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_therapy_couch():
    """ASCII art of Woody Allen on a therapy couch"""
    couch_art = f"""
{Colors.CYAN}          ╭─────────────────────────────────────╮
          │  {Colors.BOLD}Woody Allen's Existential Advice{Colors.RESET}  │
          ╰─────────────────────────────────────╯
    
                    {Colors.MAGENTA}(╯°□°)╯︵ ┻━┻{Colors.RESET}
                
                {Colors.GREEN}┌─════════════════─┐{Colors.RESET}
                {Colors.GREEN}│{Colors.WHITE}   ╭─╮   ╭─╮   {Colors.GREEN}│{Colors.RESET}
                {Colors.GREEN}│{Colors.WHITE}   ╰┬┬╯   ╰┬┬╯   {Colors.GREEN}│{Colors.RESET}
                {Colors.GREEN}│{Colors.WHITE}    ╰╯     ╰╯    {Colors.GREEN}│{Colors.RESET}
                {Colors.GREEN}└─════════════════─┘{Colors.RESET}
    
    """
    print(couch_art)

def print_thought_bubble():
    """ASCII thought bubble with neurotic energy"""
    bubble = f"""
{Colors.YELLOW}                  .-""""""-.
{Colors.YELLOW}                 /   o   o  \\
{Colors.YELLOW}                |    ^      |
{Colors.YELLOW}                \\   '=='    /
{Colors.YELLOW}                 '-.______.-'
{Colors.YELLOW}                      |
{Colors.YELLOW}                      |
{Colors.YELLOW}                      V
{Colors.RESET}
    """
    print(bubble)

def main():
    # Clear screen and set the mood
    print('\033[2J\033[H')  # Clear and move cursor to top
    
    # Print title with anxiety-inducing flashing
    print(f"\n{Colors.BOLD}{Colors.RED}")
    print("╔══════════════════════════════════════╗")
    print("║                                      ║")
    print("║   EXISTENTIAL CRISIS GENERATOR       ║")
    print("║        (Powered by Anxiety)          ║")
    print("║                                      ║")
    print("╚══════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
    # Show the therapy couch
    print_therapy_couch()
    
    # Display a thought bubble
    print_thought_bubble()
    
    # The main philosophical quote (Woody Allen style)
    quote = "I'm not afraid of death; I'm afraid of arriving at the pearly gates and having them say, 'Sorry, we booked the wrong Woody Allen.'"
    
    # Type it out nervously with blinking cursor effect
    print(f"{Colors.BOLD}{Colors.CYAN}")
    typewriter("Doctor, I have this terrible fear that...", 0.08)
    time.sleep(0.5)
    
    # Blinking cursor while building tension
    for _ in range(3):
        sys.stdout.write(f"{Colors.RED}_")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\b ")
        sys.stdout.flush()
        time.sleep(0.3)
    
    print(f"\n\n{Colors.BOLD}{Colors.MAGENTA}My philosophical insight:{Colors.RESET}\n")
    time.sleep(0.5)
    
    # Typewriter effect for the quote with emphasis on key words
    words = quote.split()
    for i, word in enumerate(words):
        if word.lower() in ['afraid', 'death', 'wrong']:
            typewriter(word + " ", 0.05, Colors.RED + Colors.BOLD)
        elif word.lower() in ['woody', 'allen']:
            typewriter(word + " ", 0.05, Colors.YELLOW + Colors.BOLD)
        else:
            typewriter(word + " ", 0.05, Colors.WHITE)
        time.sleep(0.02)
    
    print(f"\n{Colors.DIM}")
    typewriter("-- Woody Allen, probably during therapy", 0.04, Colors.CYAN)
    print(f"{Colors.RESET}")
    
    # Add some neurotic footnotes
    print(f"\n{Colors.GREEN}{Colors.ITALIC}")
    typewriter("Footnotes:", 0.06)
    typewriter("• This quote is covered by my existential insurance policy", 0.04)
    typewriter("• Results may vary based on day of the week", 0.04)
    typewriter("• I'm sorry if this upsets you. I'm mostly upset myself.", 0.04)
    print(f"{Colors.RESET}")
    
    # Final ASCII art signature
    print(f"\n{Colors.BLUE}")
    typewriter("     ___", 0.03)
    typewriter("    (o o)", 0.03)
    typewriter("   (  V  )  Woody Allen", 0.03)
    typewriter("   --'-'--", 0.03)
    print(f"{Colors.RESET}")

if __name__ == "__main__":
    main()