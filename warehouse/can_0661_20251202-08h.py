"""
Campbell's Soup Can #661
Produced: 2025-12-02 08:46:02
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def woody_quote():
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
    # ASCII art frame
    frame_top = BOLD + BLUE + "╔══════════════════════════════════════════════════════════════════════════════════╗" + END
    frame_bottom = BOLD + BLUE + "╚══════════════════════════════════════════════════════════════════════════════════╝" + END
    frame_side = BOLD + BLUE + "║" + END
    woody_face = YELLOW + " ( -__-) " + END
    
    # Quote parts with different colors
    quote = [
        frame_top,
        frame_side + " " + WHITE + BOLD + "WOODY ALLEN on EXISTENTIAL ANXIETY" + END + " " + frame_side,
        frame_side + " " + END + " " + frame_side,
        frame_side + " " + RED + "I've spent my entire life worrying about the meaning of existence," + END + " " + frame_side,
        frame_side + " " + MAGENTA + "only to realize that the universe doesn't care if I'm neurotic or not -" + END + " " + frame_side,
        frame_side + " " + CYAN + "it's just going to keep expanding whether I'm having a panic attack or not." + END + " " + frame_side,
        frame_side + " " + GREEN + "You know, for a while there, I thought about becoming an optimist," + END + " " + frame_side,
        frame_side + " " + YELLOW + "but then I remembered I have dental insurance." + END + " " + frame_side,
        frame_side + " " + END + " " + frame_side,
        frame_side + " " + ITALIC + WHITE + "             - Woody Allen (probably)" + END + " " + frame_side,
        frame_side + " " + woody_face + " " + frame_side,
        frame_bottom
    ]
    
    # Print with animation
    for line in quote:
        print(line)
        time.sleep(0.1)
    
    # Blinking effect for the punchline
    for _ in range(3):
        sys.stdout.write("\033[F")  # Move cursor up
        sys.stdout.write("\033[K")  # Clear line
        print(frame_side + " " + YELLOW + "but then I remembered I have dental insurance." + END + " " + frame_side)
        sys.stdout.flush()
        time.sleep(0.5)
        
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        print(frame_side + " " + WHITE + "but then I remembered I have dental insurance." + END + " " + frame_side)
        sys.stdout.flush()
        time.sleep(0.5)

if __name__ == "__main__":
    clear_screen()
    woody_quote()
    
    # Add a little extra neurotic touch
    print("\n" + BOLD + WHITE + "P.S. I'm already worried that you didn't find this funny enough." + END)
    time.sleep(1)
    print(BOLD + WHITE + "P.P.S. What if I told you this was my second favorite joke?" + END)
    time.sleep(1)
    print(BOLD + WHITE + "P.P.P.S. I think I'm going to lie down now." + END)