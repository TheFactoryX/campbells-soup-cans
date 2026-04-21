"""
Campbell's Soup Can #3386
Produced: 2026-04-21 11:32:52
Worker: Anthropic: Claude Opus 4.5 (anthropic/claude-opus-4.5)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI escape codes for colors and styles
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
RED = "\033[91m"
GREEN = "\033[92m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.03, color=""):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)

def animate_thinking():
    frames = ["🤔", "😰", "😓", "🥴", "😵‍💫"]
    for _ in range(2):
        for frame in frames:
            sys.stdout.write(f"\r  {frame} Neurotic contemplation in progress... ")
            sys.stdout.flush()
            time.sleep(0.3)
    print("\n")

def draw_woody():
    woody = f"""
{DIM}{YELLOW}
              .-'''-.
             /        \\
            |  O    O  |
            |    __    |
             \\  \\__/  /
           ___`------'___
          /   \\______/   \\
         |  ANXIETY  |   |
          \\_________/    |
            |glasses|----'
{RESET}"""
    print(woody)

def main():
    clear_screen()
    
    # Header with animation
    print(f"\n{MAGENTA}{'═' * 60}{RESET}")
    time.sleep(0.2)
    
    title = "  🎬  WOODY ALLEN'S NEUROTIC WISDOM  🎬  "
    print(f"{BOLD}{YELLOW}{title.center(60)}{RESET}")
    print(f"{MAGENTA}{'═' * 60}{RESET}\n")
    time.sleep(0.5)
    
    # Draw Woody
    draw_woody()
    
    # Thinking animation
    animate_thinking()
    
    # The quote
    quote = "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown."
    
    # Fancy quote box
    box_width = 56
    print(f"{CYAN}  ╔{'═' * box_width}╗{RESET}")
    print(f"{CYAN}  ║{' ' * box_width}║{RESET}")
    
    # Print quote with typewriter effect inside box
    print(f"{CYAN}  ║  {RESET}", end="")
    
    words = quote.split()
    line = ""
    lines = []
    for word in words:
        if len(line) + len(word) + 1 <= box_width - 4:
            line += word + " "
        else:
            lines.append(line.strip())
            line = word + " "
    if line:
        lines.append(line.strip())
    
    for i, line_text in enumerate(lines):
        if i > 0:
            print(f"{CYAN}  ║  {RESET}", end="")
        typewriter(f"{ITALIC}{WHITE}{line_text}", 0.02)
        padding = box_width - len(line_text) - 4
        print(f"{' ' * padding}  {CYAN}║{RESET}")
    
    print(f"{CYAN}  ║{' ' * box_width}║{RESET}")
    
    # Attribution with style
    attribution = "— Woody Allen"
    attr_padding = box_width - len(attribution) - 2
    print(f"{CYAN}  ║{' ' * attr_padding}{RED}{BOLD}{attribution}  {CYAN}║{RESET}")
    
    print(f"{CYAN}  ║{' ' * box_width}║{RESET}")
    print(f"{CYAN}  ╚{'═' * box_width}╝{RESET}")
    
    # Animated existential crisis meter
    print(f"\n{DIM}  Existential Crisis Level:{RESET}")
    print(f"  {GREEN}[", end="")
    for i in range(20):
        time.sleep(0.05)
        if i < 5:
            print(f"{GREEN}█", end="")
        elif i < 12:
            print(f"{YELLOW}█", end="")
        else:
            print(f"{RED}█", end="")
        sys.stdout.flush()
    print(f"{RED}] {BOLD}MAXIMUM{RESET}")
    
    # Footer
    print(f"\n{DIM}{MAGENTA}  {'~' * 56}{RESET}")
    print(f"{DIM}  \"In my next life I want to live backwards...\" 🎭{RESET}")
    print(f"{DIM}{MAGENTA}  {'~' * 56}{RESET}\n")

if __name__ == "__main__":
    main()