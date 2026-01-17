"""
Campbell's Soup Can #1670
Produced: 2026-01-17 15:32:18
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody Allen Philosophical Quote Printer
# A single, self-contained, visually entertaining Python script.

import sys
import time
import random

def clear_screen():
    """Clear the terminal screen."""
    # ANSI escape sequence for clear screen and reset cursor
    print("\033[2J\033[H", end="")

def type_text(text, delay=0.03, color_code=""):
    """Typewriter effect with optional color."""
    for char in text:
        sys.stdout.write(f"\033[{color_code}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_woody_ascii():
    """Draw a simple ASCII art representation of Woody Allen (glasses and neurotic vibe)."""
    # Using block characters for a stylized look
    glasses = r"""
         _,.--.
      ,-'      `-.
    ,'            `-.
   (      O       O  )
   |                 |
   (      _     _    )
    `.   \ `---' /  ,'
      `-._`-.___`-.'
          `-----' 
    """
    print("\033[36m" + glasses + "\033[0m")  # Cyan color

def draw_coffin_ascii():
    """Draw a coffin ASCII art for the existential punchline."""
    coffin = r"""
      ___________
     /           \
    |  R.I.P.     |
    |  Reality?   |
    |_____________|
    """
    print("\033[31m" + coffin + "\033[0m")  # Red color

def draw_box(text):
    """Wrap text in a styled ASCII box."""
    width = len(text) + 4
    top = "╔" + "═" * (width - 2) + "╗"
    bottom = "╚" + "═" * (width - 2) + "╝"
    middle = f"║  {text}  ║"
    
    # Colors
    border_color = "\033[33m" # Yellow
    text_color = "\033[37m"   # White
    reset = "\033[0m"
    
    print(f"{border_color}{top}{reset}")
    print(f"{border_color}║{reset}{' ' * (width - 2)}{border_color}║{reset}")
    print(f"{border_color}║{reset} {text_color}{text}{reset} {border_color}║{reset}")
    print(f"{border_color}║{reset}{' ' * (width - 2)}{border_color}║{reset}")
    print(f"{border_color}{bottom}{reset}")

def loading_bar():
    """Simulate a neurotic 'loading' process."""
    print("\n\033[33mAnalyzing existential dread...\033[0m")
    width = 30
    for i in range(width + 1):
        bar = "█" * i + "░" * (width - i)
        percent = int((i / width) * 100)
        sys.stdout.write(f"\r\033[32m[{bar}] {percent}%\033[0m")
        sys.stdout.flush()
        time.sleep(random.uniform(0.02, 0.1))
    print("\n")

def main():
    clear_screen()
    
    # Phase 1: Introduction
    print("\033[1;35m" + "=" * 60 + "\033[0m")
    print("\033[1;35m" + " " * 15 + "WOODY ALLEN QUOTE GENERATOR 3000" + " " * 12 + "\033[0m")
    print("\033[1;35m" + "=" * 60 + "\033[0m")
    
    draw_woody_ascii()
    
    type_text("Initializing neurotic simulation...", 0.05, "36")
    time.sleep(0.5)
    
    loading_bar()
    
    # Phase 2: The Quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    
    print("\033[34m" + "-" * 60 + "\033[0m")
    type_text("\"" + quote + "\"", 0.08, "37")
    print("\033[34m" + "-" * 60 + "\033[0m")
    
    # Phase 3: Visual Punchline
    time.sleep(1)
    print("\n\033[33mProcessing philosophical conclusion...\033[0m")
    time.sleep(1.5)
    
    # Animation of the coffin appearing
    clear_screen()
    draw_box("LOGIC: UNRELIABLE")
    time.sleep(0.5)
    
    print("\n")
    draw_coffin_ascii()
    
    print("\n\033[31m" + " " * 20 + "Reality is a crutch for people who can't handle anxiety.\033[0m")
    
    # Footer
    print("\n\033[2;30mPowered by neurosis and coffee.\033[0m")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[31mProgram interrupted by existential crisis.\033[0m")
        sys.exit(0)