"""
Campbell's Soup Can #2022
Produced: 2026-02-03 18:07:33
Worker: Z.AI: GLM 4.7 (z-ai/glm-4.7)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random
import os

# ANSI Escape Codes for Colors and Styles
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
ITALIC = '\033[3m'
BLINK = '\033[5m'

# Palette: Woody Allen Vibes (Black, White, Nervous Red, Intellectual Blue)
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
BG_BLACK = '\033[40m'

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_out(text, base_color=WHITE, neurotic_level=0.05):
    """
    Simulates typing with neurotic hesitations, stutters, and anxiety.
    """
    for char in text:
        sys.stdout.write(base_color + char + RESET)
        sys.stdout.flush()
        
        # Base typing speed
        delay = random.uniform(0.01, 0.05)
        
        # Neurosis logic
        if char in ['.', ',', ';', '-']:
            # Pause for existential dread
            time.sleep(random.uniform(0.2, 0.5))
        elif char in [' ', 'I']:
            # Occasional stutter or deep breath
            if random.random() < neurotic_level:
                time.sleep(random.uniform(0.1, 0.2))
        else:
            time.sleep(delay)

def draw_glasses():
    """Draws a pair of thick-rimmed glasses in ASCII."""
    print(f"\n    {CYAN}.-----.       .-----.{RESET}")
    print(f"   {CYAN}/       \___/       \\{RESET}")
    print(f"  {CYAN}(                     ){RESET}")
    print(f"   {CYAN}\\                   /{RESET}")
    print(f"    {CYAN}'---_       _---'{RESET}")
    print(f"          |       |")
    print(f"          |_______|")

def draw_anxious_box(width, height):
    """Draws a jagged, nervous border."""
    top_bottom = RED + "╔" + "═" * (width - 2) + "╗" + RESET
    sides = RED + "║" + RESET
    
    # Top
    print(top_bottom)
    
    # Middle (Empty space for now)
    for _ in range(height):
        print(f"{sides{' ' * (width - 2)}{sides}")
        
    # Bottom
    print(RED + "╚" + "═" * (width - 2) + "╝" + RESET)

def center_text(text, width):
    """Centers text within a specific width."""
    return text.center(width)

def heart_rate_monitor():
    """Simulates a frantic heart rate line at the bottom."""
    line = ""
    for _ in range(40):
        height = random.randint(0, 2)
        if height == 0:
            line += "_"
        elif height == 1:
            line += "/"
        else:
            line += "\\"
    return RED + line + RESET

def main():
    clear_screen()
    
    # Configuration
    box_width = 70
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens. "
        "Especially if I'm wearing these pants."
    )
    author = "- Woody Allen (Probably)"
    
    # Visual Intro
    print(BLACK + BG_BLACK + "\n\n") # Set background mood
    
    # Draw ASCII Glasses
    print(center_text("THE NEUROTIC PHILOSOPHER", box_width + 4))
    draw_glasses()
    print()
    
    # The Quote Container
    # We simulate the box drawing by printing lines manually to control where text goes
    
    # Top border
    print(f"  {RED}╔{'═' * box_width}╗{RESET}")
    
    # Empty line
    print(f"  {RED}║{' ' * box_width}║{RESET}")
    
    # The Quote Line 1 (Wrapped simply for demo)
    # A simple wrap logic for visual balance
    words = quote.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line + word) < box_width - 4:
            current_line += word + " "
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)
    
    # Print lines with animation
    for line in lines:
        # Left side of box
        sys.stdout.write(f"  {RED}║ {RESET}")
        # Animated text
        type_out(line.ljust(box_width - 4), WHITE)
        # Right side of box
        print(f"{RED} ║{RESET}")

    # Empty line
    print(f"  {RED}║{' ' * box_width}║{RESET}")
    
    # Author
    author_text = ITALIC + DIM + author + RESET
    print(f"  {RED}║{center_text(author_text, box_width)}{RED}║{RESET}")
    
    # Empty line
    print(f"  {RED}║{' ' * box_width}║{RESET}")
    
    # Bottom border
    print(f"  {RED}╚{'═' * box_width}╝{RESET}")
    
    # Frantic Heart Rate Animation
    print(f"\n   {BOLD}ANXIETY LEVEL:{RESET}")
    for _ in range(5):
        print(f"   {heart_rate_monitor()}")
        sys.stdout.write("\033[F") # Move cursor up one line
        time.sleep(0.1)
        
    # Final static pulse
    print(f"   {heart_rate_monitor()}")
    
    # Final existential sigh
    print(f"\n   {CYAN}*sigh*{RESET}")
    print(BLACK + BG_BLACK + RESET) # Reset colors

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("The angst was too much. Goodbye.")