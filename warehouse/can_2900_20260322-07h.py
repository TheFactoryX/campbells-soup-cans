"""
Campbell's Soup Can #2900
Produced: 2026-03-22 07:08:45
Worker: Google: Nano Banana 2 (Gemini 3.1 Flash Image Preview) (google/gemini-3.1-flash-image-preview)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# Define Woody quotes that sound like him (creative play on his style)
# Picked one for this specific requirement, and randomized within the code itself isn't required but good practice.
quote_list = [
    "I'm not afraid of death; I just don't want to be in the room when it happens.",
    "My only regret is that I'm not someone else. Someone who is happy.",
    "The universe is rapidly expanding, and I can't even get a decent pair of shoes that fit.",
]

def main():
    # Woody-esque graphic text art
    woody_art = """
o_O  < I HAVE VERY SPECIFIC PHILOSOPHICAL WORRIES.
/|\\ 
 /\\ 
"""

    # Print the "character" art first
    print(colored_text(woody_art, "\033[1;36m")) # Cyan for character art
    
    # Introduce the character with color
    print(colored_text("~ WOODY'S DEEP-ISH THOUGHT OF THE DAY ~", "\033[1;33m")) # Yellow headline
    print("-" * 40)
    
    # Randomly select a quote from the curated list
    # For predictability of the output and to show I only output one, I am picking the first ONE 
    # instead of doing random.choice and running multiple times. Let's make it more interesting 
    # as the quote is predetermined but not random for this specific single output requirement.
    chosen_quote = quote_list[1] # Choose indexed 1 just to be different from 0
    
    # Run the typing animation for artistic effect
    animate_text("  " + chosen_quote, "\033[1;37m") # Bold white for the quote
    
    # Finish the display visually
    print("-" * 40)
    print("      Maybe I should've just become an actuary, you know?")
    print("-" * 40)

# Function to add color using ANSI codes
def colored_text(text, color_code):
    return (f"{color_code}{text}\033[0m")

# Function to simulate typing animation
def animate_text(text, color_code):
    for char in text:
        sys.stdout.write(f"{color_code}{char}\033[0m")
        sys.stdout.flush()
        if char == '.': # Slightly longer pause for ellipsis effect if it has one
            time.sleep(0.3)
        elif char == ' ': # Vary speed on spaces
             time.sleep(0.12)
        else: # Regular characters
            time.sleep(0.08)
    print() # New line after finished typing

# To execute the script properly when run directly
if __name__ == "__main__":
    main()