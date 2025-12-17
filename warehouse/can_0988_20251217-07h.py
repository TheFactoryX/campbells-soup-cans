"""
Campbell's Soup Can #988
Produced: 2025-12-17 07:34:07
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, color_code='\033[0m', delay=0.03):
    for char in text:
        sys.stdout.write(color_code + char + '\033[0m')
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_woody_quote():
    # ANSI color codes
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    END = '\033[0m'
    
    clear_screen()
    
    # Title
    print(BLUE + BOLD + "╔════════════════════════════════════════════════════════════════╗" + END)
    print(BLUE + "║" + END + " " + BOLD + MAGENTA + "                   PHILOSOPHY ACCORDING TO WOODY                " + END + " " + BLUE + "║" + END)
    print(BLUE + "╚════════════════════════════════════════════════════════════════╝" + END)
    print("\n")
    
    # ASCII art frame for the quote
    print(YELLOW + "    ┌─────────────────────────────────────────────────────────┐" + END)
    print(YELLOW + "    │                                                         │" + END)
    
    # Quote with typing animation
    quote = "I've been to therapists, gurus, and even that guy who claims to"
    type_text("    │ " + BOLD + MAGENTA + quote + END + " │", delay=0.02)
    
    quote = "channel spirits from beyond, but I've learned one thing for sure:"
    type_text("    │ " + BOLD + MAGENTA + quote + END + " │", delay=0.02)
    
    quote = "the only thing worse than an existential crisis is being stuck in"
    type_text("    │ " + BOLD + MAGENTA + quote + END + " │", delay=0.02)
    
    quote = "traffic when you're having an existential crisis."
    type_text("    │ " + BOLD + MAGENTA + quote + END + " │", delay=0.02)
    print(YELLOW + "    │                                                         │" + END)
    print(YELLOW + "    └─────────────────────────────────────────────────────────┘" + END)
    print("\n")
    
    # Author attribution
    print(CYAN + BOLD + "                                                    -- Woody Allen" + END)
    print("\n")
    
    # Funny footer with ASCII art
    print(GREEN + "  ☺  " + END + RED + BOLD + "Life's too short for bad traffic and existential dread." + END)
    print("\n")
    print(BLUE + "  (╯°□°)╯︵ ┻━┻   " + END + YELLOW + "But at least the horn works when you're honking at the void." + END)

if __name__ == "__main__":
    print_woody_quote()