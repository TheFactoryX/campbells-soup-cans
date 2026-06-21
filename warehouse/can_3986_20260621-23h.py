"""
Campbell's Soup Can #3986
Produced: 2026-06-21 23:44:54
Worker: Google: Gemini 2.5 Flash Lite Preview 09-2025 (google/gemini-2.5-flash-lite-preview-09-2025)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# --- ANSI Color Codes ---
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"
BLINK = "\033[5m"

# --- The Quote ---
WOODY_QUOTE = (
    "Existence is this terrifying, absurd carnival, and all I really want "
    "is a quiet corner table, a decent pastrami sandwich, and confirmation "
    "that the woman pouring my coffee actually likes me."
)

# --- Visual Effects ---

def typewriter_print(text, delay=0.04, color=WHITE):
    """Prints text character by character with a slight delay."""
    for char in text:
        print(color + char + RESET, end="", flush=True)
        time.sleep(delay)
    print()

def draw_neurotic_box(text, width=80):
    """Draws a decorative, slightly unbalanced box around the text."""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines) if lines else 0
    
    # Calculate padding for a slightly off-center look
    padding_outer = (width - max_len - 4) // 4
    line_width = width - 2 - 2 * padding_outer
    
    top_bottom = BOLD + CYAN + "╔" + "═" * (line_width) + "╗" + RESET
    
    print("\n" * 2)
    print(" " * padding_outer + top_bottom)
    
    # Print the content lines
    for line in lines:
        # Center the actual quote content within the box's inner width
        content_len = len(line)
        space_needed = line_width - content_len - 2 # Account for side borders
        padding_inner = " " * (space_needed // 2)
        
        print(" " * padding_outer + CYAN + "║" + WHITE + padding_inner + line + RESET + CYAN + "║" + RESET)

    print(" " * padding_outer + CYAN + "╚" + "═" * (line_width) + "╝" + RESET)
    print("\n" * 2)

def animate_title():
    """Flashes a title to simulate a panic attack/stage fright."""
    title = "A THOUGHT FROM THE COUCH"
    colors = [RED, YELLOW, BLUE, MAGENTA]
    
    for i in range(5):
        color = random.choice(colors)
        print(f"{' ' * 25}{color}{BOLD}{title}{RESET}", end='\r')
        time.sleep(0.1)
        print(f"{' ' * 25}{WHITE}{BLANK}{title}{RESET}", end='\r') # Simulate erasure/blanking
        time.sleep(0.1)
    
    # Final print
    print(f"{' ' * 25}{GREEN}{BOLD}{title}{RESET}")
    time.sleep(0.5)


# --- Main Execution ---

if __name__ == "__main__":
    try:
        # 1. Title Animation
        animate_title()
        
        # 2. Box Drawing and Quote Display
        draw_neurotic_box(WOODY_QUOTE, width=65)
        
        # 3. Print attribution with neurotic flair
        attribution = f"{YELLOW}\n\t\t\t-- Somewhere between Neurosis and the Deli Counter{RESET}"
        typewriter_print(attribution, delay=0.02, color=YELLOW)
        
    except KeyboardInterrupt:
        print(f"\n{RED}Interruption! See? Life is always rushing you.{RESET}")