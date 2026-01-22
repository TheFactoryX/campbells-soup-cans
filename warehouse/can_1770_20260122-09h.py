"""
Campbell's Soup Can #1770
Produced: 2026-01-22 09:47:24
Worker: Qwen: Qwen3 Next 80B A3B Instruct (free) (qwen/qwen3-next-80b-a3b-instruct:free)
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

def typewriter_effect(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

# Woody Allen style quote (original, in his voice)
quote = "I'm not afraid of death—I just don't want to be around when it happens. Like, imagine showing up to the afterlife and realizing they forgot to send the invitation to my therapist. Also, I asked the angel at the gate for a refund on my mortal life. He said, 'Sir, we don't do returns on existential dread.' So now I'm stuck here... with my regrets and a malfunctioning toaster that insists on burning my bagels for 'symbolic reasons.'"

# Create a visually stunning display
def display_woody_quote():
    # ANSI colors
    RED = "31"
    YELLOW = "33"
    BLUE = "34"
    MAGENTA = "35"
    CYAN = "36"
    WHITE = "37"
    BRIGHT_WHITE = "97"
    BOLD = "1"
    
    # ASCII art frame
    border = "╔" + "═" * 60 + "╗"
    sides = "║" + " " * 60 + "║"
    
    print()  # empty line for spacing
    
    # Animated title
    typewriter_effect(color_text("    🎬  W O O D Y   A L L E N   P H I L O S O P H Y   🎬", MAGENTA), 0.05)
    
    print(f"\033[33m{border}\033[0m")
    
    # Randomly color each word
    words = quote.split()
    colored_words = []
    
    color_list = [RED, YELLOW, BLUE, MAGENTA, CYAN, WHITE]
    for word in words:
        # Clean punctuation
        clean_word = word.rstrip('.,!?;:')
        punctuation = word[len(clean_word):] if len(word) > len(clean_word) else ""
        color = random.choice(color_list)
        colored = color_text(clean_word, color)
        colored_words.append(colored + punctuation)
    
    # Rejoin words to form the quote line
    colored_quote = " ".join(colored_words)
    
    # Split quote into lines that fit the box (max ~58 chars per line)
    line = ""
    lines = []
    for word in words:
        clean_word = word.rstrip('.,!?;:')
        punctuation = word[len(clean_word):] if len(word) > len(clean_word) else ""
        test_line = line + (" " if line else "") + clean_word + punctuation
        if len(test_line) <= 58:
            line = test_line
        else:
            lines.append(line)
            line = clean_word + punctuation
    
    if line:
        lines.append(line)
    
    # Print each line centered in box
    for line in lines:
        padded_line = line.center(60)
        print(f"\033[37m║\033[0m{padded_line}\033[37m║\033[0m")
    
    print(f"\033[33m{border}\033[0m")
    
    # Add a trembling glowing effect
    glimmer = "  🌟 " + color_text("This quote was written by a man who fears both death AND double parking.", BRIGHT_WHITE) + " 🌟"
    print(glimmer)
    
    # Slowly blink a lightbulb
    for _ in range(5):
        sys.stdout.write("\r  💡 " + " " * 10)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\r  🚫 " + " " * 10)
        sys.stdout.flush()
        time.sleep(0.3)
    
    print("\n\n")
    typewriter_effect(color_text("   ...and yes, I've already scheduled my funeral. April 1st. Because even in death, I'm not giving them a straight answer.", BLUE), 0.02)
    typewriter_effect(color_text("   Now, if you'll excuse me... I have to go check if my oven is off. Or was I just thinking about it?", YELLOW), 0.03)

# Run the show
if __name__ == "__main__":
    display_woody_quote()