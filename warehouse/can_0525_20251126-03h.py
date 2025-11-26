"""
Campbell's Soup Can #525
Produced: 2025-11-26 03:54:59
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

def woody_allen_quote():
    quote = "I once tried to find meaning in life. It was like trying to find a taxi in the rain during rush hour - expensive, frustrating, and you probably end up somewhere you don't want to be."
    
    # ASCII art elements
    frame_top = "╔══════════════════════════════════════════════════════════════╗"
    frame_bottom = "╚══════════════════════════════════════════════════════════════╝"
    divider = "║                                                          ║"
    inner_width = len(frame_top) - 4  # Calculate inner width for text
    
    # Woody Allen ASCII art
    woody = """
       .-.
      (o o)  Woody Allen
     /  V  \\
    /   |   \\
   (    |    )
    \\   |   /
     \\  |  /
      \\ | /
       \\|/
        """
    
    # Broken heart ASCII art
    broken_heart = """
   .-.   .-.
  (   \\ /   )
   \\   X   /
    \\ / \\ /
     \\   /
      \\ /
    """
    
    # Taxi ASCII art (New York reference)
    taxi = """
      ______
    _/|_||_\\`.__
   (   _    _ _\\"
  =`-(_)--(_)-'
    """
    
    # ANSI color codes
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"
    
    # Helper function to print with delay
    def delay_print(text, delay=0.03):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    # Print title
    delay_print(f"\n{BOLD}{BLUE} Woody Allen on Finding Meaning {END}\n", 0.05)
    
    # Print Woody ASCII art
    delay_print(f"{CYAN}{woody}{END}", 0.02)
    
    # Print broken heart
    delay_print(f"{RED}{broken_heart}{END}", 0.02)
    
    # Print taxi (New York reference)
    delay_print(f"{YELLOW}{taxi}{END}", 0.02)
    
    # Print frame
    delay_print(f"{GREEN}{frame_top}{END}", 0.01)
    delay_print(f"{GREEN}{divider}{END}", 0.01)
    
    # Print quote with typewriter effect, ensuring it fits in frame
    padded_quote = f"  {quote}  "
    # Truncate if necessary to fit in frame
    if len(padded_quote) > inner_width:
        padded_quote = padded_quote[:inner_width]
    else:
        # Center the quote if it's shorter than the frame
        padding = (inner_width - len(padded_quote)) // 2
        padded_quote = " " * padding + padded_quote + " " * padding
    quote_line = f"║{YELLOW}{padded_quote}{GREEN}║"
    delay_print(quote_line, 0.03)
    
    # Print frame bottom
    delay_print(f"{GREEN}{divider}{END}", 0.01)
    delay_print(f"{GREEN}{frame_bottom}{END}", 0.01)
    
    # Add some decorative elements
    delay_print("\n", 0.1)
    
    # Musical notes animation
    notes = ["♪", "♫", "♬", "♩"]
    for i in range(3):
        note_line = " ".join(random.choice(notes) for _ in range(8))
        delay_print(f"{BOLD}{MAGENTA} {note_line} {END}", 0.1)
        time.sleep(0.2)
    
    # Wisdom tag
    delay_print(f"\n{BOLD}{ITALIC} -- existential wisdom -- {END}\n", 0.05)
    
    # Self-deprecating footer
    delay_print(f"{BOLD}{UNDERLINE}{BLUE}  (By someone who's lost more than just his keys){END}\n", 0.05)

if __name__ == "__main__":
    woody_allen_quote()