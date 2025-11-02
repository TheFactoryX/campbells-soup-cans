"""
Campbell's Soup Can #9
Produced: 2025-11-02 15:28:29
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI escape codes for colors
RED = "\033[38;5;196m"
YELLOW = "\033[38;5;220m"
ORANGE = "\033[38;5;208m"
RESET = "\033[0m"

# The existential quote
quote = [
    "The universe is basically an unsupervised daycare center",
    "run by toddlers with scissors.",
    "But oh, how they make us pay for the extra nap time."
]

# Coffee cup ASCII art
def print_coffee():
    print(f"""{ORANGE}
      )  (
     (   ) )
      ) ( (
    _______)_
 .-'---------|  
( C|/{RED}☕{ORANGE}\/☕{RED}☕{ORANGE}\ |{RESET}
 '-./\___/ \_.'
    '-----'{RESET}
""")

# Typewriter effect with anxiety delays
def neurotic_typewriter(text, color=YELLOW):
    print(color, end='')
    for i, char in enumerate(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        
        # Variable anxiety-based typing speed
        delay = 0.04
        
        # Extra hesitation before big words
        if char.isspace() and len(text.split()) > i//3:
            delay *= 3
            
        # Panic when mentioning the universe
        if text[0:15] == "The universe" and i > 15:
            delay *= 1.7
            
        time.sleep(delay)
    print(RESET, end='')

# Main program
def main():
    # Clears screen
    print("\033c", end='')
    
    # Print nervous coffee cup
    print_coffee()
    
    # Quote in an "anxious" box
    box_width = 58
    
    print(f"{RED}┏{' ' * box_width}┓{RESET}")
    
    for idx, line in enumerate(quote):
        padding = (box_width - len(line)) // 2
        print(f"{RED}┃{' ' * padding}", end='')
        neurotic_typewriter(line)
        print(f"{' ' * (box_width - len(line) - padding)}┃{RESET}")
        
        # Fidgety pause between lines
        time.sleep(0.3 + 0.1 * (1 + idx**2))
    
    # Woody's signature (disclaimer)
    print(f"{RED}┃{'Eternity is overrated - Woody Allen? Maybe?'.rjust(box_width)}┃{RESET}")
    print(f"{RED}┗{' ' * box_width}┛{RESET}")
    
    # Nervous blink before exit
    time.sleep(2)
    print("\n(Program nervously exits before you can ask about existential dread)")

if __name__ == "__main__":
    main()