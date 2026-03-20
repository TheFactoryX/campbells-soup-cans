"""
Campbell's Soup Can #2867
Produced: 2026-03-20 15:02:37
Worker: Qwen: Qwen3 235B A22B Thinking 2507 (qwen/qwen3-235b-a22b-thinking-2507)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
GREEN = "\033[92m"

def psychedelic_text(text, delay=0.03):
    """Type out text with random color changes for each character"""
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    for char in text:
        sys.stdout.write(random.choice(colors) + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)

def draw_box():
    """Create a dynamically drawn box with philosophical quote inside"""
    width = 60
    quote = "I'm not afraid of death; I just don't want to be there when it happens... especially during my afternoon nap."
    neurotic_word = "neurotic"
    quote = "Existence is a cosmic typo, but I'm too " + neurotic_word + " to hit 'undo' before it saves automatically."
    
    # Create the box components
    top_border = "╱" + "╌" * width + "╲"
    bottom_border = "╲" + "╌" * width + "╱"
    empty_line = "║" + " " * width + "║"
    
    # Center the quote and break into two lines
    lines = []
    words = quote.split()
    mid = len(words) // 2
    line1 = " ".join(words[:mid])
    line2 = " ".join(words[mid:])
    lines.append(line1.center(width))
    lines.append(line2.center(width))
    
    # Draw the box with animation
    print(YELLOW + "\n" * 3, end="")
    
    # Top border with ripple effect
    print(" " * 10, end="")
    for char in top_border:
        print(YELLOW + BOLD + char + RESET, end='', flush=True)
        time.sleep(0.05)
    print()
    
    # Empty line above quote
    print(YELLOW + BOLD + " " * 10 + empty_line + RESET)
    
    # Quote lines with typewriter effect and neurotic word in red
    for line in lines:
        print(YELLOW + BOLD + " " * 10 + "║", end='', flush=True)
        time.sleep(0.2)
        
        # Process each character with special coloring for neurotic word
        i = 0
        while i < len(line):
            if line[i:i+len(neurotic_word)] == neurotic_word:
                print(RED + BOLD + ITALIC + neurotic_word + RESET + YELLOW + BOLD, end='', flush=True)
                sys.stdout.flush()
                time.sleep(0.3)
                i += len(neurotic_word)
            else:
                print(CYAN + line[i] + RESET, end='', flush=True)
                sys.stdout.flush()
                time.sleep(0.05)
                i += 1
        print(YELLOW + BOLD + "║" + RESET)
        time.sleep(0.3)
    
    # Empty line below quote
    print(YELLOW + BOLD + " " * 10 + empty_line + RESET)
    
    # Bottom border with heartbeat effect
    print(" " * 10, end="")
    for char in bottom_border:
        print(YELLOW + BOLD + char + RESET, end='', flush=True)
        time.sleep(0.03)
        if char in "\\/":
            time.sleep(0.15)
            print("\b \b" + char, end='', flush=True)
            time.sleep(0.1)
    
    # Add Woody Allen style signature
    time.sleep(0.5)
    print("\n" + " " * 25 + MAGENTA + BOLD + "-- Woody Allen, probably while avoiding eye contact" + RESET)
    print(" " * 28 + ITALIC + "(or so I imagine, from my therapist's waiting room)" + RESET)

def main():
    # Clear screen (works in most terminals)
    print("\033c", end="")
    
    # Display title with glitch effect
    title = "WOODY ALLEN'S EXISTENTIAL DILEMMA OF THE HOUR"
    print("\n" * 5)
    for i, char in enumerate(title):
        color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA])
        print(color + BOLD + char + RESET, end='', flush=True)
        time.sleep(0.05 if char != " " else 0.01)
    time.sleep(1)
    
    # Draw the animated box
    draw_box()
    
    # Add some shaking to simulate nervous energy
    time.sleep(0.5)
    for _ in range(5):
        sys.stdout.write("\033[1D \033[1D")
        time.sleep(0.05)
        sys.stdout.write("  ")
        time.sleep(0.05)
    
    # Final touch: spinning thought bubble
    thought = ["(◐.◑)", "(◑.◐)", "(●.●)", "(◕.◕)"]
    print("\n\n" + " " * 35, end='')
    for _ in range(8):
        for face in thought:
            sys.stdout.write("\r" + " " * 35 + CYAN + face + RESET)
            sys.stdout.flush()
            time.sleep(0.1)

if __name__ == "__main__":
    main()