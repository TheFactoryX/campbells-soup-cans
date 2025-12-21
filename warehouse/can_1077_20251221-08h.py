"""
Campbell's Soup Can #1077
Produced: 2025-12-21 08:40:10
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
    ▄████████    ▄████████    ▄████████    ▄████████    ▄████████    ▄████████ 
   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ 
   ███    █▀    ███    ███   ███    ███   ███    ███   ███    ███   ███    █▀  
   ███         ▄███▄▄▄▄██▀   ███    ███   ███    ███   ███    ███   ███       
   ███        ▀▀███▀▀▀▀▀   ▀███████████   ███    ███   ███    ███   ███       
   ███    █▄  ▀███████████   ███    ███   ███    ███   ███    ███   ███    █▄  
   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ 
   ▀████████▀    ███    ███   ███    █▀    ████████▀    ████████▀    ████████▀  
                 ███    ███                                                        
"""
import time
import random
import sys

# ANSI Color Codes
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

# Palette (Noir meets Neurosis)
C_BEIGE = "\033[38;5;223m" # The color of stale bagels
C_BLUE  = "\033[38;5;24m"  # The color of NYPD
C_RED   = "\033[38;5;196m" # The color of anxiety
C_GOLD  = "\033[38;5;220m" # The color of empty promises
C_GRAY  = "\033[38;5;240m" # The color of existential dread

def type_effect(text, speed=0.04, color=C_BEIGE):
    """Types out text like a nervous comedian."""
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(speed)
    print()

def slide_in(text, color=C_BLUE):
    """Slides text in from the right."""
    width = 50
    for i in range(width, -1, -1):
        padding = " " * i
        # Clear line
        sys.stdout.write("\r" + " " * (width + len(text) + 5))
        sys.stdout.write(f"\r{padding}{color}{text}{RESET}")
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def main():
    # Clear screen
    print("\033[2J\033[H", end="") 
    
    # 1. The Visual Setup: A lonely stage (ASCII Art)
    # We draw a stage with a microphone
    stage = f"""
    {C_GRAY}____________________________________________________
           |                                                |
           |      {C_RED}MY THERAPIST SAID TO BUILD SOMETHING       {C_GRAY}|
           |      {C_RED}THAT LASTS. SO I BUILT A GUAC RECIPE.      {C_GRAY}|
           |________________________________________________|
    {C_BLUE}__________|________________________________________|__________
    {C_BLUE}          |________________________________________|          
              /                                          \\
             /                                            \\
            /                                              \\
           {C_GOLD}|      (  MY ANXIETY IS AUTO-CORRECTING      )     {C_BLUE}|
           {C_GOLD}|       (   MY SADNESS HAS A SPELLCHECKER   )     {C_BLUE}|
           {C_GOLD}|        (    MY EXISTENCE IS BETA-TESTING  )     {C_BLUE}|
           {C_GOLD}|         (______________________________)      {C_BLUE}|
            \\______________________________________________/
    {RESET}
    """
    
    # Print the stage
    print(stage)
    time.sleep(1)

    # 2. The Monologue (Animated)
    print(f"\n{BOLD}{C_BEIGE}")
    slide_in("The waiter arrives with the bill...")
    time.sleep(0.5)
    
    type_effect("I looked at the bill, and then I looked at my life.", 0.05, C_BEIGE)
    time.sleep(0.3)
    
    print(f"{C_GRAY}...")
    time.sleep(0.8)
    
    type_effect("They were surprisingly similar.", 0.05, C_RED)
    time.sleep(0.5)
    
    print(f"{RESET}{C_GRAY}          (Too expensive, and I'm not sure what I ordered.){RESET}")

    # 3. The Punchline (The ASCII Art Fly)
    # Because life is short, like a fly in soup.
    print(f"\n{C_BLUE}")
    fly = r"""
       _     _     _     
      (w).-.(w)  (o)     
       / ._. \  /|       
      \|  (__)| /        
       '-----' `         
    """
    # Let's animate the fly buzzing around
    positions = ["\033[10;40H", "\033[8;50H", "\033[12;45H", "\033[9;60H", "\033[11;30H"]
    
    for pos in positions:
        # Clear previous position area roughly (lazy clear)
        print("\033[7;30H          \033[8;30H          \033[9;30H          \033[10;30H          \033[11;30H          ", end="")
        print(f"\033[2K{pos}{fly}{RESET}", end="")
        sys.stdout.flush()
        time.sleep(0.15)
        
    # Final clean line
    print("\n\n")
    
    # 4. The Grand Finale Quote (Slow Fade / Typewriter)
    final_quote = '"My brain is the only organ I know that works against me 24/7, and yet I still pay the rent for it."'
    
    # Randomly choose a highlight color for the quote
    highlight = random.choice([C_RED, C_GOLD, C_BEIGE])
    
    # Print borders around quote
    border_len = len(final_quote) + 4
    border = "═" * border_len
    
    print(f"{C_GRAY}┌{border}┐{RESET}")
    print(f"{C_GRAY}│{RESET}  {highlight}", end="")
    
    # Typewriter effect for the final quote
    for char in final_quote:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
        
    print(f"{RESET}  {C_GRAY}│{RESET}")
    print(f"{C_GRAY}└{border}┘{RESET}")

    # 5. The Cursor Blink (Waiting for nothing)
    print(f"\n{C_GRAY}[ Press 'Ctrl+C' to stop worrying about the simulation ]{RESET}")
    try:
        while True:
            sys.stdout.write(f"{C_RED}●{RESET}")
            sys.stdout.flush()
            time.sleep(1)
            sys.stdout.write("\b \b")
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nFine, I'll go exist somewhere else.")
        time.sleep(1)
        print("\033[2J\033[H") # Clean exit

if __name__ == "__main__":
    main()