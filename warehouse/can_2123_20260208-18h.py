"""
Campbell's Soup Can #2123
Produced: 2026-02-08 18:55:38
Worker: Pony Alpha (openrouter/pony-alpha)
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

def animate_woody():
    # ANSI color codes
    RESET = "\033[0m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    DIM = "\033[2m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    
    # The quote
    quote = "The universe is merely a fleeting cosmic accident, which wouldn't be so bad if it hadn't happened to me personally."
    
    # ASCII art frame with Woody's glasses
    frame_top = f"""
{DIM}╔══════════════════════════════════════════════════════════════════════════════╗
║{RESET}  {CYAN}   ╭──╮{RESET}                                                        {DIM}║
║{RESET}  {CYAN}   │  │{RESET}   {BOLD}{YELLOW}WOODY ALLEN'S EXISTENTIAL THOUGHT{RESET}                {DIM}║
║{RESET}  {CYAN}   ○  ○{RESET}  (thinking since 1935)                              {DIM}║
╚══════════════════════════════════════════════════════════════════════════════╝{RESET}
"""
    print(frame_top)
    time.sleep(0.5)
    
    # Dramatic intro with loading dots
    print(f"\n{DIM}Pondering existence", end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(f"{MAGENTA}.{RESET}", end="", flush=True)
    print(f" {GREEN}✓{RESET}\n")
    time.sleep(0.3)
    
    # Quote box
    print(f"{ITALIC}{MAGENTA}┌─────────────────────────────────────────────────────────────────────────────┐{RESET}")
    print(f"{ITALIC}{MAGENTA}│{RESET}                                                                             {MAGENTA}│{RESET}")
    print(f"{ITALIC}{MAGENTA}│{RESET}  ", end="", flush=True)
    
    # Typewriter effect with random color variations for emphasis
    emphasis_words = ["universe", "accident", "me", "personally"]
    
    for char in quote:
        if char == " ":
            # Check if next word is emphasis word
            remaining = quote[quote.index(char, quote.find(char)):] if char in quote else ""
            sys.stdout.write(char)
        else:
            # Random slight color for neurotic effect
            if random.random() < 0.03:
                sys.stdout.write(f"{RED}{char}{RESET}")
            else:
                sys.stdout.write(f"{BOLD}{YELLOW}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(0.02)
    
    print(f"  {ITALIC}{MAGENTA}│{RESET}")
    print(f"{ITALIC}{MAGENTA}│{RESET}                                                                             {MAGENTA}│{RESET}")
    print(f"{ITALIC}{MAGENTA}│{RESET}                         {DIM}— Woody Allen (probably){RESET}                  {MAGENTA}│{RESET}")
    print(f"{ITALIC}{MAGENTA}│{RESET}                                                                             {MAGENTA}│{RESET}")
    print(f"{ITALIC}{MAGENTA}└─────────────────────────────────────────────────────────────────────────────┘{RESET}")
    
    # Neurotic footer animation
    time.sleep(0.5)
    footers = [
        f"\n{DIM}[ ]{RESET} Not therapeutic advice",
        f"{DIM}[ ]{RESET} May increase existential dread",
        f"{DIM}[ ]{RESET} Laughter is a coping mechanism"
    ]
    
    print()
    for footer in footers:
        print(footer)
        time.sleep(0.3)
    
    # Final blink
    print(f"\n{CYAN}▓▓▓{RESET} {ITALIC}Keep worrying, it hasn't killed you yet.{RESET} {CYAN}▓▓▓{RESET}\n")

if __name__ == "__main__":
    animate_woody()