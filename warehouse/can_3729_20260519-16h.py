"""
Campbell's Soup Can #3729
Produced: 2026-05-19 16:30:57
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def woody_quote():
    # ANSI color codes
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    END = '\033[0m'
    
    # Woody Allen ASCII art
    woody = [
        f"{YELLOW}      .--.",
        f"{YELLOW}     |o_o |",
        f"{YELLOW}     |:_/ |",
        f"{YELLOW}    //   \\ \\",
        f"{YELLOW}   (|     | )",
        f"{YELLOW}/'\\_   _/`\\",
        f"{YELLOW}\\___)=(___/{END}"
    ]
    
    # Box decoration
    top = f"{YELLOW}╔═════════════════════════════════════════════════════════════════════════════════════════╗"
    bottom = f"{YELLOW}╚═════════════════════════════════════════════════════════════════════════════════════════╝"
    side = f"{YELLOW}║{END}"
    
    # The quote with color emphasis
    quote = f"""
    {BOLD}{GREEN}"I spent the entire weekend searching for the meaning of life, only to discover
    it was hiding in the back of my refrigerator next to the expired yogurt and
    my hopes for a meaningful relationship. Turns out, life's meaning is just
    whatever you can salvage before it goes bad."{END}
    """
    
    # Footnote
    footnote = f"{ITALIC}{RED}   - Woody Allen (probably) {END}"
    
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print Woody Allen ASCII art
    for line in woody:
        type_text(line, 0.02)
    
    # Print top border
    type_text(top)
    type_text(f"{YELLOW}║{BLUE}" + " " * 100 + f"{YELLOW}║")
    type_text(f"{YELLOW}║{BLUE}" + " " * 100 + f"{YELLOW}║")
    
    # Print quote with typewriter effect
    type_text(f"{YELLOW}║{BLUE}" + " " * 45 + "WOODY ALLEN ON LIFE" + " " * 44 + f"{YELLOW}║")
    type_text(f"{YELLOW}║{BLUE}" + " " * 100 + f"{YELLOW}║")
    type_text(f"{YELLOW}║{BLUE}" + " " * 100 + f"{YELLOW}║")
    type_text(f"{YELLOW}║{BLUE}" + " " * 100 + f"{YELLOW}║")
    
    # Print the quote with color emphasis
    type_text(f"{YELLOW}║{END}", 0.01)
    type_text(f"{BOLD}{GREEN}", 0.01)
    for line in quote.split('\n'):
        type_text(f"{YELLOW}║{BLUE} {line}{YELLOW}║")
    
    # Print footnote
    type_text(f"{YELLOW}║{END}")
    type_text(f"{YELLOW}║{ITALIC}{RED}   " + footnote.lstrip() + " " * (75 - len(footnote)) + f"{YELLOW}║")
    type_text(f"{YELLOW}║{BLUE}" + " " * 100 + f"{YELLOW}║")
    type_text(f"{YELLOW}║{BLUE}" + " " * 100 + f"{YELLOW}║")
    
    # Print bottom border
    type_text(bottom)
    
    # Add some jazz hands at the end
    time.sleep(1)
    print("\n" * 3)
    for _ in range(5):
        print(f"\r{RED}   \\o/   {YELLOW}(contemplating){RED}   \\o/   ", end="", flush=True)
        time.sleep(0.3)
        print(f"\r{RED}   o|o   {YELLOW}(anxiously){RED}   o|o   ", end="", flush=True)
        time.sleep(0.3)

if __name__ == "__main__":
    woody_quote()