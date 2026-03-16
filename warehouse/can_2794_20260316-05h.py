"""
Campbell's Soup Can #2794
Produced: 2026-03-16 05:57:32
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random
import os

# Clear screen and hide cursor for cleaner animation
def init_screen():
    sys.stdout.write("\033[2J\033[?25l")
    sys.stdout.flush()

# Show cursor when done
def restore_screen():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

# ANSI color codes
class Colors:
    NEUROTIC = "\033[38;5;208m"    # Anxiety orange
    EXISTENTIAL = "\033[38;5;21m"  # Melancholy blue
    PUNCHLINE = "\033[38;5;226m"   # Insightful yellow
    RESET = "\033[0m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"

# Woody Allen quote (original creation)
quote = [
    "I've come to the conclusion that the universe is a giant",
    "existential joke played by a committee of bored gods",
    "with terrible sense of humor. And I'm the punchline.",
    "",
    "I'm not afraid of commitment. I'm afraid of being committed.",
    "To anything. Especially to my own thoughts.",
    "",
    "They say 'carpe diem' but what if you're not",
    "particularly fond of diems? What then?",
    "",
    "My therapist says I have a fear of success.",
    "I told him I'm successful at fearing success.",
    "He said 'That's not what I meant.'",
    "I said 'That's what I'm afraid of.'"
]

def typewriter(text, color=Colors.EXISTENTIAL, delay=0.03, jitter=0.01):
    """Print text with Woody's signature hesitant, neurotic typing"""
    for char in text:
        # Random jitter to simulate nervous typing
        time.sleep(delay + random.uniform(-jitter, jitter*2))
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
    print()

def draw_neurotic_border(width):
    """Draw a slightly crooked, neurotic border"""
    sys.stdout.write(Colors.NEUROTIC)
    for i in range(width):
        # Randomly skip a character to look anxious
        if random.random() < 0.1:
            sys.stdout.write("·")
        else:
            sys.stdout.write("─")
        time.sleep(0.005)
    sys.stdout.write(Colors.RESET + "\n")

def main():
    try:
        init_screen()
        
        # Title with neurotic animation
        sys.stdout.write("\n" * 3)
        title = " Woody Allen's Guide to Not Being Okay "
        padding = (80 - len(title)) // 2
        print(" " * padding, end="")
        typewriter(title, Colors.PUNCHLINE, 0.08, 0.03)
        time.sleep(0.5)
        
        # Draw wobbly top border
        sys.stdout.write("\n")
        draw_neurotic_border(76)
        
        # Print quote with dramatic pauses
        for i, line in enumerate(quote):
            if line == "":
                print()
                time.sleep(0.3)
                continue
                
            # Calculate padding (center with slight randomness)
            base_pad = (76 - len(line)) // 2
            pad = base_pad + random.randint(-1, 1)
            print(" " * max(pad, 1), end="")
            
            # Color according to emotional content
            if "punchline" in line.lower() or "afraid" in line.lower():
                color = Colors.PUNCHLINE
                delay = 0.06
            elif "existential" in line.lower() or "universe" in line.lower():
                color = Colors.EXISTENTIAL
                delay = 0.05
            elif "therapist" in line.lower() or "commitment" in line.lower():
                color = Colors.NEUROTIC
                delay = 0.04
            else:
                color = Colors.RESET
                delay = 0.03
                
            typewriter(line, color, delay)
            time.sleep(random.uniform(0.1, 0.3))
        
        # Draw wobbly bottom border
        draw_neurotic_border(76)
        
        # Final neurotic signature
        time.sleep(0.5)
        sig = " — from the mind of someone who should probably be sleeping"
        print("\n" + " " * ((80 - len(sig)) // 2), end="")
        typewriter(sig, Colors.NEUROTIC, 0.04, 0.02)
        
        # Blinking cursor effect
        sys.stdout.write("\n\n")
        for _ in range(3):
            sys.stdout.write("\033[30;5m_\033[0m")
            sys.stdout.flush()
            time.sleep(0.3)
            sys.stdout.write("\b \b")
            sys.stdout.flush()
            time.sleep(0.3)
            
    except KeyboardInterrupt:
        pass
    finally:
        restore_screen()

if __name__ == "__main__":
    main()