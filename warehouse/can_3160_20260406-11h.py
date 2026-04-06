"""
Campbell's Soup Can #3160
Produced: 2026-04-06 11:13:07
Worker: Qwen: Qwen3.6 Plus (free) (qwen/qwen3.6-plus:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random
import textwrap

class Terminal:
    """ANSI color & formatting helper"""
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    YELLOW  = "\033[33m"
    CYAN    = "\033[36m"
    MAGENTA = "\033[35m"
    GRAY    = "\033[90m"
    RED     = "\033[31m"
    
    @staticmethod
    def clear():
        print("\033[H\033[J", end="")

    @staticmethod
    def type_char(char, delay=0.03, color=YELLOW):
        sys.stdout.write(f"{color}{char}{Terminal.RESET}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(0.01, 0.04))

QUOTE = (
    "The universe is an absurd, indifferent void hurtling toward heat death, "
    "which is deeply unsettling, mostly because I still have three unread emails "
    "and I haven't even decided what to wear to my own existential crisis."
)

def loading_sequence():
    frames = ["(◔_◔)", "(◑_◑)", "(◕_◕)", "(◔_◔)"]
    for i in range(14):
        sys.stdout.write(f"\r{Terminal.MAGENTA}  Calibrating existential dread... {frames[i % 4]} {i * 8}%{Terminal.RESET}")
        sys.stdout.flush()
        time.sleep(0.18)
    print(f"\r{Terminal.GRAY}  ✓ Anxiety fully loaded.                        {Terminal.RESET}\n")

def main():
    Terminal.clear()
    
    # Header
    print(f"\n{Terminal.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║                                                  ║")
    print(f"║        {Terminal.BOLD}♪  A Neurotic Observation on Being  ♪        {Terminal.CYAN}║")
    print(f"║                                                  ║")
    print(f"╚══════════════════════════════════════════════════════════╝{Terminal.RESET}\n")
    
    time.sleep(0.4)
    loading_sequence()
    time.sleep(0.3)
    
    # Box & Typewriter Quote
    width = 54
    wrapped = textwrap.wrap(QUOTE, width=width)
    
    print(f"{Terminal.GRAY}  ┌{'─' * (width + 2)}┐")
    
    for line in wrapped:
        sys.stdout.write(f"  {Terminal.CYAN}│{Terminal.RESET} ")
        sys.stdout.flush()
        time.sleep(0.1)
        
        # Typewriter each character with neurotic timing
        for char in line:
            Terminal.type_char(char, color=Terminal.YELLOW)
            
        # Right padding
        padding = width - len(line)
        sys.stdout.write(f"{' ' * padding} {Terminal.CYAN}│{Terminal.RESET}")
        sys.stdout.write("\n")
        sys.stdout.flush()
        
    print(f"  └{'─' * (width + 2)}┘{Terminal.RESET}\n")
    
    # Footer
    time.sleep(0.5)
    print(f"   {Terminal.BOLD}{Terminal.RED}─ Woody Allen{Terminal.RESET}")
    print(f"   {Terminal.GRAY}(He'd also ask for a refund on consciousness, but keep the receipts.){Terminal.RESET}")
    
    # Graceful exit pause
    time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Exit cleanly on Ctrl+C
        print(f"\n{Terminal.GRAY}...and the screen goes dark. Much like my therapy bills.{Terminal.RESET}")
        sys.exit(0)