"""
Campbell's Soup Can #3596
Produced: 2026-05-07 17:58:00
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

def type_text(text, delay=0.03, color_code='\033[0m'):
    for char in text:
        sys.stdout.write(f"{color_code}{char}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\033[0m\n')
    sys.stdout.flush()

def woody_allen_quote():
    # ANSI color codes
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    RESET = '\033[0m'
    
    clear_screen()
    
    # Title with ASCII art
    print(f"{BOLD}{CYAN}")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║              WOODY ALLEN'S PHILOSOPHICAL CORNER              ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print(RESET)
    
    time.sleep(1)
    
    # Quote box with border
    print(f"{BOLD}{YELLOW}")
    print("┌──────────────────────────────────────────────────────────────┐")
    print("│                                                              │")
    type_text("│", 0.01)
    type_text(" ", 0.01)
    type_text(f"{ITALIC}{PURPLE}I spent years in therapy, getting to know myself intimately. ", 0.02)
    type_text("Now I", 0.02)
    type_text(f" {GREEN}can't", 0.02)
    type_text(" stand the person I've become. ", 0.02)
    type_text(f"{YELLOW}", 0.02)
    type_text("It's like", 0.02)
    type_text(f" {ITALIC}", 0.02)
    type_text("attending your own funeral as", 0.02)
    type_text(f" {RED}the eulogist", 0.02)
    type_text(f"{YELLOW} who", 0.02)
    type_text(" didn't", 0.02)
    type_text(" write", 0.02)
    type_text(" the speech. ", 0.02)
    type_text("Life", 0.02)
    type_text(f" is", 0.02)
    type_text(f" {ITALIC}", 0.02)
    type_text("a", 0.02)
    type_text(f" {BLUE}tragic", 0.02)
    type_text(f" {ITALIC}", 0.02)
    type_text("comedy", 0.02)
    type_text(f" {YELLOW} where", 0.02)
    type_text(" I'm", 0.02)
    type_text(" the", 0.02)
    type_text(f" {RED}butt", 0.02)
    type_text(f" {YELLOW} of", 0.02)
    type_text(" every", 0.02)
    type_text(" joke", 0.02)
    type_text(".", 0.02)
    type_text(f"{YELLOW}", 0.02)
    type_text(" │", 0.01)
    print("│                                                              │")
    print("└──────────────────────────────────────────────────────────────┘")
    print(RESET)
    
    time.sleep(2)
    
    # Woody Allen signature with typewriter effect
    print(f"{BOLD}{GREEN} Woody Allen".center(60))
    print(RESET)
    
    # Small philosophical musing at the bottom
    print(f"{ITALIC}{CYAN}")
    type_text("     ... contemplating the existential void while eating a pastrami sandwich ...\n", 0.02)
    print(RESET)

if __name__ == "__main__":
    woody_allen_quote()