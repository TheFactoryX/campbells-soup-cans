"""
Campbell's Soup Can #4906
Produced: 2026-09-05 16:05:01
Worker: MiniMax: MiniMax M3 (free) (minimax/minimax-m3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

BG_BLACK = "\033[40m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, color=WHITE, delay=0.03):
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_thinking():
    """Animate a neurotic little brain thinking"""
    frames = ["(o_o)", "(O_O)", "(°_°)", "(•_•)", "(◑_◑)", "(◐_◐)"]
    thoughts = [
        "contemplating mortality...",
        "is this cheese expired?",
        "what if I'm a simulation?",
        "do I exist on Tuesdays?",
        "analyzing my own anxieties...",
        "having another existential crisis..."
    ]
    for i, (frame, thought) in enumerate(zip(frames, thoughts)):
        sys.stdout.write(f"\r{YELLOW}{frame}{RESET} {DIM}{thought}{RESET}   ")
        sys.stdout.flush()
        time.sleep(0.4)
    print()

def draw_box():
    """Draw a fancy ASCII art box"""
    box = f"""
{BLUE}╔══════════════════════════════════════════════════════════════════════════════╗
║{RESET}                                                                              {BLUE}║
║{RESET}    {MAGENTA}✦{RESET}  {ITALIC}"{CYAN}I don't want to achieve immortality through my work...{RESET}  {MAGENTA}✦{RESET}      {BLUE}║
║{RESET}                                                                              {BLUE}║
║{RESET}         {YELLOW}I want to achieve it through {BOLD}{RED}not dying{RESET}{YELLOW}.{RESET}                              {BLUE}║
║{RESET}                                                                              {BLUE}║
║{RESET}    {DIM}...which, given my cholesterol and general paranoia,{RESET}                  {BLUE}║
║{RESET}    {DIM}   is looking like an increasingly ambitious goal.{RESET}                       {BLUE}║
║{RESET}                                                                              {BLUE}║
╚══════════════════════════════════════════════════════════════════════════════╝{RESET}
"""
    return box

def draw_woody():
    """ASCII art Woody Allen"""
    woody = f"""
{YELLOW}        ┌─────────────────────┐
        │  {BOLD}WOODY ALLEN SAYS:{RESET}{YELLOW}  │
        └─────────────────────┘{RESET}
        {RED}   ╭─────╮
      ╭─┤  ● ● ├─╮
      │ │   ▽   │ │
      │ │  ╱│╲  │ │    {CYAN}"I'm a neurotic mess,{RESET}
      ╰─┤  ╱ ╲  ├─╯    {CYAN} but at least{RESET}
        ╰──┬┬──╯       {CYAN} I'm aware of it."{RESET}
           ││
          ╱╱ ╲╲
{RESET}"""
    return woody

def main():
    clear()
    
    # Header with colors
    print(f"{BOLD}{MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{BOLD}{CYAN}   ✦  T H E   N E U R O T I C   P H I L O S O P H E R  ✦{RESET}")
    print(f"{BOLD}{MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}\n")
    
    # Animated thinking brain
    animate_thinking()
    print()
    
    # Show the Woody character
    print(draw_woody())
    print()
    
    # Typewriter effect for the quote setup
    typewriter(f"  {DIM}A thought suddenly struck me...{RESET}", DIM, 0.04)
    time.sleep(0.5)
    print()
    
    # Draw and animate the quote box
    box = draw_box()
    
    # Print the box line by line with a slight delay for effect
    for line in box.split('\n'):
        print(line)
        time.sleep(0.15)
    
    print()
    
    # Footer with blinking dots
    print(f"  {YELLOW}{BOLD}— Anonymous (probably){RESET}")
    print()
    
    # Blinking dots animation
    for _ in range(3):
        for i in range(4):
            dots = "." * i
            sys.stdout.write(f"\r  {MAGENTA}{ITALIC}contemplating the absurdity of existence{dots}   {RESET}")
            sys.stdout.flush()
            time.sleep(0.3)
        print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}Oh great, you interrupted my existential crisis. Thanks.{RESET}")