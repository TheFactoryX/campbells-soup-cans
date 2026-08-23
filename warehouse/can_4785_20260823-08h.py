"""
Campbell's Soup Can #4785
Produced: 2026-08-23 08:48:28
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# woody_allen_quotes.py

import sys
import time

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

    # ASCII art frame
    frame = f"""
{CYAN}╔══════════════════════════════════════════════════════════╗
║  {MAGENTA}██╗  ██╗██╗██╗   ██╗ █████╗ {YELLOW}██╗   ██╗{CYAN}██╗   ██╗{MAGENTA}██╗  ██╗██╗   ██╗██╗███╗   ██╗{CYAN}
║  ██║ ██╔╝██║██║   ██║██╔══██╗{YELLOW}██║   ██║{CYAN}██║   ██║{MAGENTA}██║ ██╔╝██║   ██║██║████╗  ██║{CYAN}
║  █████╔╝ ██║██║   ██║███████║{YELLOW}██║   ██║{CYAN}██║   ██║{MAGENTA}████╔╝ ██║   ██║██║██╔██╗ ██║{CYAN}
║  ██╔═██╗ ██║╚██████╔╝██╔══██║{YELLOW}██║   ██║{CYAN}██║   ██║{MAGENTA}██╔═██╗ ██║   ██║██║██║╚██╗██║{CYAN}
║  ██║  ██╗██║ ╚═════╝ ██║  ██║{YELLOW}╚██████╔╝{CYAN}╚██████╔╝{MAGENTA}██║  ██╗╚██████╔╝██║██║ ╚████║{CYAN}
║  ╚═╝  ╚═╝╚═╝         ╚═╝  ╚═╝{YELLOW} ╚═════╝ {CYAN} ╚═════╝ {MAGENTA}╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝{CYAN}
║                                                          ║
║  {BOLD}{GREEN}"I told my wife she was drawing her eyebrows too high.{RESET}
║  {GREEN}She looked surprised."{CYAN}                                      ║
║                                                          ║
║  {YELLOW}{BOLD}On Existential Dread & Relationship Problems{RESET}{CYAN}        ║
║                                                          ║
║  {RED}{BOLD}The universe is vast, indifferent, and probably{RESET}
║  {RED}{BOLD}doesn't give a damn about my neuroses. But at{RESET}
║  {RED}{BOLD}least my neuroses are consistent.{RESET}{CYAN}                ║
║                                                          ║
║  {MAGENTA}───────────────────────────────────────────────────{RESET}
║  {WHITE}{BOLD}"I'm not paranoid, I just have excellent reasons{RESET}
║  {WHITE}{BOLD}to be anxious about everything, including this{RESET}
║  {WHITE}{BOLD}very anxiety.{RESET}{CYAN}                                    ║
║                                                          ║
║  {BLUE}{BOLD}"Life is full of suffering and disappointment.{RESET}
║  {BLUE}{BOLD}And then you die. But hey, at least the{RESET}
║  {BLUE}{BOLD}disappointment is consistent.{RESET}{CYAN}                          ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝{RESET}
"""
    
    print()
    slow_print(frame)
    
    quote = f"""
    {BOLD}{YELLOW}╔════════════════════════════════════════════════════╗
    ║  {MAGENTA}"I'm not afraid of death; I just don't want to{RESET}
    {BOLD}{MAGENTA}    be there when it happens, especially since{RESET}
    {BOLD}{MAGENTA}    I haven't finished worrying about everything{RESET}
    {BOLD}{MAGENTA}    I've been putting off worrying about."{RESET}{YELLOW}        ║
    ╚════════════════════════════════════════════════════╝{RESET}
    """
    
    print()
    slow_print(quote)
    
    # Animated ending
    dots = "..."
    for i in range(3):
        sys.stdout.write(f"\r{YELLOW}{BOLD}Existential crisis loading{dots[:i+1]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.5)
    
    final = f"\n\n{GREEN}{BOLD}Philosophy Complete™ - No Actual Wisdom Imparted{RESET}\n"
    slow_print(final, 0.05)

if __name__ == "__main__":
    main()