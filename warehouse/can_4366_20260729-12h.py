"""
Campbell's Soup Can #4366
Produced: 2026-07-29 12:20:59
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import math

def animate_text(text, delay=0.05, color_code="\033[96m"):
    """Prints text with a typewriter effect and color."""
    for char in text:
        sys.stdout.write(f"{color_code}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(width, height, quote_lines, color="\033[95m"):
    """Renders the quote inside a dynamic, pulsing ASCII box."""
    
    # ANSI Escape Codes
    RESET = "\033[0m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    YELLOW = "\033[93m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    
    # The Neurotic Quote
    quote = [
        "\"I find that my anxiety is a very efficient way",
        "of making sure I never actually enjoy anything,",
        "which is helpful because, frankly, the universe",
        "is a terrifying void of chaos and I'm quite",
        "certain it's looking for me specifically.\""
    ]

    # Animation Loop
    try:
        for frame in range(40):
            # Clear screen (ANSI)
            print("\033[H\033[J", end="")
            
            # Calculate a "pulsing" effect for the border
            pulse = (math.sin(frame * 0.5) + 1) / 2
            border_color = CYAN if pulse > 0.5 else MAGENTA
            
            # Top Border
            print(f"{border_color}{'═' * (width)}")
            
            # Side borders and content
            for i in range(height):
                line = quote[i] if i < len(quote) else ""
                # Center the text
                padding = (width - len(line) - 2) // 2
                if padding < 0: padding = 0
                
                row = "║" + (" " * padding) + line + (" " * (width - len(line) - padding - 2)) + "║"
                print(f"{border_color}{row}")
            
            # Bottom Border
            print(f"{border_color}{'═' * (width)}")
            
            # Neurotic footer
            print(f"\n\n    {YELLOW}— Status: Existentially Dreadful  {RESET}")
            print(f"    {CYAN}— Mood: Overthinking everything... {RESET}")
            
            time.sleep(0.1)
            
        # Final Reveal
        print("\n" + "="*50)
        animate_text("LIFE IS JUST A SERIES OF UNFORTUNATE EVENTS", 0.08, "\033[91m")
        print("="*50)

    except KeyboardInterrupt:
        print("\n\n\033[91m[Disconnected from reality]\033[0m")

if __name__ == "__main__":
    # Dimensions
    WIDTH = 60
    HEIGHT = 6
    
    # Run the art
    draw_frame(WIDTH, HEIGHT)