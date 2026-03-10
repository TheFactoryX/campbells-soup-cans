"""
Campbell's Soup Can #2681
Produced: 2026-03-10 11:47:41
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def neurotic_typewriter(text, delay=0.03):
    """Print text withTypewriter effect that occasionally stutters nervously"""
    for char in text:
        if random.random() < 0.05:  # 5% chance of nervous stutter
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay * 3)  # Longer pause for stutter
            sys.stdout.write(char)  # Repeat the character
            sys.stdout.flush()
        else:
            sys.stdout.write(char)
            sys.stdout.flush()
        time.sleep(delay)
    print()

def existential_crisis_box():
    """Create an animated Woody Allen-style existential crisis"""
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    
    # Random neurotic colors
    colors = [
        '\033[38;5;226m',  # nervous yellow
        '\033[38;5;204m',  # anxious pink
        '\033[38;5;122m',  # worried mint
        '\033[38;5;45m',   # existential cyan
        '\033[38;5;201m',  # self-conscious magenta
    ]
    reset = '\033[0m'
    
    # Top of anxiety box
    print("\n" + " " * 10 + colors[3] + "╔" + "═" * 60 + "╗" + reset)
    
    # Animated opening
    for i in range(3):
        print("\r" + " " * 10 + colors[2] + "║ " + " " * 58 + "║" + reset, end="")
        time.sleep(0.1)
        print("\r" + " " * 10 + colors[2] + "║ " + "..." + " " * 55 + "║" + reset, end="")
        time.sleep(0.1)
    
    print("\r" + " " * 10 + colors[2] + "║ " + reset, end="")
    
    # Typewriter effect with colored words
    words = quote.split()
    color_index = 0
    
    for i, word in enumerate(words):
        # Cycle through colors restlessly
        color = colors[color_index % len(colors)]
        sys.stdout.write(color)
        
        # Punctuation gets special treatment
        if word.endswith((';', ':', ',')):
            neurotic_typewriter(word, delay=0.02)
        elif word.endswith('.'):
            neurotic_typewriter(word + " ", delay=0.05)
            sys.stdout.write(reset)
            # Add existential sigh after sentence
            time.sleep(0.3)
            sys.stdout.write(colors[4] + "..." + reset + "\n")
            time.sleep(0.2)
            sys.stdout.write(" " * 12 + colors[1] + "│ " + reset)
        else:
            neurotic_typewriter(word + " ", delay=0.01)
        
        sys.stdout.write(reset)
        color_index += 1
    
    # Bottom of anxiety box
    print("\n" + " " * 10 + colors[3] + "╚" + "═" * 60 + "╝" + reset)
    
    # Signature in tiny, faded text
    time.sleep(0.5)
    print("\n" + " " * 30 + '\033[38;5;244m' + "— Woody, probably" + reset)
    
    # Final existential shrug animation
    time.sleep(1)
    shrug = [
        "        \\|/",
        "       /- \\",
        "      /_/ \\_\\",
        "     (     )",
        "    (       )",
        "   (         )",
        "    (       )",
        "     (     )",
        "      '-.-'   "
    ]
    
    for line in shrug:
        print("\r" + " " * 30 + '\033[38;5;8m' + line + reset, end="")
        time.sleep(0.1)
    print("\n")

if __name__ == "__main__":
    try:
        existential_crisis_box()
    except KeyboardInterrupt:
        print("\n\n" + '\033[38;5;196m' + "Typical. Even my program has commitment issues." + reset)